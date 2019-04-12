from rest_framework import serializers
from nota.models import AlunoNotaMes
from aluno.views import *
from bimestre.views import *

from bimestre.models import *
from bimestre.serializer import *


class AlunoNotaMesSerializer(serializers.HyperlinkedModelSerializer):
    # bimestre = BimestreSerializer(many=False, read_only=False)

    class Meta:
        model = AlunoNotaMes
        fields = (
            'nota', 'bimestre', 'sequencia', 'disciplinaaluno', 'inseridofechamento', 'tipolancamentonota', 'anoletivo',
            'matricula', 'unidade', 'unidade', 'disciplina', 'datahora', 'usuario')
