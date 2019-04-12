from rest_framework import serializers
from funcionario.models import *


class FuncionarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Funcionario
        fields = 'id', 'escolaridade', 'pessoafisica', 'cargo', 'cargahoraria', 'situacaofuncional', 'dataadmissao', 'statusfuncionario'


class CargoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cargo
        fields = 'id', 'abreviacao', 'descricao'


class FuncionarioEscolaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FuncionarioEscola
        fields = 'id', 'ativo', 'unidade', 'funcionario'
