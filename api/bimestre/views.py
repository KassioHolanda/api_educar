from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status, permissions
from rest_framework import filters, viewsets

from bimestre.models import Bimestre
from bimestre.serializer import BimestreSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
from rest_framework import generics


class BimestreList(generics.ListCreateAPIView):
    name = 'bimestre-lista'
    queryset = Bimestre.objects.all()
    serializer_class = BimestreSerializer


class BimestreDetalhe(generics.RetrieveUpdateDestroyAPIView):
    name = 'bimestre-detail'
    queryset = Bimestre.objects.all()
    serializer_class = BimestreSerializer
