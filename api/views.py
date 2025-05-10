from rest_framework import viewsets

from core.models import (
    Disciplina, 
    PostoGraduacao, 
    Estudante, 
    Instrutor, 
    Monitor, 
    Inscricao, 
    Escore, 
    Presenca,
) 

from .serializers import (
    DisciplinaSerializer, 
    PostoGraduacaoSerializer, 
    EstudanteSerializer, 
    InstrutorSerializer, 
    MonitorSerializer, 
    InscricaoSerializer, 
    EscoreSerializer, 
    PresencaSerializer,
)

class DisciplinaViewSet(viewsets.ModelViewSet):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer

class PostoGraduacaoViewSet(viewsets.ModelViewSet):
    queryset = PostoGraduacao.objects.all()
    serializer_class = PostoGraduacaoSerializer

class EstudanteViewSet(viewsets.ModelViewSet):
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer

class InstrutorViewSet(viewsets.ModelViewSet):
    queryset = Instrutor.objects.all()
    serializer_class = InstrutorSerializer

class MonitorViewSet(viewsets.ModelViewSet):
    queryset = Monitor.objects.all()
    serializer_class = MonitorSerializer

class InscricaoViewSet(viewsets.ModelViewSet):
    queryset = Inscricao.objects.all()
    serializer_class = InscricaoSerializer

class EscoreViewSet(viewsets.ModelViewSet):
    queryset = Escore.objects.all()
    serializer_class = EscoreSerializer

class PresencaViewSet(viewsets.ModelViewSet):
    queryset = Presenca.objects.all()
    serializer_class = PresencaSerializer


