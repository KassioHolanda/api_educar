from rest_framework.reverse import reverse
from rest_framework.response import Response
from pessoa.views import *
from unidade.views import *
from ocorrencia.views import *
from rest_framework import generics
from nota.views import *
from funcionario.views import *
from bimestre.views import *
from grade.views import *
from aluno.views import *


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            # 'MatriculaSerializacaoAlunoFrequenciaMesEAlunoNotaMes' : reverse(PessoaFisicaCPFMostrarTodasAsClassesSerializadas.name, request=request),
            'Aluno': reverse(AlunoList.name, request=request),
            'Aluno Frequencia Mes': reverse(AlunoFrequenciaMesList.name, request=request),
            'Aluno Nota Mes': reverse(AlunoNotaMesList.name, request=request),
            'Ano Letivo': reverse(AnoLetivoList.name, request=request),
            'Bimestre': reverse(BimestreList.name, request=request),
            'Cargo': reverse(CargoList.name, request=request),
            'Disciplina': reverse(DisciplinaList.name, request=request),
            'Disciplina Aluno': reverse(DisciplinaAlunoList.name, request=request),
            'Fechamento Unidade': reverse(FechamentoUnidadeList.name, request=request),
            'Funcionario': reverse(FuncionarioList.name, request=request),
            'Funcionario Escola': reverse(FuncionarioEscolaLista.name, request=request),
            'Grade Curso': reverse(GradeCursolist.name, request=request),
            'Local Escola': reverse(LocalEscolaList.name, request=request),
            'Matricula': reverse(MatriculaList.name, request=request),
            'Ocorrencia': reverse(OcorrenciaList.name, request=request),
            'Perfil': reverse(PerfilList.name, request=request),
            'Pessoa Fisica': reverse(PessoaFisicaList.name, request=request),
            'Serie': reverse(SerieList.name, request=request),
            'Serie Disciplina': reverse(SerieDisciplinaList.name, request=request),
            'Serie Turma': reverse(SerieTurmaList.name, request=request),
            'Situacao Turma Mes': reverse(SituacaoTurmaMesList.name, request=request),
            'Tipo Ocorrencia': reverse(TipoOcorrenciaList.name, request=request),
            'Turma': reverse(TurmaViewLis.name, request=request),
            'Unidade': reverse(UnidadeList.name, request=request),
            'Usuarios': reverse(UsuarioList.name, request=request),
        })
