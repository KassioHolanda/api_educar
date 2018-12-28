from rest_framework import serializers

from unidade.models import Unidade, LocalEscola, Turma, Serie, SerieTurma


class UnidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unidade
        fields = 'id', 'abreviacao', 'cnpj', 'nome'


class LocalEscolaSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocalEscola
        fields = 'id', 'descricao', 'unidade'


class TurmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turma
        fields = '__all__'


class SerieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serie
        fields = 'id', 'descricao', 'nivel'


class SerieTurmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SerieTurma
        fields = '__all__'
