from django.shortcuts import render
from rest_framework import filters, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
from rest_framework import generics
# Create your views here.
from grade.models import GradeCurso, Disciplina, SerieDisciplina, AnoLetivo, DisciplinaAluno, SituacaoTurmaMes
from grade.serializer import GradeCursoSerializer, DisciplinaSerializer, SerieDisciplinaSerializer, AnoLetivoSerializer, \
    DisciplinaAlunoSerializer, SituacaoTurmaMesSerializer


class DisciplinaDetalhe(generics.RetrieveUpdateDestroyAPIView):
    name = 'disciplina-detail'
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer


class DisciplinaList(generics.ListCreateAPIView):
    name = 'disciplina-list'
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer


class GradeCursolist(generics.ListCreateAPIView):
    name = 'gradecurso-list'
    queryset = GradeCurso.objects.all()
    serializer_class = GradeCursoSerializer


class GradeCursoProfessor(APIView):
    def get_object(self, professor):
        return GradeCurso.objects.filter(professor=professor)

    def get(self, request, professor, format=None):
        grade = self.get_object(professor)
        serializer = GradeCursoSerializer(grade, many=True)
        return Response(serializer.data)


class GradeCursoProfessorTurma(APIView):
    def get_object(self, professor, turma):
        return GradeCurso.objects.filter(professor=professor, turma=turma)

    def get(self, request, professor, turma, format=None):
        grade = self.get_object(professor, turma)
        serializer = GradeCursoSerializer(grade, many=True)
        return Response(serializer.data)


class GradeCursoDetalhe(generics.RetrieveUpdateDestroyAPIView):
    name = 'gradecurso-detail'
    queryset = GradeCurso.objects.all()
    serializer_class = GradeCursoSerializer


class SerieDisciplinaList(generics.ListCreateAPIView):
    queryset = SerieDisciplina.objects.all()
    serializer_class = SerieDisciplinaSerializer
    name = 'seriedisciplina-list'


class SerieDisciplinaSerie(APIView):
    def get_object(self, serie):
        return SerieDisciplina.objects.filter(serie=serie)

    def get(self, request, serie, format=None):
        serie = self.get_object(serie)
        serializer = SerieDisciplinaSerializer(serie, many=True)
        return Response(serializer.data)


class SerieDisciplinaDisciplina(APIView):
    def get_object(self, disciplina):
        return SerieDisciplina.objects.filter(disciplina=disciplina)

    def get(self, request, disciplina, format=None):
        sd = self.get_object(disciplina)
        serializer = SerieDisciplinaSerializer(sd, many=True)
        return Response(serializer.data)


class DisciplinaAlunoMatriculaDetalhe(APIView):
    def get_object(self, matricula):
        return DisciplinaAluno.objects.filter(matricula=matricula)

    def get(self, request, matricula, format=None):
        da = self.get_object(matricula)
        serializer = DisciplinaAlunoSerializer(da, many=True)
        return Response(serializer.data)


class SerieDisciplinaDetalhe(generics.RetrieveUpdateDestroyAPIView):
    queryset = SerieDisciplina.objects.all()
    serializer_class = SerieDisciplinaSerializer
    name = 'seriedisciplina-detail'


class AnoLetivoList(generics.ListCreateAPIView):
    queryset = AnoLetivo.objects.all()
    serializer_class = AnoLetivoSerializer
    name = 'anoletivo-list'


class AnoLetivoDetalhe(generics.RetrieveUpdateDestroyAPIView):
    queryset = AnoLetivo.objects.all()
    serializer_class = AnoLetivoSerializer
    name = 'anoletivo-detail'


class DisciplinaAlunoList(generics.ListCreateAPIView):
    queryset = DisciplinaAluno.objects.all()
    serializer_class = DisciplinaAlunoSerializer
    name = 'disciplinaaluno-list'


class DisciplinaAlunoDetalhe(generics.RetrieveUpdateDestroyAPIView):
    queryset = DisciplinaAluno.objects.all()
    serializer_class = DisciplinaAlunoSerializer
    name = 'disciplinaaluno-detail'


class SituacaoTurmaMesList(generics.ListCreateAPIView):
    queryset = SituacaoTurmaMes.objects.all()
    serializer_class = SituacaoTurmaMesSerializer
    name = 'situacaoturmames-list'


class SituacaoTurmaMesDetalhe(generics.RetrieveUpdateDestroyAPIView):
    queryset = SituacaoTurmaMes.objects.all()
    serializer_class = SituacaoTurmaMesSerializer
    name = 'situacaoturmames-detail'


class SituacaoTurmaMesTurma(APIView):
    def get_object(self, turma):
        return SituacaoTurmaMes.objects.filter(turma=turma)

    def get(self, request, turma, format=None):
        da = self.get_object(turma)
        serializer = SituacaoTurmaMesSerializer(da, many=True)
        return Response(serializer.data)
