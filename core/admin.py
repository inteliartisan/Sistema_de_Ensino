from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from .models import (
    UsuarioPersonalizado, PostoGraduacao, Disciplina, Estudante, Instrutor, Monitor, Inscricao, Escore, Presenca
)

@admin.register(UsuarioPersonalizado)
class UsuarioPersonalizadoAdmin(BaseUserAdmin):
    list_display = ('email', 'primeiro_nome', 'sobrenome', 'is_staff', 'is_superuser', 'is_active')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('email', 'primeiro_nome', 'sobrenome')
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Informações Pessoais'), {'fields': ('primeiro_nome', 'sobrenome')}),
        (_('Permissões'), {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Datas importantes'), {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'primeiro_nome', 'sobrenome', 'password1', 'password2'),
        }),
    ) 

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
    search_fields = ('matricula', 'posto_graduacao__posto_graduacao', 'primeiro_nome', 'sobrenome', 'nome_guerra', 'data_de_aniversario', 'email')
    list_filter = ('posto_graduacao', 'nome_guerra',)
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
    search_fields = ('matricula', 'posto_graduacao__posto_graduacao', 'primeiro_nome', 'sobrenome', 'nome_guerra', 'email')
    list_filter = ('posto_graduacao', 'nome_guerra',)
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
    search_fields = ('matricula', 'posto_graduacao__posto_graduacao', 'primeiro_nome', 'sobrenome', 'nome_guerra', 'email')
    list_filter = ('posto_graduacao', 'nome_guerra',)
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
    list_filter = ('data', 'status')

