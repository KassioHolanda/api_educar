from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
from rest_framework import generics
# Create your views here.
from grade.models import *
from grade.serializer import *


class DisciplinaDetalhe(generics.RetrieveAPIView):
    name = 'disciplina-detail'
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer


class DisciplinaList(generics.ListAPIView):
    name = 'disciplina-list'
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer


class GradeCursolist(generics.ListAPIView):
    name = 'gradecurso-list'
    queryset = GradeCurso.objects.select_related('seriedisciplina', 'disciplina', 'turma').all()
    serializer_class = GradeCursoSerializer


class GradeCursoProfessor(APIView):
    def get_object(self, professor):
        return GradeCurso.objects.select_related('professor', 'seriedisciplina', 'turma', 'disciplina').filter(
            professor=professor)

    def get(self, request, professor, format=None):
        grade = self.get_object(professor)
        serializer = GradeCursoSerializer(grade, many=True)
        return Response(serializer.data)


class GradeCursoProfessorTurma(APIView):
    def get_object(self, professor, turma):
        return GradeCurso.objects.select_related('professor', 'seriedisciplina', 'turma', 'disciplina').filter(
            professor=professor, turma=turma)

    def get(self, request, professor, turma, format=None):
        grade = self.get_object(professor, turma)
        serializer_context = {
            'request': request,
        }
        serializer = GradeCursoSerializer(grade, many=True, context=serializer_context)

        return Response(serializer.data)


class GradeCursoDetalhe(generics.RetrieveAPIView):
    name = 'gradecurso-detail'
    queryset = GradeCurso.objects.select_related('professor', 'seriedisciplina', 'turma', 'disciplina').all()
    serializer_class = GradeCursoSerializer


class SerieDisciplinaList(generics.ListAPIView):
    queryset = SerieDisciplina.objects.select_related('serie', 'disciplina').all()
    serializer_class = SerieDisciplinaSerializer
    name = 'seriedisciplina-list'


class SerieDisciplinaSerie(APIView):
    def get_object(self, serie):
        return SerieDisciplina.objects.select_related('serie', 'disciplina').filter(serie=serie)

    def get(self, request, serie, format=None):
        serie = self.get_object(serie)
        serializer_context = {
            'request': request,
        }
        serializer = SerieDisciplinaSerializer(serie, many=True, context=serializer_context)
        return Response(serializer.data)


class SerieDisciplinaDisciplina(APIView):
    def get_object(self, disciplina):
        return SerieDisciplina.objects.select_related('serie', 'disciplina').filter(disciplina=disciplina)

    def get(self, request, disciplina, format=None):
        sd = self.get_object(disciplina)
        serializer_context = {
            'request': request,
        }
        serializer = SerieDisciplinaSerializer(sd, many=True, serializer=serializer_context)
        return Response(serializer.data)


class DisciplinaAlunoMatriculaDetalhe(APIView):
    def get_object(self, matricula):
        return DisciplinaAluno.objects.select_related('matricula', 'seriedisciplina',
                                                      'usuarioatualizacaoprovafinal').filter(matricula=matricula)

    def get(self, request, matricula, format=None):
        da = self.get_object(matricula)
        serializer_context = {
            'request': request,
        }
        serializer = DisciplinaAlunoSerializer(da, many=True, serializer=serializer_context)
        return Response(serializer.data)


class SerieDisciplinaDetalhe(generics.RetrieveAPIView):
    queryset = SerieDisciplina.objects.select_related('serie', 'disciplina').all()
    serializer_class = SerieDisciplinaSerializer
    name = 'seriedisciplina-detail'


class AnoLetivoList(generics.ListAPIView):
    queryset = AnoLetivo.objects.all()
    serializer_class = AnoLetivoSerializer
    name = 'anoletivo-list'


class AnoLetivoDetalhe(generics.RetrieveAPIView):
    queryset = AnoLetivo.objects.all()
    serializer_class = AnoLetivoSerializer
    name = 'anoletivo-detail'


class DisciplinaAlunoList(generics.ListAPIView):
    queryset = DisciplinaAluno.objects.select_related('matricula', 'seriedisciplina',
                                                      'usuarioatualizacaoprovafinal').all()
    serializer_class = DisciplinaAlunoSerializerPost
    name = 'disciplinaaluno-list'


class DisciplinaAlunoDetalhe(generics.RetrieveAPIView):
    queryset = DisciplinaAluno.objects.select_related('matricula', 'seriedisciplina',
                                                      'usuarioatualizacaoprovafinal').all()
    serializer_class = DisciplinaAlunoSerializerPost
    name = 'disciplinaaluno-detail'


class SituacaoTurmaMesList(generics.ListCreateAPIView):
    queryset = SituacaoTurmaMes.objects.select_related('turma', 'bimestre').all()

    serializer_class = SituacaoTurmaMesSerializerPost
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('status', 'turma', )

    name = 'situacaoturmames-list'


class SituacaoTurmaMesDetalhe(generics.RetrieveUpdateDestroyAPIView):
    queryset = SituacaoTurmaMes.objects.select_related('turma', 'bimestre').all()
    serializer_class = SituacaoTurmaMesSerializerPost
    name = 'situacaoturmames-detail'


class SituacaoTurmaMesTurma(APIView):
    def get_object(self, turma):
        return SituacaoTurmaMes.objects.select_related('turma', 'bimestre').filter(turma=turma)

    def get(self, request, turma, format=None):
        da = self.get_object(turma)
        serializer_context = {
            'request': request,
        }
        serializer = SituacaoTurmaMesSerializer(da, many=True, serializer=serializer_context)
        return Response(serializer.data)
