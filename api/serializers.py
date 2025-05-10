from rest_framework import serializers

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

class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields = '__all__'

class PostoGraduacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostoGraduacao
        fields = '__all__'

class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = '__all__'

class InstrutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instrutor
        fields = '__all__'

class MonitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monitor
        fields = '__all__'

class InscricaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscricao
        fields = '__all__'

class EscoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Escore
        fields = '__all__'

class PresencaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Presenca
        fields = '__all__'