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

class TipoOcorrenciaList(generics.ListAPIView):
    name = 'tipoocorrencia-list'
    queryset = TipoOcorrencia.objects.all()
    serializer_class = TipoOcorrenciaSerializer


class TipoOcorrenciaDetalhe(generics.RetrieveUpdateDestroyAPIView):
    name = 'tipoocorrencia-detalhe'
    queryset = TipoOcorrencia.objects.all()
    serializer_class = TipoOcorrenciaSerializer


class OcorrenciaList(generics.ListAPIView):
    name = 'ocorrencia-list'
    queryset = Ocorrencia.objects.all()
    serializer_class = OcorrenciaSerializer


class OcorrenciaDetalhe(generics.RetrieveUpdateDestroyAPIView):
    name = 'ocorrencia-detalhe'
    queryset = Ocorrencia.objects.all()
    serializer_class = OcorrenciaSerializer
