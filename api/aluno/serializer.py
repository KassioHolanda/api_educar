from rest_framework import serializers

from aluno.models import *


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'


class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = '__all__'


class AlunoFrequenciaMesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlunoFrequenciaMes
        fields = '__all__'
