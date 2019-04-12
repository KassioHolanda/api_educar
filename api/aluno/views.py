from django.shortcuts import render
from rest_framework import filters, viewsets

# Create your views here.
from aluno.models import *
from aluno.serializer import *

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
from rest_framework import generics


class AlunoList(generics.ListCreateAPIView):
    name = 'aluno-list'
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


class AlunoDetail(generics.RetrieveUpdateDestroyAPIView):
    name = 'aluno-detail'
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


class MatriculaList(generics.ListCreateAPIView):
    name = 'matricula-list'
    # recuperando apenas usuarios com matricula em andamento
    queryset = Matricula.objects.filter(statusmatricula='EM_ANDAMENTO')
    serializer_class = MatriculaSerializer


class MatriculaDetalhe(generics.RetrieveUpdateDestroyAPIView):
    name = 'matricula-detail'
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer


class MatriculaTurma(APIView):
    def get_object(self, turma):
        return Matricula.objects.filter(turma=turma)

    def get(self, request, turma, format=None):
        matricula = self.get_object(turma)
        serializer = MatriculaSerializer(matricula, many=True)
        return Response(serializer.data)


class AlunoFrequenciaMesList(generics.ListCreateAPIView):
    name = 'alunofrequenciames-list'
    queryset = AlunoFrequenciaMes.objects.all()
    serializer_class = AlunoFrequenciaMesSerializer


class AlunoFrequenciaMesDetail(generics.RetrieveUpdateDestroyAPIView):
    name = 'alunofrequenciames-detail'
    queryset = AlunoFrequenciaMes.objects.all()
    serializer_class = AlunoFrequenciaMesSerializer


class AlunoFrequenciaMesMatricula(APIView):
    def get_object(self, matricula):
        return AlunoFrequenciaMes.objects.filter(matricula=matricula)

    def get(self, request, matricula, format=None):
        alnofrequencia = self.get_object(matricula)
        serializer = AlunoFrequenciaMesSerializer(alnofrequencia, many=True)
        return Response(serializer.data)

# generics.ListCreateAPIView
# generics.RetrieveUpdateDestroyAPIView
