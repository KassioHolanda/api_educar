from django.shortcuts import render
from rest_framework import filters, viewsets

# Create your views here.
from aluno.models import *
from aluno.serializer import *


class AlunoViewSet(viewsets.ModelViewSet):
    name = 'aluno'
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


class MatriculaViewSet(viewsets.ModelViewSet):
    name = 'matricula'
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer



class AlunoFrequenciaMesViewSet(viewsets.ModelViewSet):
    name = 'alunofrequenciames'
    queryset = AlunoFrequenciaMes.objects.all()
    serializer_class = AlunoFrequenciaMesSerializer
