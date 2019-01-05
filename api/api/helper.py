from rest_framework.reverse import reverse
from rest_framework.response import Response
from pessoa.views import *
from rest_framework import generics


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'perfil': reverse(PerfilList.name, request=request),
            'pessoafisica': reverse(PessoaFisicaList.name, request=request),
            'usuarios': reverse(UsuarioList.name, request=request)
        })
