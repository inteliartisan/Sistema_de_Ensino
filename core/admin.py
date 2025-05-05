from django.contrib import admin

from.models import  PostoGraduacao, Disciplina, Estudante, Instrutor, Monitor, Inscricao, Escore, Presenca

@admin.register(PostoGraduacao)
class PostoGraduacaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'posto_graduacao')
    search_fields = ('posto_graduacao',)

@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nome', 'carga_horaria', 'creditos')
    search_fields = ('nome',)
    list_filter = ('nome',)

@admin.register(Estudante)
class EstudanteAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'posto_graduacao', 'primeiro_nome', 'sobrenome', 'nome_guerra', 'data_de_aniversario', 'email')
    search_fields = ('matricula', 'posto_graduacao', 'primeiro_nome', 'sobrenome', 'nome_guerra', 'data_de_aniversario', 'email')
    list_filter = ('nome_guerra',)
    readonly_fields = ('email',)
    fieldsets = (
        ('Informações Pessoais', {
            'fields': ('primeiro_nome', 'sobrenome', 'data_de_aniversario', 'email')
        }),
        ('Informações Militares', { 
            'fields': ('matricula','posto_graduacao', 'nome_guerra')
        }),
    )

@admin.register(Instrutor)
class InstrutorAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'posto_graduacao', 'primeiro_nome', 'sobrenome', 'nome_guerra', 'email')
    search_fields = ('matricula', 'posto_graduacao', 'primeiro_nome', 'sobrenome', 'nome_guerra', 'email')
    list_filter = ('nome_guerra',)
    readonly_fields = ('email',)
    fieldsets = (
        ('Informações Pessoais', { 
            'fields': ('primeiro_nome', 'sobrenome', 'email')
        }),
        ('Informações Militares', {
            'fields': ('matricula', 'posto_graduacao', 'nome_guerra')
        }),
    )

@admin.register(Monitor)
class MonitorAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'posto_graduacao', 'primeiro_nome', 'sobrenome', 'nome_guerra', 'email')
    search_fields = ('matricula', 'posto_graduacao', 'primeiro_nome', 'sobrenome', 'nome_guerra', 'email')
    list_filter = ('nome_guerra',)
    readonly_fields = ('email',)
    fieldsets = (
        ('Informações Pessoais', { 
            'fields': ('primeiro_nome', 'sobrenome', 'email')
        }),
        ('Informações Militares', {
            'fields': ('matricula', 'posto_graduacao', 'nome_guerra')
        }),
    )

@admin.register(Inscricao)
class InscricaoAdmin(admin.ModelAdmin):
    list_display = ('estudante', 'disciplina', 'data_de_inscricao')
    search_fields = ('estudante__primeiro_nome', 'disciplina__nome')
    list_filter = ('estudante',)

@admin.register(Escore)
class EscoreAdmin(admin.ModelAdmin):
    list_display = ('estudante', 'disciplina', 'escore')
    search_fields = ('estudante__primeiro_nome', 'disciplina__nome')
    list_filter = ('estudante',)

@admin.register(Presenca)
class PresencaAdmin(admin.ModelAdmin):
    list_display = ('estudante', 'data', 'status')
    search_fields = ('estudante__primeiro_nome',)
