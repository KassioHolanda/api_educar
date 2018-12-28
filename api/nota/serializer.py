from rest_framework import serializers
from nota.models import AlunoNotaMes

class AlunoNotaMesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlunoNotaMes
        fields = '__all__'
