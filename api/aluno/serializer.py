from rest_framework import serializers

from aluno.models import Aluno, Matricula, AlunoFrequenciaMes
from grade.serializer import SerieSerializer, AnoLetivoSerializer, DisciplinaAlunoSerializer
from nota.serializer import AlunoNotaMesSerializer, DisciplinaSerializer
from bimestre.serializer import *
from ocorrencia.serializer import OcorrenciaSerializer
from pessoa.models import PessoaFisica


class PessoaFisicaAlunoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PessoaFisica
        fields = 'id', 'cpf', 'nome', 'nacionalidade', 'sexo', 'email', 'senha', 'datanascimento', 'rg',


class AlunoSerializer(serializers.HyperlinkedModelSerializer):
    pessoafisica = PessoaFisicaAlunoSerializer(many=False)

    class Meta:
        model = Aluno
        fields = ('id', 'pessoafisica', 'datacadastro')


class MatriculaSerializer(serializers.HyperlinkedModelSerializer):
    aluno = AlunoSerializer(many=False)
    # # turma = TurmaSerializer(many=False)
    serie = SerieSerializer(many=False)
    anoletivo = AnoLetivoSerializer(many=False)
    todas_disciplinas_aluno = DisciplinaAlunoSerializer(many=True)

    class Meta:
        model = Matricula
        fields = 'id', 'aluno', 'statusmatricula', 'datamatricula', 'statusatual', 'serie', 'anoletivo', 'todas_disciplinas_aluno',


class AlunoFrequenciaMesSerializer(serializers.ModelSerializer):
    bimestre = BimestreSerializer(many=False)
    # matricula = MatriculaSerializer(many=False)
    disciplina = DisciplinaSerializer(many=False)

    class Meta:
        model = AlunoFrequenciaMes
        fields = (
            'id',
            'totalfaltas',
            'tipolancamentofrequencia',
            'matricula',
            'bimestre',
            'disciplina',
            'disciplinaaluno',
        )


# UTILIZADO PARA FAZER AS REQUISIÇÕES
class AlunoFrequenciaMesSerializerPost(serializers.ModelSerializer):

    class Meta:
        model = AlunoFrequenciaMes
        fields = (
            'id',
            'totalfaltas',
            'tipolancamentofrequencia',
            'matricula',
            'bimestre',
            'disciplina',
            'disciplinaaluno',
        )


class MatriculaSerializacaoAlunoFrequenciaMesEAlunoNotaMes(serializers.HyperlinkedModelSerializer):
    # aluno = AlunoSerializer(many=False)
    # # turma = TurmaSerializer(many=False)
    # serie = SerieSerializer(many=False)
    # anoletivo = AnoLetivoSerializer(many=False)
    # todas_disciplinas_aluno = DisciplinaAlunoSerializer(many=True)

    aluno_frequencia_mes = AlunoFrequenciaMesSerializer(many=True)
    aluno_nota_mes = AlunoNotaMesSerializer(many=True)
    ocorrencias = OcorrenciaSerializer(many=True)

    class Meta:
        model = Matricula
        fields = 'id', 'aluno_frequencia_mes', 'aluno_nota_mes', 'ocorrencias'
