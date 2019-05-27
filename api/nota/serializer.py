from rest_framework import serializers
from aluno.models import *
from bimestre.serializer import *
from grade.serializer import *


# from pessoa.serializer import *


class AlunoNotaMesSerializer(serializers.ModelSerializer):
    bimestre = BimestreSerializer(many=False)
    # matricula = MatriculaSerializer(many=False)
    # disciplinaaluno = DisciplinaAlunoSerializer(many=False)
    anoletivo = AnoLetivoSerializer(many=False)
    disciplina = DisciplinaSerializer(many=False)

    # usuario = UsuarioSerializer(many=False)

    class Meta:
        model = AlunoNotaMes
        fields = (
            'id',
            'nota',
            'bimestre',
            'sequencia',
            'disciplinaaluno',
            'inseridofechamento',
            'tipolancamentonota',
            'anoletivo',
            'disciplina',
            'datahora',
            # 'usuario'
        )


# UTILIZADO PARA FAZER AS REQUISIÇÕES
class AlunoNotaMesSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = AlunoNotaMes
        fields = (
            'id',
            'nota',
            'bimestre',
            'sequencia',
            'disciplinaaluno',
            'inseridofechamento',
            'tipolancamentonota',
            'anoletivo',
            'matricula',
            'unidade',
            'disciplina',
            'datahora',
            'usuario'
        )
