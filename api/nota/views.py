from django.shortcuts import render
from rest_framework import filters, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
from rest_framework import generics
from nota.models import AlunoNotaMes
from nota.serializer import *


class AlunoNotaMesList(generics.ListCreateAPIView):
    name = 'alunonotames-list'
    queryset = AlunoNotaMes.objects.select_related('bimestre', 'disciplinaaluno', 'anoletivo', 'matricula', 'unidade',
                                                   'disciplina', 'usuario').all()
    serializer_class = AlunoNotaMesSerializerPost


class AlunoNotaMesDetalhe(generics.RetrieveUpdateDestroyAPIView):
    name = 'alunonotames-detail'
    queryset = AlunoNotaMes.objects.all()
    serializer_class = AlunoNotaMesSerializerPost


class AlunoNotaMesDetalheMatricula(APIView):
    def get_object(self, matricula):
        return AlunoNotaMes.objects.filter(matricula=matricula)

    def get(self, request, matricula, format=None):
        anm = self.get_object(matricula)
        serializer = AlunoNotaMesSerializer(anm, many=True)
        return Response(serializer.data)
