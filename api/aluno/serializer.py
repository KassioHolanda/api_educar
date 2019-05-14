from rest_framework import serializers

from aluno.models import Aluno, Matricula, AlunoFrequenciaMes
from grade.serializer import SerieSerializer, AnoLetivoSerializer, DisciplinaAlunoSerializer
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


class AlunoFrequenciaMesSerializer(serializers.HyperlinkedModelSerializer):
    # bimestre = BimestreSerializer(many=False)
    # matricula = MatriculaSerializer(many=False)

    class Meta:
        model = AlunoFrequenciaMes
        fields = 'id', 'totalfaltas', 'tipolancamentofrequencia', 'matricula', 'bimestre', 'disciplina', 'disciplinaaluno'
