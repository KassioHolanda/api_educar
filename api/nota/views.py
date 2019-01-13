from django.shortcuts import render
from rest_framework import filters, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
from rest_framework import generics
from nota.models import AlunoNotaMes
from nota.serializer import AlunoNotaMesSerializer


class AlunoNotaMesList(generics.ListCreateAPIView):
    name = 'alunonotames-list'
    queryset = AlunoNotaMes.objects.all()
    serializer_class = AlunoNotaMesSerializer


class AlunoNotaMesDetalhe(generics.RetrieveUpdateDestroyAPIView):
    name = 'alunonotames-detalhe'
    queryset = AlunoNotaMes.objects.all()
    serializer_class = AlunoNotaMesSerializer
