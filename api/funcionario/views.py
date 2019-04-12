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


class FuncionarioList(generics.ListCreateAPIView):
    name = 'funcionario-list'
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer


class FuncionarioDetail(generics.RetrieveUpdateDestroyAPIView):
    name = 'funcionario-detail'
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer


class FuncionarioPessoaFisica(APIView):
    def get_object(self, pessoafisica):
        return Funcionario.objects.filter(pessoafisica=pessoafisica)

    def get(self, request, pessoafisica, format=None):
        funcionario = self.get_object(pessoafisica)
        serializer = FuncionarioSerializer(funcionario, many=True)
        return Response(serializer.data)



class CargoList(generics.ListCreateAPIView):
    name = 'cargo-list'
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer


class CargoDetalhe(generics.RetrieveUpdateDestroyAPIView):
    name = 'cargo-detail'
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer


class FuncionarioEscolaLista(generics.ListCreateAPIView):
    name = 'funcionarioescola-list'
    queryset = FuncionarioEscola.objects.all()
    serializer_class = FuncionarioEscolaSerializer


class FuncionarioEscolaDetalhe(generics.RetrieveUpdateDestroyAPIView):
    name = 'funcionarioescola-detail'
    queryset = FuncionarioEscola.objects.all()
    serializer_class = FuncionarioEscolaSerializer


class FuncionarioEscolaFuncionario(APIView):
    def get_object(self, funcionario):
        return FuncionarioEscola.objects.filter(funcionario=funcionario)

    def get(self, request, funcionario, format=None):
        usuario = self.get_object(funcionario)
        serializer = FuncionarioEscolaSerializer(usuario, many=True)
        return Response(serializer.data)
