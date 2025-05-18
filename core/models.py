from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class GerenciarUsuarios(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('O campo de e-mail deve ser preenchido')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superusuario precisa ser is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superusuario precisa ser is_superuser=True.')
        return self.create_user(email, password, **extra_fields)
    
class UsuarioPersonalizado(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    primeiro_nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['primeiro_nome', 'sobrenome']

    objects = GerenciarUsuarios()

    def __str__(self):
        return self.email

class Disciplina(models.Model):
    codigo = models.CharField('Código da Disciplina', max_length=10, unique=True)
    nome = models.CharField('Nome', max_length=30)
    descricao = models.TextField('Descrição')
    carga_horaria = models.IntegerField('Carga Horária')
    creditos = models.IntegerField('Créditos')

    def __str__(self):
        return self.nome
    
class PostoGraduacao(models.Model):
    posto_graduacao = models.CharField(max_length=20)

    def __str__(self):
        return self.posto_graduacao

class Estudante(models.Model):
    matricula = models.CharField('Matrícula', max_length=10, unique=True)
    primeiro_nome = models.CharField('Primeiro Nome', max_length=30)
    sobrenome = models.CharField('Sobrenome', max_length=50)
    posto_graduacao = models.ForeignKey(PostoGraduacao, on_delete=models.CASCADE)
    nome_guerra = models.CharField('Nome de Guerra', max_length=30)
    data_de_aniversario = models.DateField('Data de Aniversário')
    email = models.EmailField('E-mail', unique=True)

    def __str__(self):
        return f"{self.primeiro_nome} {self.sobrenome}"

class Instrutor(models.Model):
    matricula = models.CharField('Matrícula', max_length=10, unique=True)
    primeiro_nome = models.CharField('Primeiro Nome', max_length=30)
    sobrenome = models.CharField('Sobrenome', max_length=50)
    posto_graduacao = models.ForeignKey(PostoGraduacao, on_delete=models.CASCADE)
    nome_guerra = models.CharField('Nome de Guerra', max_length=30)
    email = models.EmailField('E-mail', unique=True)
    disciplina = models.ForeignKey('Disciplina', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.primeiro_nome} {self.sobrenome} - {self.disciplina}"

class Monitor(models.Model):
    matricula = models.CharField('Matrícula', max_length=10, unique=True)
    primeiro_nome = models.CharField('Primeiro Nome', max_length=30)
    sobrenome = models.CharField('Sobrenome', max_length=50)
    posto_graduacao = models.ForeignKey(PostoGraduacao, on_delete=models.CASCADE)
    nome_guerra = models.CharField('Nome de Guerra', max_length=30)
    email = models.EmailField('E-mail', unique=True)
    disciplina = models.ForeignKey('Disciplina', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.primeiro_nome} {self.sobrenome} - {self.disciplina}"

class Inscricao(models.Model):
    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    data_de_inscricao = models.DateField('Data de Inscrição', auto_now_add=True)

    def __str__(self):
        return f"{self.estudante} inscrito na disciplina {self.disciplina}"
    
class Escore(models.Model):
    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    escore = models.DecimalField(max_digits=5, decimal_places=2)
    data_do_registro = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.estudante} - {self.disciplina}: {self.escore}'

class Presenca(models.Model):
    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE)
    data = models.DateField()
    status = models.CharField(max_length=10, choices=[('Presente', 'Presente'), ('Ausente', 'Ausente')])

    def __str__(self):
        return f'{self.estudante} - {self.data} - {self.status}'

