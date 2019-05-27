from rest_framework import serializers, request
from rest_framework.request import Request

from aluno.serializer import MatriculaSerializer
from grade.models import GradeCurso, Disciplina, SerieDisciplina, AnoLetivo, SituacaoTurmaMes, DisciplinaAluno
from grade.serializer import TurmaSerializer, SerieDisciplinaSerializer, DisciplinaSerializer
from pessoa.models import PessoaFisica, Usuario, Perfil
from funcionario.serializer import *
from unidade.models import LocalEscola, Unidade, Serie, Turma, SerieTurma
from unidade.serializer import SerieSerializer


class AnoLetivoSerializerHelper(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AnoLetivo
        fields = 'id', 'datafinal', 'datainicio', 'fechadonota'


class GradeCursoSerializerHelper(serializers.HyperlinkedModelSerializer):
    # turma = TurmaSerializerHelper(many=False)
    seriedisciplina = SerieDisciplinaSerializer(many=False)
    disciplina = DisciplinaSerializer(many=False)

    class Meta:
        model = GradeCurso
        fields = ('id',
                  # 'professor',
                  'seriedisciplina',
                  # 'turma',
                  'disciplina'
                  )

class SituacaoTurmaMesSerializerHelper(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SituacaoTurmaMes
        fields = 'id', 'datahora', 'status', 'quantidadeaprovados', 'quantidadereprovados', 'bimestre'


class TurmaSerializerHelper(serializers.HyperlinkedModelSerializer):
    # sala = LocalEscolaSerializerHelper(many=False)
    anoletivo = AnoLetivoSerializerHelper(many=False)
    serie = SerieSerializer(many=False)
    grade_curso = GradeCursoSerializerHelper(many=True)
    # matriculas = MatriculaSerializer(many=True)

    class Meta:
        model = Turma
        fields = ('id', 'descricao', 'turno', 'anoletivo', 'nivel', 'statusturma', 'anoletivo', 'serie', 'grade_curso',
                 # 'matriculas',
                 #  'situacao_turma_mes'
                  )


class LocalEscolaSerializerHelper(serializers.HyperlinkedModelSerializer):
    # unidade = UnidadeSerializer(many=False)
    turmas = TurmaSerializerHelper(many=True)

    class Meta:
        model = LocalEscola
        fields = 'id', 'descricao', 'turmas'


class UnidadeSerializerHelper(serializers.HyperlinkedModelSerializer):
    locais_escola = LocalEscolaSerializerHelper(many=True)

    class Meta:
        model = Unidade
        fields = ('id',
                  'abreviacao',
                  'cnpj',
                  'locais_escola',
                  'nome'
                  )


class CargoSerializerHelper(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cargo
        fields = 'id', 'abreviacao', 'descricao'


class FuncionarioEscolaSerializerHelper(serializers.HyperlinkedModelSerializer):
    unidade = UnidadeSerializerHelper(many=False)

    # grade_curso = GradeCursoSerializerHelper(many=True)

    class Meta:
        model = FuncionarioEscola
        fields = ('id',
                  'ativo',
                  'unidade',
                  # 'funcionario'
                  # 'grade_curso'
                  )


class PerfilSerializerHelper(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Perfil
        fields = ('id',
                  'perfilexterno',
                  'vertodasasescolas')


class UsuarioSerializerHelper(serializers.HyperlinkedModelSerializer):
    perfil = PerfilSerializerHelper(many=False)

    # pessoafisica = PessoaFisicaSerializerHelper(many=False)

    class Meta:
        model = Usuario
        fields = ('id',
                  'ativo',
                  'login',
                  'matricula',
                  'senha',
                  # 'pessoafisica',
                  'perfil')


class PessoaFisicaSerializerHelper(serializers.HyperlinkedModelSerializer, ):
    usuario = UsuarioSerializerHelper(many=False)

    class Meta:
        model = PessoaFisica
        fields = 'id', 'cpf', 'nome', 'nacionalidade', 'sexo', 'email', 'senha', 'datanascimento', 'rg', 'usuario'


class FuncionarioSerializerHelper(serializers.HyperlinkedModelSerializer):
    cargo = CargoSerializerHelper(many=False)
    funcionario_escolas = FuncionarioEscolaSerializerHelper(many=True)
    # grade_curso = GradeCursoSerializerHelper(many=True)
    pessoafisica = PessoaFisicaSerializerHelper(many=False)

    class Meta:
        model = Funcionario
        fields = ('id',
                  'escolaridade',
                  # 'pessoafisica',
                  'cargo',
                  'cargahoraria',
                  'situacaofuncional',
                  'funcionario_escolas',
                  'dataadmissao',
                  'statusfuncionario',
                  # 'grade_curso',
                  'pessoafisica',
                  )


class SerieSerializerHelper(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Serie
        fields = 'id', 'descricao', 'nivel'


class SerieTurmaSerializerHelper(serializers.HyperlinkedModelSerializer):
    serie = SerieSerializerHelper(many=False)
    turma = TurmaSerializerHelper(many=False)

    class Meta:
        model = SerieTurma
        fields = 'id', 'serie', 'turma'


class DisciplinaSerializerHelper(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Disciplina
        fields = 'id', 'descricao', 'codigo'


# CODIGO REPETIDO TODO
class SerieSerializerHelper(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Serie
        fields = 'id', 'descricao', 'nivel'


class SerieDisciplinaSerializerHelper(serializers.HyperlinkedModelSerializer):
    # serie = SerieSerializer(many=False)
    # disciplina = DisciplinaSerializer(many=False)

    class Meta:
        model = SerieDisciplina
        fields = 'id', 'serie', 'disciplina'


class DisciplinaAlunoSerializerHelper(serializers.HyperlinkedModelSerializer):
    # seriedisciplina = SerieDisciplinaSerializer(many=False)
    # matricula = MatriculaSerializer(many=False)

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
