from rest_framework.reverse import reverse
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import filters, viewsets

from helper.serializer import *
from pessoa.models import PessoaFisica, Usuario, Perfil
from funcionario.models import Funcionario
from django.shortcuts import get_object_or_404
from pessoa.serializer import PessoaFisicaSerializer, UsuarioSerializer, PerfilSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import status


class PessoaFisicaList(generics.ListAPIView):
    queryset = PessoaFisica.objects.all()
    serializer_class = PessoaFisicaSerializer
    name = 'pessoa-list'


class PessoaFisicaDetalhe(generics.RetrieveAPIView):
    queryset = PessoaFisica.objects.all()
    serializer_class = PessoaFisicaSerializer
    name = 'pessoa-detail'


class PessoaFisicaCPF(APIView):
    def get_object(self, cpf):
        return PessoaFisica.objects.filter(cpf=cpf)

    def get(self, request, cpf, format=None):
        pessoa = self.get_object(cpf)
        serializer_context = {
            'request': request,
        }
        serializer = PessoaFisicaSerializer(pessoa, many=True)
        return Response(serializer.data)


class PessoaFisicaCPFMostrarTodasAsClassesSerializadas(APIView):
    name = 'pessoafisica-list'
    def get_object(self, cpf):
        p = PessoaFisica.objects.get(cpf=cpf)
        return Funcionario.objects.select_related('pessoafisica').filter(pessoafisica=p)

    def get(self, request, cpf, format=None):
        pessoa = self.get_object(cpf)
        serializer_context = {
            'request': request,
        }
        serializer = FuncionarioSerializerHelper(pessoa, many=True, context=serializer_context)
        return Response(serializer.data)


class UsuarioList(generics.ListAPIView):
    name = 'usuario-list'
    queryset = Usuario.objects.select_related('perfil', 'pessoafisica').all()
    # queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class UsuarioPessoaFisica(APIView):
    def get_object(self, pessoafisica):
        return Usuario.objects.select_related('pessoafisica').filter(pessoafisica=pessoafisica)

    def get(self, request, pessoafisica, format=None):
        usuario = self.get_object(pessoafisica)
        serializer = UsuarioSerializer(usuario, many=True)
        return Response(serializer.data)


class UsuarioPerfil(APIView):
    def get_object(self, perfil):
        return Usuario.objects.filter(perfil=perfil)

    def get(self, request, perfil, format=None):
        usuario = self.get_object(perfil)
        serializer = UsuarioSerializer(usuario, many=True)
        return Response(serializer.data)


class UsuarioDetalhe(generics.RetrieveAPIView):
    name = 'usuario-detail'
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class PerfilList(generics.ListAPIView):
    name = 'perfil-list'
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer


class PerfilDetalhe(generics.RetrieveAPIView):
    name = 'perfil-detail'
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer

# class ApiRoot(generics.GenericAPIView):
#     name = 'api-root'
#
#     def get(self, request, *args, **kwargs):
#         return Response({
#             'perfil': reverse(PerfilList.name, request=request),
#             'pessoafisica': reverse(PessoaFisicaList.name, request=request),
#             'usuarios': reverse(UsuarioList.name, request=request)
#         })
