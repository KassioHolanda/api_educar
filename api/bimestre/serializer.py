from rest_framework import serializers

from bimestre.models import Bimestre


class BimestreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bimestre
        fields = ('id','descricao', 'sequencia', 'temnota')
