from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
from rest_framework import generics
from rest_framework import filters, viewsets
from unidade.models import Unidade, LocalEscola, Turma, Serie, SerieTurma
from unidade.serializer import *


class UnidadeList(generics.ListAPIView):
    queryset = Unidade.objects.all()
    serializer_class = UnidadeSerializer
    name = 'unidade-list'


class UnidadeDetalhe(generics.RetrieveAPIView):
    queryset = Unidade.objects.all()
    serializer_class = UnidadeSerializer
    name = 'unidade-detail'


class LocalEscolaList(generics.ListAPIView):
    queryset = LocalEscola.objects.all()
    serializer_class = LocalEscolaSerializer
    name = 'localescola-list'


class LocalEscolaUnidade(APIView):
    def get_object(self, unidade):
        return LocalEscola.objects.filter(unidade=unidade)

    def get(self, request, unidade, format=None):
        unidade = self.get_object(unidade)
        serializer = LocalEscolaSerializer(unidade, many=True)
        return Response(serializer.data)


class LocalEscolaDetalhe(generics.RetrieveAPIView):
    queryset = LocalEscola.objects.all()
    serializer_class = LocalEscolaSerializer
    name = 'localescola-detail'


class TurmaViewLis(generics.ListAPIView):
    queryset = Turma.objects.filter(statusturma='CADASTRADA')
    serializer_class = TurmaSerializer
    name = 'turma-list'


class TurmaViewListSimples(generics.ListAPIView):
    queryset = Turma.objects.filter(statusturma='CADASTRADA')
    serializer_class = TurmaSerializerSimplificada
    name = 'turma-list'


class TurmaSala(APIView):
    def get_object(self, sala):
        return Turma.objects.filter(sala=sala).filter(statusturma='CADASTRADA').filter(nivel='FUNDAMENTAL')

    def get(self, request, sala, format=None):
        turma = self.get_object(sala)
        serializer = TurmaSerializerSimplificada(turma, many=True)
        return Response(serializer.data)


class TurmaDetalheSerializado(generics.RetrieveAPIView):
    name = 'turma-detail'
    queryset = Turma.objects.filter(statusturma='CADASTRADA')
    serializer_class = TurmaSerializer


class TurmaDetalhe(generics.RetrieveAPIView):
    name = 'turma-detail'
    queryset = Turma.objects.filter(statusturma='CADASTRADA')
    serializer_class = TurmaSerializer


class kkkkTurmaDetalheSerializado(generics.RetrieveAPIView):
    name = 'turma-detail'
    queryset = Turma.objects.filter(statusturma='CADASTRADA')
    serializer_class = TurmaSerializer


class TurmaSerie(APIView):
    def get_object(self, serie):
        return Turma.objects.filter(serie=serie).filter(statusturma='CADASTRADA')

    def get(self, request, serie, format=None):
        turma = self.get_object(serie)
        serializer = TurmaSerializer(turma, many=True)
        return Response(serializer.data)


class SerieList(generics.ListAPIView):
    queryset = Serie.objects.all()
    serializer_class = SerieSerializer
    name = 'serie-list'


class SerieDetalhe(generics.RetrieveAPIView):
    queryset = Serie.objects.all()
    serializer_class = SerieSerializer
    name = 'serie-detail'


class SerieTurmaList(generics.ListAPIView):
    queryset = SerieTurma.objects.all()
    serializer_class = SerieTurmaSerializer
    name = 'serieturma-list'


class SerieTurmaSerie(APIView):
    def get_object(self, serie):
        return SerieTurma.objects.filter(serie=serie)

    def get(self, request, serie, format=None):
        serieturma = self.get_object(serie)
        serializer = SerieTurmaSerializer(serieturma, many=True)
        return Response(serializer.data)


class SerieTurmaTurma(APIView):
    def get_object(self, turma):
        return SerieTurma.objects.filter(turma=turma)

    def get(self, request, turma, format=None):
        serieturma = self.get_object(turma)
        serializer = SerieTurmaSerializer(serieturma, many=True)
        return Response(serializer.data)


class SerieTurmaSerieTurma(APIView):
    def get_object(self, turma, serie):
        return SerieTurma.objects.filter(turma=turma, serie=serie)

    def get(self, request, turma, serie, format=None):
        serieturma = self.get_object(turma, serie)
        serializer = SerieTurmaSerializer(serieturma, many=True)
        return Response(serializer.data)


class SerieTurmaDetalhe(APIView):
    queryset = SerieTurma.objects.all()
    serializer_class = SerieTurmaSerializer
    name = 'serieturma-detail'


class FechamentoUnidadeDetalhe(generics.RetrieveAPIView):
    queryset = FechamentoUnidade.objects.all()
    serializer_class = FechamentoUnidadeSerializer
    name = 'fechamentounidade-detail'


class FechamentoUnidadeList(generics.ListAPIView):
    queryset = FechamentoUnidade.objects.all()
    serializer_class = FechamentoUnidadeSerializer
    name = 'fechamentounidade-list'