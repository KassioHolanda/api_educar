from django.shortcuts import render
from rest_framework import filters, viewsets
from pessoa.models import PessoaFisica, Usuario, Perfil
from pessoa.serializer import PessoaFisicaSerializer, UsuarioSerializer, PerfilSerializer


class PessoaFisicaViewSet(viewsets.ModelViewSet):
    name = 'pessoafisica'
    queryset = PessoaFisica.objects.all()
    serializer_class = PessoaFisicaSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    name = 'usuario'
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class PerfilViewSet(viewsets.ModelViewSet):
    name = 'perfil'
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer

