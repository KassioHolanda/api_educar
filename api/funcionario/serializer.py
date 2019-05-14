from rest_framework import serializers

from funcionario.models import Cargo, FuncionarioEscola, Funcionario
from pessoa.models import PessoaFisica
from pessoa.serializer import PessoaFisicaSerializer
from unidade.serializer import UnidadeSerializer


class CargoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cargo
        fields = 'id', 'abreviacao', 'descricao'


class FuncionarioEscolaSerializer(serializers.HyperlinkedModelSerializer):
    unidade = UnidadeSerializer(many=False)

    class Meta:
        model = FuncionarioEscola
        fields = ('id',
                  'ativo',
                  'unidade',
                  # 'funcionario'
                  )

class FuncionarioSerializer(serializers.HyperlinkedModelSerializer):
    cargo = CargoSerializer(many=False)
    funcionario_escolas = FuncionarioEscolaSerializer(many=True)
    pessoafisica = PessoaFisicaSerializer(many=False)
    # grade_curso = GradeCursoSerializer(many=True)
    class Meta:
        model = Funcionario
        fields = ('id', 'escolaridade',
                  # 'pessoafisica',
                  'cargo',
                  'cargahoraria',
                  'situacaofuncional',
                  'funcionario_escolas',
                  'dataadmissao',
                  'statusfuncionario',
                  # 'grade_curso',
                  'pessoafisica'
                  )

class FuncionarioSerializerAjuda(serializers.HyperlinkedModelSerializer):
    cargo = CargoSerializer(many=False)
    pessoafisica = PessoaFisicaSerializer(many=False)
    funcionario_escolas = FuncionarioEscolaSerializer(many=True)

    # grade_curso = GradeCursoSerializer(many=True)
    class Meta:
        model = Funcionario
        fields = ('id', 'escolaridade',
                  # 'pessoafisica',
                  'cargo',
                  'cargahoraria',
                  'situacaofuncional',
                  'funcionario_escolas',
                  'dataadmissao',
                  'statusfuncionario',
                  'pessoafisica'
                  # 'grade_curso'
                  )
