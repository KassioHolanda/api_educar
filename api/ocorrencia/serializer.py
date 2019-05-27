from rest_framework import serializers
from ocorrencia.models import *


class TipoOcorrenciaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TipoOcorrencia
        fields = 'id', 'funcionario', 'enviasms', 'descricao', 'codigo'


class OcorrenciaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ocorrencia
        fields = ('id', 'datahoracadastro', 'funcionarioescola', 'descricao', 'matriculaaluno', 'tipoocorrencia',
                  'aluno', 'anoletivo', 'funcionario', 'unidade', 'enviadosms', 'anoletivo', 'dataenviosms',
                  'resumosms', 'observacao', 'numerotelefone')


class OcorrenciaSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = Ocorrencia
        fields = ('id',
                  'datahoracadastro',
                  'funcionarioescola',
                  'descricao',
                  'matriculaaluno',
                  'tipoocorrencia',
                  'aluno',
                  'anoletivo',
                  'funcionario',
                  'unidade',
                  'enviadosms',
                  'anoletivo',
                  'dataenviosms',
                  'resumosms',
                  'observacao',
                  'numerotelefone')
