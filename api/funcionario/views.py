from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status, permissions
from funcionario.models import *
from rest_framework.response import Response
from rest_framework.reverse import reverse
from funcionario.serializer import *
from unidade.views import *
from rest_framework import filters, viewsets


class FuncionarioViewSet(viewsets.ModelViewSet):
    name = 'funcionario'
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer


class CargoViewSet(viewsets.ModelViewSet):
    name = 'cargo'
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer


class FuncionarioEscolaViewSet(viewsets.ModelViewSet):
    name = 'funcionarioescola'
    queryset = FuncionarioEscola.objects.all()
    serializer_class = FuncionarioEscolaSerializer

