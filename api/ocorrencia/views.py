from django.shortcuts import render
from rest_framework import filters, viewsets
from ocorrencia.models import *
from ocorrencia.serializer import *


# Create your views here.

class TipoOcorrenciaViewSet(viewsets.ModelViewSet):
    name = 'tipoocorrencia'
    queryset = TipoOcorrencia.objects.all()
    serializer_class = TipoOcorrenciaSerializer


class OcorrenciaViewSet(viewsets.ModelViewSet):
    name = 'ocorrencia'
    queryset = Ocorrencia.objects.all()
    serializer_class = OcorrenciaSerializer
