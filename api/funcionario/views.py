from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status, permissions
from funcionario.models import *
from rest_framework.response import Response
from rest_framework.reverse import reverse
from funcionario.serializer import *
from unidade.views import *
from rest_framework import filters, viewsets

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
from rest_framework import generics


class FuncionarioList(generics.ListAPIView):
    name = 'funcionario-list'
    queryset = Funcionario.objects.filter(cargo=5)
    serializer_class = FuncionarioSerializerAjuda


class FuncionarioDetail(generics.RetrieveAPIView):
    name = 'funcionario-detail'
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializerAjuda


class FuncionarioPessoaFisica(APIView):
    def get_object(self, pessoafisica):
        return Funcionario.objects.filter(pessoafisica=pessoafisica, cargo=5)

    def get(self, request, pessoafisica, format=None):
        funcionario = self.get_object(pessoafisica)
        serializer = FuncionarioSerializer(funcionario, many=True)
        return Response(serializer.data)

class FuncionarioCPF(APIView):
    def get_object(self, cpf):
        pessoa = PessoaFisica.objects.get(cpf=cpf)
        return Funcionario.objects.filter(pessoafisica=pessoa, cargo=5)

    def get(self, request, cpf, format=None):
        funcionario = self.get_object(cpf)
        serializer = FuncionarioSerializer(funcionario, many=True)
        return Response(serializer.data)


class CargoList(generics.ListAPIView):
    name = 'cargo-list'
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer


class CargoDetalhe(generics.RetrieveAPIView):
    name = 'cargo-detail'
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer


class FuncionarioEscolaLista(generics.ListAPIView):
    name = 'funcionarioescola-list'
    queryset = FuncionarioEscola.objects.all()
    serializer_class = FuncionarioEscolaSerializer


class FuncionarioEscolaDetalhe(generics.RetrieveAPIView):
    name = 'funcionarioescola-detail'
    queryset = FuncionarioEscola.objects.select_related('funcionario', 'unidade').all()
    serializer_class = FuncionarioEscolaSerializer


class FuncionarioEscolaFuncionario(APIView):
    def get_object(self, funcionario):
        return FuncionarioEscola.objects.filter(funcionario=funcionario)

    def get(self, request, funcionario, format=None):
        usuario = self.get_object(funcionario)
        serializer = FuncionarioEscolaSerializer(usuario, many=True)
        return Response(serializer.data)
