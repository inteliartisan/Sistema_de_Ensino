from django.db import models

class Disciplina(models.Model):
    codigo = models.CharField('Código da Disciplina', max_length=10, unique=True)
    nome = models.CharField('Nome', max_length=50)
    descricao = models.TextField('Descrição')
    carga_horaria = models.IntegerField('Carga Horária')
    creditos = models.IntegerField('Créditos')

    def __str__(self):
        return self.nome

class Estudante(models.Model):
    matricula = models.CharField('Matrícula', max_length=50, unique=True)
    primeiro_nome = models.CharField('Primeiro Nome', max_length=50)
    sobrenome = models.CharField('Sobrenome', max_length=50)
    posto_graduacao = models.CharField('Posto ou Graduação', max_length=50)
    nome_guerra = models.CharField('Nome de Guerra', max_length=50)
    data_de_aniversario = models.DateField('Data de Aniversário')
    email = models.EmailField('E-mail', unique=True)

    def __str__(self):
        return f"{self.primeiro_nome} {self.sobrenome}"

class Instrutor(models.Model):
    matricula = models.CharField('Matrícula', max_length=50, unique=True)
    primeiro_nome = models.CharField('Primeiro Nome', max_length=50)
    sobrenome = models.CharField('Último Nome', max_length=50)
    posto_graduacao = models.CharField('Posto ou Graduação', max_length=50)
    nome_guerra = models.CharField('Nome de Guerra', max_length=50)
    email = models.EmailField('E-mail', unique=True)
    disciplina = models.ForeignKey('Disciplina', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.primeiro_nome} {self.sobrenome} - {self.disciplina}"

class Monitor(models.Model):
    matricula = models.CharField('Matrícula', max_length=50, unique=True)
    primeiro_nome = models.CharField('Primeiro Nome', max_length=50)
    sobrenome = models.CharField('Último Nome', max_length=50)
    posto_graduacao = models.CharField('Posto ou Graduação', max_length=50)
    nome_guerra = models.CharField('Nome de Guerra', max_length=50)
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

