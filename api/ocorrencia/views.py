from django.shortcuts import render
from rest_framework import filters, viewsets
from ocorrencia.models import *
from ocorrencia.serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
from rest_framework import generics


# Create your views here.

class TipoOcorrenciaList(generics.ListCreateAPIView):
    name = 'tipoocorrencia-list'
    queryset = TipoOcorrencia.objects.all()
    serializer_class = TipoOcorrenciaSerializer


class TipoOcorrenciaDetalhe(generics.RetrieveUpdateDestroyAPIView):
    name = 'tipoocorrencia-detail'
    queryset = TipoOcorrencia.objects.all()
    serializer_class = TipoOcorrenciaSerializer


class OcorrenciaList(generics.ListCreateAPIView):
    name = 'ocorrencia-list'
    queryset = Ocorrencia.objects.all()
    serializer_class = OcorrenciaSerializer


class OcorrenciaDetalhe(generics.RetrieveUpdateDestroyAPIView):
    name = 'ocorrencia-detail'
    queryset = Ocorrencia.objects.all()
    serializer_class = OcorrenciaSerializer


class OcorrenciaDetalheAluno(APIView):
    def get_object(self, aluno):
        return Ocorrencia.objects.filter(aluno=aluno)

    def get(self, request, aluno, format=None):
        anm = self.get_object(aluno)
        serializer = OcorrenciaSerializer(anm, many=True)
        return Response(serializer.data)
