from rest_framework import serializers

from aluno.models import *


class AlunoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Aluno
        fields = ('id', 'pessoafisica', 'datacadastro')


class MatriculaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Matricula
        fields = 'id', 'aluno', 'turma', 'statusmatricula', 'datamatricula', 'statusatual', 'serie', 'anoletivo'


class AlunoFrequenciaMesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AlunoFrequenciaMes
        fields = 'id','totalfaltas', 'tipolancamentofrequencia', 'matricula', 'bimestre', 'disciplina', 'disciplinaaluno'
