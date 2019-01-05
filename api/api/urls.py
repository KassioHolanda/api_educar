"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from rest_framework.routers import DefaultRouter
from django.urls import path
from django.contrib import admin

from api import helper
from funcionario.views import *
from grade.views import *
from pessoa.views import *
from unidade.views import *
from nota.views import *
from aluno.views import *
from ocorrencia.views import *
from bimestre.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', helper.ApiRoot().as_view()),

    path('pessoafisica/', PessoaFisicaList.as_view(), name=PessoaFisicaList.name),
    path('pessoafisica/cpf=<int:cpf>/', PessoaFisicaCPF.as_view(), name='pessoafisica-id-detail'),
    path('pessoafisica/id=<int:id>/', PessoaFisicaDetalhe.as_view(), name='pessoafisica-cpf-detail'),

    path('usuario/', UsuarioList.as_view(), name=UsuarioList.name),
    path('usuario/pessoafisica=<int:pessoafisica>/', UsuarioPessoaFisica.as_view(), name='usuario-pessoafisica-detail'),
    path('usuario/id=<int:id>/', UsuarioDetalhe.as_view(), name='usuario-detail'),
    path('usuario/perfil=<int:perfil>/', UsuarioPerfil.as_view(), name='usuario-detail-perfil'),

    path('perfil/', PerfilList.as_view(), name=PerfilList.name),
    path('perfil/id=<int:id>/', PerfilDetalhe.as_view(), name='perfil-detail'),

]

# router = DefaultRouter()
#
# # router.register('pessoafisica', PessaFisicaView.as_view(), base_name=PessoaFisicaViewSet.name)
# router.register('funcionario', FuncionarioViewSet, base_name=FuncionarioViewSet.name)
# router.register('cargo', CargoViewSet, base_name=CargoViewSet.name)
# router.register('unidade', UnidadeViewSet, base_name=UnidadeViewSet.name)
# router.register('funcionarioescola', FuncionarioEscolaViewSet, base_name=FuncionarioEscolaViewSet.name)
# router.register('disciplina', DisciplinaViewSet, base_name=DisciplinaViewSet.name)
# router.register('localescola', LocalEscolaViewSet, base_name=LocalEscolaViewSet.name)
# router.register('turma', TurmaViewSet, base_name=TurmaViewSet.name)
# router.register('serie', SerieViewSet, base_name=SerieViewSet.name)
# router.register('seriedisciplina', SerieDisciplinaViewSet, base_name=SerieDisciplinaViewSet.name)
# router.register('anoletivo', AnoLetivoViewSet, base_name=AnoLetivoViewSet.name)
# router.register('gradecurso', GradeCursoViewSet, base_name=GradeCursoViewSet.name)
# router.register('aluno', AlunoViewSet, base_name=AlunoViewSet.name)
# router.register('matricula', MatriculaViewSet, base_name=MatriculaViewSet.name)
# router.register('alunofrequenciames', AlunoFrequenciaMesViewSet, base_name=AlunoFrequenciaMesViewSet.name)
# router.register('tipoocorrencia', TipoOcorrenciaViewSet, base_name=TipoOcorrenciaViewSet.name)
# router.register('ocorrencia', OcorrenciaViewSet, base_name=OcorrenciaViewSet.name)
# router.register('usuario', UsuarioViewSet, base_name=UsuarioViewSet.name)
# router.register('disciplinaluno', DisciplinaAlunoViewSet, base_name=DisciplinaAlunoViewSet.name)
# router.register('alunonotames', AlunoNotaMesViewSet, base_name=AlunoNotaMesViewSet.name)
# router.register('situacaoturmames', SituacaoTurmaMesViewSet, base_name=SituacaoTurmaMesViewSet.name)
# router.register('perfil', PerfilViewSet, base_name=PerfilViewSet.name)
# router.register('bimestre', BimestreViewSet, base_name=BimestreViewSet.name)
# router.register('serieturma', SerieTurmaViewSet, base_name=SerieTurmaViewSet.name)
#
# urlpatterns = router.urls
