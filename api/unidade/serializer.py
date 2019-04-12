from rest_framework import serializers

from unidade.models import Unidade, LocalEscola, Turma, Serie, SerieTurma


class UnidadeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Unidade
        fields = 'id', 'abreviacao', 'cnpj', 'nome'


class LocalEscolaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LocalEscola
        fields = 'id', 'descricao', 'unidade'


class TurmaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Turma
        fields = 'id', 'descricao', 'turno', 'sala', 'anoletivo', 'serie', 'nivel', 'statusturma'


class SerieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Serie
        fields = 'id', 'descricao', 'nivel'


class SerieTurmaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SerieTurma
        fields = 'id', 'serie', 'turma'
