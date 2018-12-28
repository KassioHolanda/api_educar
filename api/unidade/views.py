from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework import filters, viewsets
from unidade.models import Unidade, LocalEscola, Turma, Serie, SerieTurma
from unidade.serializer import UnidadeSerializer, LocalEscolaSerializer, TurmaSerializer, SerieSerializer, \
    SerieTurmaSerializer


class UnidadeViewSet(viewsets.ModelViewSet):
    queryset = Unidade.objects.all()
    serializer_class = UnidadeSerializer
    name = 'unidade'


class LocalEscolaViewSet(viewsets.ModelViewSet):
    queryset = LocalEscola.objects.all()
    serializer_class = LocalEscolaSerializer
    name = 'localescola'


class TurmaViewSet(viewsets.ModelViewSet):
    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer
    name = 'turma'


class SerieViewSet(viewsets.ModelViewSet):
    queryset = Serie.objects.all()
    serializer_class = SerieSerializer
    name = 'serie'


class SerieTurmaViewSet(viewsets.ModelViewSet):
    queryset = SerieTurma.objects.all()
    serializer_class = SerieTurmaSerializer
    name = 'serieturma'

