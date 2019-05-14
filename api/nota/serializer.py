from rest_framework import serializers
from nota.models import AlunoNotaMes
from aluno.views import *
from bimestre.views import *

from bimestre.models import *
from bimestre.serializer import *
from aluno.serializer import *


class AlunoNotaMesSerializer(serializers.HyperlinkedModelSerializer):
    bimestre = BimestreSerializer(many=False)
    # matricula = MatriculaSerializer(many=False)
    # disciplinaaluno = DisciplinaAlunoSerializer(many=False)
    # anoletivo = AnoLetivoSerializer(many=False)
    # disciplina = DisciplinaSerializer(many=False)
    # usuario = UsuarioSerializer(many=False)

    class Meta:
        model = AlunoNotaMes
        fields = (
            'nota',
            'bimestre',
            'sequencia',
            # 'disciplinaaluno',
            'inseridofechamento',
            'tipolancamentonota',
            'anoletivo',
            'disciplina',
            'datahora',
            'usuario')
