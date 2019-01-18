from rest_framework import serializers
from ocorrencia.models import *


class TipoOcorrenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoOcorrencia
        fields = '__all__'


class OcorrenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ocorrencia
        fields = '__all__'

