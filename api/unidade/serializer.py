from rest_framework import serializers

from aluno.serializer import *
from grade.serializer import *
from unidade.models import *


class FechamentoUnidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FechamentoUnidade
        fields = '__all__'


class UnidadeSerializer(serializers.ModelSerializer):
    # fechamento_unidade = FechamentoUnidadeSerializer(many=True)

    class Meta:
        model = Unidade
        fields = ('id',
                  'abreviacao',
                  'cnpj',
                  'nome',
                  # 'fechamento_unidade'
                  )


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
