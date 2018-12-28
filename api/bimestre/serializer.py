from rest_framework import serializers

from bimestre.models import Bimestre


class BimestreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bimestre
        fields = '__all__'
