from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
from rest_framework import generics
from rest_framework import filters, viewsets
from unidade.models import Unidade, LocalEscola, Turma, Serie, SerieTurma
from unidade.serializer import UnidadeSerializer, LocalEscolaSerializer, TurmaSerializer, SerieSerializer, \
    SerieTurmaSerializer


class UnidadeList(generics.ListAPIView):
    queryset = Unidade.objects.all()
    serializer_class = UnidadeSerializer
    name = 'unidade-list'


class UnidadeDetalhe(APIView):
    def get_object(self, id):
        return Unidade.objects.filter(id=id)

    def get(self, request, id, format=None):
        unidade = self.get_object(id)
        serializer = UnidadeSerializer(unidade, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UnidadeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id, format=None):
        post = self.get_object(id)
        serializer = UnidadeSerializer(post, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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


class LocalEscolaDetalhe(APIView):
    def get_object(self, id):
        return LocalEscola.objects.filter(id=id)

    def get(self, request, id, format=None):
        localescola = self.get_object(id)
        serializer = LocalEscolaSerializer(localescola, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = LocalEscolaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id, format=None):
        post = self.get_object(id)
        serializer = LocalEscolaSerializer(post, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TurmaViewLis(generics.ListAPIView):
    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer
    name = 'turma-list'


class TurmaSala(APIView):
    def get_object(self, sala):
        return Turma.objects.filter(sala=sala)

    def get(self, request, sala, format=None):
        turma = self.get_object(sala)
        serializer = TurmaSerializer(turma, many=True)
        return Response(serializer.data)


class TurmaDetalhe(APIView):
    def get_object(self, id):
        return Turma.objects.filter(id=id)

    def get(self, request, id, format=None):
        turma = self.get_object(id)
        serializer = TurmaSerializer(turma, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TurmaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id, format=None):
        post = self.get_object(id)
        serializer = TurmaSerializer(post, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TurmaSerie(APIView):
    def get_object(self, serie):
        return Turma.objects.filter(serie=serie)

    def get(self, request, serie, format=None):
        turma = self.get_object(serie)
        serializer = TurmaSerializer(turma, many=True)
        return Response(serializer.data)


class SerieList(generics.ListAPIView):
    queryset = Serie.objects.all()
    serializer_class = SerieSerializer
    name = 'serie-list'


class SerieDetalhe(APIView):
    def get_object(self, id):
        return Serie.objects.filter(id=id)

    def get(self, request, id, format=None):
        serie = self.get_object(id)
        serializer = SerieSerializer(serie, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SerieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id, format=None):
        post = self.get_object(id)
        serializer = SerieSerializer(post, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
    def get_object(self, id):
        return SerieTurma.objects.filter(id=id)

    def get(self, request, id, format=None):
        serie = self.get_object(id)
        serializer = SerieTurmaSerializer(serie, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SerieTurmaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id, format=None):
        post = self.get_object(id)
        serializer = SerieTurmaSerializer(post, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
