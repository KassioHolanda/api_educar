from django.shortcuts import render
from rest_framework import filters, viewsets

from nota.models import AlunoNotaMes
from nota.serializer import AlunoNotaMesSerializer


class AlunoNotaMesViewSet(viewsets.ModelViewSet):
    name = 'alunonotames'
    queryset = AlunoNotaMes.objects.all()
    serializer_class = AlunoNotaMesSerializer
