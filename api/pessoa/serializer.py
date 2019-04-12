from rest_framework import serializers

from pessoa.models import PessoaFisica, Usuario, Perfil


class PessoaFisicaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PessoaFisica
        fields = 'id', 'cpf', 'nome', 'nacionalidade', 'sexo', 'email', 'senha', 'datanascimento', 'rg'


class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = 'id', 'ativo', 'login', 'matricula', 'senha', 'pessoafisica', 'perfil'


class PerfilSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Perfil
        fields = 'id', 'perfilexterno', 'vertodasasescolas'
