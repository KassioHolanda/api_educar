from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status, permissions
from rest_framework import filters, viewsets

from bimestre.models import Bimestre
from bimestre.serializer import BimestreSerializer


class BimestreViewSet(viewsets.ModelViewSet):
    name = 'bimestre'
    queryset = Bimestre.objects.all()
    serializer_class = BimestreSerializer

