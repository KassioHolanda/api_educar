from rest_framework.reverse import reverse
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import filters, viewsets
from pessoa.models import PessoaFisica, Usuario, Perfil
from django.shortcuts import get_object_or_404
from pessoa.serializer import PessoaFisicaSerializer, UsuarioSerializer, PerfilSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import status


class PessoaFisicaList(generics.ListAPIView):
    queryset = PessoaFisica.objects.all()
    serializer_class = PessoaFisicaSerializer
    name = 'pessoa-list'


class PessoaFisicaDetalhe(APIView):
    def get_object(self, id):
        return PessoaFisica.objects.filter(id=id)

    def get(self, request, id, format=None):
        pessoa = self.get_object(id)
        serializer = PessoaFisicaSerializer(pessoa, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PessoaFisicaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id, format=None):
        post = self.get_object(id)
        serializer = PessoaFisicaSerializer(post, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PessoaFisicaCPF(APIView):
    def get_object(self, cpf):
        return PessoaFisica.objects.filter(cpf=cpf)

    def get(self, request, cpf, format=None):
        pessoa = self.get_object(cpf)
        serializer = PessoaFisicaSerializer(pessoa, many=True)
        return Response(serializer.data)


class UsuarioList(generics.ListAPIView):
    name = 'usuario-list'
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class UsuarioPessoaFisica(APIView):
    def get_object(self, pessoafisica):
        return Usuario.objects.filter(pessoafisica=pessoafisica)

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


class UsuarioDetalhe(APIView):
    def get_object(self, id):
        return Usuario.objects.filter(id=id)

    def get(self, request, id, format=None):
        usuario = self.get_object(id)
        serializer = UsuarioSerializer(usuario, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id, format=None):
        post = self.get_object(id)
        serializer = UsuarioSerializer(post, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PerfilList(generics.ListAPIView):
    name = 'perfil-list'
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer


class PerfilDetalhe(APIView):
    def get_object(self, id):
        return Perfil.objects.filter(id=id)

    def get(self, request, id, format=None):
        perfil = self.get_object(id)
        serializer = PerfilSerializer(perfil, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PerfilSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id, format=None):
        post = self.get_object(id)
        serializer = PerfilSerializer(post, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class ApiRoot(generics.GenericAPIView):
#     name = 'api-root'
#
#     def get(self, request, *args, **kwargs):
#         return Response({
#             'perfil': reverse(PerfilList.name, request=request),
#             'pessoafisica': reverse(PessoaFisicaList.name, request=request),
#             'usuarios': reverse(UsuarioList.name, request=request)
#         })
