from django.shortcuts import render
from rest_framework import filters, viewsets
# Create your views here.
from grade.models import GradeCurso, Disciplina, SerieDisciplina, AnoLetivo, DisciplinaAluno, SituacaoTurmaMes
from grade.serializer import GradeCursoSerializer, DisciplinaSerializer, SerieDisciplinaSerializer, AnoLetivoSerializer, \
    DisciplinaAlunoSerializer, SituacaoTurmaMesSerializer


class DisciplinaViewSet(viewsets.ModelViewSet):
    name = 'disciplina'
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer


class GradeCursoViewSet(viewsets.ModelViewSet):
    name = 'gradecurso'
    queryset = GradeCurso.objects.all()
    serializer_class = GradeCursoSerializer


class SerieDisciplinaViewSet(viewsets.ModelViewSet):
    queryset = SerieDisciplina.objects.all()
    serializer_class = SerieDisciplinaSerializer
    name = 'seriedisciplina'


class AnoLetivoViewSet(viewsets.ModelViewSet):
    queryset = AnoLetivo.objects.all()
    serializer_class = AnoLetivoSerializer
    name = 'anoletivo'


class DisciplinaAlunoViewSet(viewsets.ModelViewSet):
    queryset = DisciplinaAluno.objects.all()
    serializer_class = DisciplinaAlunoSerializer
    name = 'disciplinaaluno'


class SituacaoTurmaMesViewSet(viewsets.ModelViewSet):
    queryset = SituacaoTurmaMes.objects.all()
    serializer_class = SituacaoTurmaMesSerializer
    name = 'situacaoturmames'
