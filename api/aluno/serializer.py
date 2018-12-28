from rest_framework import serializers

from aluno.models import *


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = 'id', 'pessoafisica', 'datacadastro'


class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = 'id', 'aluno', 'turma', 'statusmatricula', 'datamatricula', 'statusatual'


class AlunoFrequenciaMesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlunoFrequenciaMes
        fields = 'id', 'totalfaltas', 'matricula', 'bimestre'
