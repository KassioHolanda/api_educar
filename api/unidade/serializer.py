from rest_framework import serializers

from aluno.serializer import MatriculaSerializer
from unidade.models import Unidade, LocalEscola, Turma, Serie, SerieTurma
from grade.serializer import *


class UnidadeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Unidade
        fields = ('id', 'abreviacao', 'cnpj', 'nome')


class LocalEscolaSerializer(serializers.HyperlinkedModelSerializer):
    unidade = UnidadeSerializer(many=False)

    class Meta:
        model = LocalEscola
        fields = 'id', 'descricao', 'unidade'


class SerieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Serie
        fields = 'id', 'descricao', 'nivel'


class SerieTurmaSerializer(serializers.HyperlinkedModelSerializer):
    serie = SerieSerializer(many=False)
    turma = TurmaSerializer(many=False)

    class Meta:
        model = SerieTurma
        fields = 'id', 'serie', 'turma'


class TurmaSerializer(serializers.HyperlinkedModelSerializer):
    sala = LocalEscolaSerializer(many=False)
    anoletivo = AnoLetivoSerializer(many=False)
    serie = SerieSerializer(many=False)
    matriculas = MatriculaSerializer(many=True)
    situacao_turma_mes = SituacaoTurmaMesSerializer(many=True)

    class Meta:
        model = Turma
        fields = ('id', 'descricao', 'turno', 'sala', 'anoletivo', 'serie', 'nivel', 'statusturma',
                  'matriculas',
                  'situacao_turma_mes'
                  )


class TurmaSerializerSimplificada(serializers.HyperlinkedModelSerializer):
    sala = LocalEscolaSerializer(many=False)
    anoletivo = AnoLetivoSerializer(many=False)
    serie = SerieSerializer(many=False)
    # matriculas = MatriculaSerializer(many=True)

    class Meta:
        model = Turma
        fields = 'id', 'descricao', 'turno', 'sala', 'anoletivo', 'serie', 'nivel', 'statusturma',

