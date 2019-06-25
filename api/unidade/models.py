from django.db import models

# Create your models here.
from aluno.models import Matricula
from grade.models import GradeCurso, SituacaoTurmaMes


class Unidade(models.Model):
    abreviacao = models.CharField('abreviacao', max_length=255)
    cnpj = models.CharField('cnpj', max_length=255)
    nome = models.CharField('nome', max_length=255)

    @property
    def locais_escola(self):
        return LocalEscola.objects.filter(unidade=self)

    @property
    def fechamento_unidade(self):
        return FechamentoUnidade.objects.filter(unidade=self)

    def __str__(self):
        return self.nome

    class Meta:
        managed = False
        db_table = 'unidade'
        ordering = ('id',)


class LocalEscola(models.Model):
    descricao = models.CharField('descricao', max_length=255)
    unidade = models.ForeignKey('Unidade', on_delete=models.CASCADE,
                                related_name='%(app_label)s_%(class)s_related', db_column='unidade_id')

    @property
    def turmas(self):
        return Turma.objects.filter(sala=self, statusturma='CADASTRADA')

    class Meta:
        managed = False
        db_table = 'localescola'
        ordering = ('id',)


class Turma(models.Model):
    descricao = models.CharField('descricao', max_length=255)
    turno = models.CharField('turno', max_length=255)
    sala = models.ForeignKey('LocalEscola', on_delete=models.CASCADE, related_name='%(app_label)s_%(class)s_related',
                             db_column='sala_id')
    anoletivo = models.ForeignKey('grade.AnoLetivo', on_delete=models.CASCADE,
                                  related_name='%(app_label)s_%(class)s_related',
                                  db_column='anoletivo_id')
    serie = models.ForeignKey('Serie', on_delete=models.CASCADE, related_name='%(app_label)s_%(class)s_related',
                              db_column='serie_id')
    nivel = models.CharField('nivel', max_length=255)
    statusturma = models.CharField(max_length=255)

    def matriculas(self):
        return Matricula.objects.select_related('turma').filter(turma=self, statusatual='EM_ANDAMENTO')

    def grade_curso(self):
        return GradeCurso.objects.filter(turma=self)

    def situacao_turma_mes(self):
        return SituacaoTurmaMes.objects.select_related('turma').filter(turma=self)

    def __str__(self):
        return self.descricao

    class Meta:
        managed = False
        db_table = 'turma'
        ordering = ('id',)


class Serie(models.Model):
    descricao = models.CharField('descricao', max_length=255)
    nivel = models.CharField('nivel', max_length=255)

    def __str__(self):
        return self.descricao

    class Meta:
        managed = False
        db_table = 'serie'
        ordering = ('id',)


class SerieTurma(models.Model):
    serie = models.ForeignKey('Serie', on_delete=models.CASCADE, related_name='%(app_label)s_%(class)s_related',
                              db_column='serie_id')
    turma = models.ForeignKey('Turma', on_delete=models.CASCADE, related_name='%(app_label)s_%(class)s_related',
                              db_column='turma_id')

    class Meta:
        managed = False
        db_table = 'serieturma'
        ordering = ('id',)


class FechamentoUnidade(models.Model):
    dataalteracao = models.DateTimeField()
    datacadastro = models.DateTimeField()
    anoletivo = models.ForeignKey('grade.AnoLetivo', on_delete=models.CASCADE,
                                  related_name='%(app_label)s_%(class)s_related', db_column='anoletivo_id')
    unidade = models.ForeignKey('Unidade', on_delete=models.CASCADE, related_name='%(app_label)s_%(class)s_related',
                                db_column='unidade_id')

    # usuarioalteracao = models.ForeignKey('pessoa.Usuario', on_delete=models.CASCADE, related_name='%(app_label)s_%(class)s_related', db_column='usuarioalteracao_id')
    # usuariocadastro = models.ForeignKey('pessoa.Usuario', on_delete=models.CASCADE, related_name='%(app_label)s_%(class)s_related', db_column='usuariocadastro_id')

    class Meta:
        managed = False
        db_table = 'fechamentounidade'
        ordering = ('id',)
