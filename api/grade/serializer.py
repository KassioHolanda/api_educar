from rest_framework import serializers

from aluno.models import Matricula
from bimestre.serializer import BimestreSerializer
from grade.models import *
from unidade.models import Serie, Turma


class DisciplinaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Disciplina
        fields = 'id', 'descricao', 'codigo'


# CODIGO REPETIDO TODO
class SerieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Serie
        fields = 'id', 'descricao', 'nivel'


class SerieDisciplinaSerializer(serializers.HyperlinkedModelSerializer):
    serie = SerieSerializer(many=False)
    disciplina = DisciplinaSerializer(many=False)

    class Meta:
        model = SerieDisciplina
        fields = 'id', 'serie', 'disciplina'


class AnoLetivoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AnoLetivo
        fields = 'id', 'descricao', 'datafinal', 'datainicio', 'fechadonota'


class TurmaSerializer(serializers.HyperlinkedModelSerializer):
    # sala = LocalEscolaSerializer(many=False)
    anoletivo = AnoLetivoSerializer(many=False)
    serie = SerieSerializer(many=False)

    class Meta:
        model = Turma
        fields = 'id', 'descricao', 'turno', 'anoletivo', 'serie', 'nivel', 'statusturma',


class GradeCursoSerializer(serializers.HyperlinkedModelSerializer):
    # turmas = TurmaSerializer(many=True)  NAO DESCONEMNTAR
    seriedisciplina = SerieDisciplinaSerializer(many=False)
    disciplina = DisciplinaSerializer(many=False)

    class Meta:
        model = GradeCurso
        fields = ('id',
                  # 'professor',
                  'seriedisciplina',
                  'turma',
                  'disciplina')


class DisciplinaAlunoSerializer(serializers.HyperlinkedModelSerializer):
    seriedisciplina = SerieDisciplinaSerializer(many=False)
    # matricula = MatriculaSerializer(many=False)

    class Meta:
        model = DisciplinaAluno
        fields = ('id',
                  'cargahoraria',
                  'statusdisciplinaaluno',
                  'statusatual',
                  # 'matricula',
                  'seriedisciplina',
                  'mediaacumulada',
                  'mesesfechadosnota',
                  'notaacumulada',
                  'datacadastroprovafinal',
                  'notaprovafinal',
                  # 'matricula',
                  'fechadoprovafinal',
                  'datacadastroatualizacaoprovafinal',
                  'notaantigaprovafinal',
                  'usuarioatualizacaoprovafinal')


# UTILIZADO PARA FAZER AS REQUISICOES
class DisciplinaAlunoSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = DisciplinaAluno
        fields = ('id',
                  'cargahoraria',
                  'statusdisciplinaaluno',
                  'statusatual',
                  'matricula',
                  'seriedisciplina',
                  'mediaacumulada',
                  'mesesfechadosnota',
                  'notaacumulada',
                  'datacadastroprovafinal',
                  'notaprovafinal',
                  'fechadoprovafinal',
                  'datacadastroatualizacaoprovafinal',
                  'notaantigaprovafinal',
                  'usuarioatualizacaoprovafinal')


class SituacaoTurmaMesSerializer(serializers.HyperlinkedModelSerializer):
    bimestre = BimestreSerializer(many=False)
    class Meta:
        model = SituacaoTurmaMes
        fields = 'id', 'datahora', 'status', 'quantidadeaproados', 'quantidadereprovados', 'bimestre'


# utilizado para fazer as requisicoes
class SituacaoTurmaMesSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = SituacaoTurmaMes
        fields = 'id', 'datahora', 'status', 'quantidadeaproados', 'quantidadereprovados', 'bimestre', 'turma'
