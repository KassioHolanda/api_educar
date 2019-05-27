from django.shortcuts import render
from rest_framework import filters, viewsets

# Create your views here.
from aluno.models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
from rest_framework import generics
from aluno.serializer import *


class AlunoList(generics.ListCreateAPIView):
    name = 'aluno-list'
    queryset = Aluno.objects.select_related('pessoafisica').all()
    serializer_class = AlunoSerializer


class AlunoDetail(generics.RetrieveUpdateDestroyAPIView):
    name = 'aluno-detail'
    queryset = Aluno.objects.select_related('pessoafisica').all()
    serializer_class = AlunoSerializer


class MatriculaList(generics.ListCreateAPIView):
    name = 'matricula-list'
    # recuperando apenas usuarios com matricula em andamento
    queryset = Matricula.objects.select_related('turma', 'aluno', 'serie').filter(statusmatricula='EM_ANDAMENTO')
    serializer_class = MatriculaSerializer


class MatriculaDetalhe(generics.RetrieveUpdateDestroyAPIView):
    name = 'matricula-detail'
    queryset = Matricula.objects.select_related('turma', 'aluno', 'serie').all()
    serializer_class = MatriculaSerializer


class MatriculaSerializarCompleta(generics.RetrieveAPIView):
    name = 'matricula-detail'
    queryset = Matricula.objects.select_related('turma', 'aluno', 'serie').all()
    serializer_class = MatriculaSerializacaoAlunoFrequenciaMesEAlunoNotaMes


class MatriculaTurma(APIView):
    def get_object(self, turma):
        return Matricula.objects.select_related('turma', 'aluno', 'serie').filter(turma=turma)

    def get(self, request, turma, format=None):
        matricula = self.get_object(turma)
        serializer = MatriculaSerializer(matricula, many=True)
        return Response(serializer.data)


class AlunoFrequenciaMesList(generics.ListCreateAPIView):
    name = 'alunofrequenciames-list'
    queryset = AlunoFrequenciaMes.objects.select_related('matricula', 'bimestre', 'disciplina', 'disciplinaaluno').all()
    serializer_class = AlunoFrequenciaMesSerializerPost


class AlunoFrequenciaMesDetail(generics.RetrieveUpdateDestroyAPIView):
    name = 'alunofrequenciames-detail'
    queryset = AlunoFrequenciaMes.objects.select_related('matricula', 'bimestre', 'disciplina', 'disciplinaaluno').all()
    serializer_class = AlunoFrequenciaMesSerializerPost


class AlunoFrequenciaMesMatricula(APIView):
    def get_object(self, matricula):
        return AlunoFrequenciaMes.objects.select_related('matricula', 'bimestre', 'disciplina',
                                                         'disciplinaaluno').filter(matricula=matricula)

    def get(self, request, matricula, format=None):
        alnofrequencia = self.get_object(matricula)
        serializer = AlunoFrequenciaMesSerializer(alnofrequencia, many=True)
        return Response(serializer.data)

# generics.ListCreateAPIView
# generics.RetrieveUpdateDestroyAPIView
