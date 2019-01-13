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
    path('pessoafisica/cpf=<path:cpf>/', PessoaFisicaCPF.as_view(), name='pessoafisica-detail'),
    path('pessoafisica/id=<int:pk>/', PessoaFisicaDetalhe.as_view(), name='pessoafisica-detail'),

    path('usuario/', UsuarioList.as_view(), name=UsuarioList.name),
    path('usuario/pessoafisica=<int:pessoafisica>/', UsuarioPessoaFisica.as_view(), name='usuario-pessoafisica-detail'),
    path('usuario/id=<int:pk>/', UsuarioDetalhe.as_view(), name='usuario-detail-id'),
    path('usuario/perfil=<int:perfil>/', UsuarioPerfil.as_view(), name='usuario-detail-perfil'),


    path('perfil/', PerfilList.as_view(), name=PerfilList.name),
    path('perfil/id=<int:pk>/', PerfilDetalhe.as_view(), name='perfil-id-detail'),

    path('unidade/', UnidadeList.as_view(), name=UnidadeList.name),
    path('unidade/id=<int:pk>/', UnidadeDetalhe.as_view(), name='unidade-id-detail'),

    path('localescola/', LocalEscolaList.as_view(), name=LocalEscolaList.name),
    path('localescola/id=<int:pk>/', LocalEscolaDetalhe.as_view(), name='unidade-id-detail'),
    path('localescola/unidade=<int:unidade>/', LocalEscolaUnidade.as_view(), name='localescola-detail-unidade'),

    path('turma/', TurmaViewLis.as_view(), name=TurmaViewLis.name),
    path('turma/id=<int:pk>/', TurmaDetalhe.as_view(), name='turma-detalhe-id'),
    path('turma/sala=<int:sala>/', TurmaSala.as_view(), name='turma-detalhe-sala'),
    path('turma/serie=<int:serie>/', TurmaSerie.as_view(), name='turma-detalhe-serie'),

    path('serie/', SerieList.as_view(), name=SerieList.name),
    path('serie/id=<int:pk>/', SerieDetalhe.as_view(), name='serie-detalhe-id'),

    path('serieturma/', SerieTurmaList.as_view(), name=SerieTurmaList.name),
    path('serieturma/id=<int:pk>/', SerieTurmaDetalhe.as_view(), name='serieturma-detalhe-id'),
    path('serieturma/serie=<int:serie>/', SerieTurmaSerie.as_view(), name='serieturma-detalhe-serie'),
    path('serieturma/turma=<int:turma>/', SerieTurmaTurma.as_view(), name='serieturma-detalhe-turma'),
    path('serieturma/turma=<int:turma>/serie=<int:serie>', SerieTurmaSerieTurma.as_view(),
         name='serieturma-detalhe-turma'),

    path('tipoocorrencia/', TipoOcorrenciaList.as_view(), name=TipoOcorrenciaList.name),
    path('tipoocorrencia/id=<int:pk>/', TipoOcorrenciaDetalhe.as_view(), name='tipoocorrencia-detalhe-id'),

    path('ocorrencia/', OcorrenciaList.as_view(), name=OcorrenciaList.name),
    path('ocorrencia/id=<int:pk>/', OcorrenciaDetalhe.as_view(), name='ocorrencia-detalhe-id'),

    path('alunonotames/', AlunoNotaMesList.as_view(), name=AlunoNotaMesList.name),
    path('alunonotames/id=<int:pk>/', AlunoNotaMesDetalhe.as_view(), name=AlunoNotaMesDetalhe.name),

    path('disciplina/', DisciplinaList.as_view(), name=DisciplinaList.name),
    path('disciplina/id=<int:pk>/', DisciplinaDetalhe.as_view(), name=DisciplinaDetalhe.name),

    path('gradecurso/', GradeCursolist.as_view(), name=GradeCursolist.name),
    path('gradecurso/id=<int:pk>/', GradeCursoDetalhe.as_view(), name=GradeCursoDetalhe.name),
    path('gradecurso/professor=<int:professor>/', GradeCursoProfessor.as_view(), name='gradecurso-detalhe-professor'),
    # path('gradecurso/professor=<int:professor>/turma=<int:turma>/', GradeCursoProfessorTurma.as_view(), name='gradecurso-detalhe-professor'),

    path('seriedisciplina/', SerieDisciplinaList.as_view(), name=SerieDisciplinaList.name),
    path('seriedisciplina/id=<int:pk>/', SerieDisciplinaDetalhe.as_view(), name=SerieDisciplinaDetalhe.name),
    path('seriedisciplina/serie=<int:serie>/', SerieDisciplinaSerie.as_view(), name='seriedisciplina-detalhe-serie'),

    path('anoletivo/', AnoLetivoList.as_view(), name=AnoLetivoList.name),
    path('anoletivo/id=<int:pk>/', AnoLetivoDetalhe.as_view(), name=AnoLetivoDetalhe.name),

    path('situacaoturmames/', SituacaoTurmaMesList.as_view(), name=SituacaoTurmaMesList.name),
    path('situacaoturmames/id=<int:pk>/', SituacaoTurmaMesDetalhe.as_view(), name=SituacaoTurmaMesDetalhe.name),

    path('disciplinaaluno/', DisciplinaAlunoList.as_view(), name=DisciplinaAlunoList.name),
    path('disciplinaaluno/id=<int:pk>/', DisciplinaAlunoDetalhe.as_view(), name=DisciplinaAlunoDetalhe.name),

    path('funcionario/', FuncionarioList.as_view(), name=FuncionarioList.name),
    path('funcionario/id=<int:pk>/', FuncionarioDetail.as_view(), name=FuncionarioDetail.name),
    path('funcionario/pessoafisica=<int:pessoafisica>/', FuncionarioPessoaFisica.as_view(), name='funcionario-detalhe-pessoafisica'),

    path('cargo/', CargoList.as_view(), name=CargoList.name),
    path('cargo/id=<int:pk>/', CargoDetalhe.as_view(), name=CargoDetalhe.name),
    #
    path('funcionarioescola/', FuncionarioEscolaLista.as_view(), name=FuncionarioEscolaLista.name),
    path('funcionarioescola/id=<int:pk>/', FuncionarioEscolaDetalhe.as_view(), name=FuncionarioEscolaDetalhe.name),
    path('funcionarioescola/funcionario=<int:funcionario>/', FuncionarioEscolaFuncionario.as_view(),
         name='funcionarioescola-detalhe-funcionario'),

    path('bimestre/', BimestreList.as_view(), name=BimestreList.name),
    path('bimestre/id=<int:pk>/', BimestreDetalhe.as_view(), name=BimestreDetalhe.name),

    path('aluno/', AlunoList.as_view(), name=AlunoList.name),
    path('aluno/id=<int:pk>/', AlunoDetail.as_view(), name=AlunoDetail.name),

    path('matricula/', MatriculaList.as_view(), name=MatriculaList.name),
    path('matricula/id=<int:pk>/', MatriculaDetalhe.as_view(), name=MatriculaDetalhe.name),
    path('matricula/turma=<int:turma>/', MatriculaTurma.as_view(), name='matricula-detalhe-turma'),

    path('alunofrequenciames/', AlunoFrequenciaMesList.as_view(), name=AlunoFrequenciaMesList.name),
    path('alunofrequenciames/id=<int:pk>/', AlunoFrequenciaMesDetail.as_view(), name=AlunoFrequenciaMesDetail.name),

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
