from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    DisciplinaViewSet, 
    PostoGraduacaoViewSet, 
    EstudanteViewSet, 
    InstrutorViewSet, 
    MonitorViewSet, 
    InscricaoViewSet, 
    EscoreViewSet, 
    PresencaViewSet,
)

router = DefaultRouter()
router.register(r'disciplinas', DisciplinaViewSet)
router.register(r'postos_graduacoes', PostoGraduacaoViewSet)
router.register(r'estudantes', EstudanteViewSet)
router.register(r'instrutores', InstrutorViewSet)
router.register(r'monitores', MonitorViewSet)
router.register(r'inscricoes', InscricaoViewSet)
router.register(r'escores', EscoreViewSet)
router.register(r'presencas', PresencaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
