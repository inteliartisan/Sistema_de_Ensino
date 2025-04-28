from django.contrib import admin

from .models import Disciplina, Estudante, Instrutor, Monitor, Inscricao, Escore, Presenca

admin.site.register(Disciplina)
admin.site.register(Estudante)
admin.site.register(Instrutor)
admin.site.register(Monitor)
admin.site.register(Inscricao)
admin.site.register(Escore)
admin.site.register(Presenca)
