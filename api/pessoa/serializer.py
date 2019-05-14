from rest_framework import serializers

from pessoa.models import PessoaFisica, Usuario, Perfil
from funcionario.serializer import *


class PessoaFisicaSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PessoaFisica
        fields = 'id', 'cpf', 'nome', 'nacionalidade', 'sexo', 'email', 'senha', 'datanascimento', 'rg'


class PerfilSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Perfil
        fields = 'id', 'perfilexterno', 'vertodasasescolas'


class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    perfil = PerfilSerializer(many=False)
    pessoafisica = PessoaFisicaSerializer(many=False)

    class Meta:
        model = Usuario
        fields = 'id', 'ativo', 'login', 'matricula', 'senha', 'pessoafisica', 'perfil'
