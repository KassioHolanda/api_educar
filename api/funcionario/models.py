from django.db import models

from grade.models import *


class Funcionario(models.Model):
    pessoafisica = models.ForeignKey('pessoa.PessoaFisica', null=False, on_delete=models.CASCADE,
                                     related_name='%(app_label)s_%(class)s_related', db_column='pessoafisica_id')
    escolaridade = models.CharField('escolaridade', max_length=255, null=True)
    cargo = models.ForeignKey('Cargo', null=True, on_delete=models.CASCADE,
                              related_name='%(app_label)s_%(class)s_related', db_column='cargo_id')
    cargahoraria = models.CharField('cargahoraria', max_length=255, null=True)
    situacaofuncional = models.CharField('situacaofuncional', max_length=255, null=True)
    dataadmissao = models.DateField('dataadmissao')
    statusfuncionario = models.CharField('statusfuncionario', max_length=255, null=True)

    def __str__(self):
        return self.pessoafisica.nome

    @property
    def funcionario_escolas(self):
        return FuncionarioEscola.objects.filter(funcionario=self)

    @property
    def grade_curso(self):
        return GradeCurso.objects.filter(professor=self)

    class Meta:
        managed = False
        db_table = 'funcionario'
        ordering = ('id',)


class Cargo(models.Model):
    abreviacao = models.CharField('abreviacacao', max_length=255, null=True)
    descricao = models.CharField('descricao', max_length=255, null=True)

    def __str__(self):
        return self.descricao

    class Meta:
        managed = False
        db_table = 'cargo'
        ordering = ('id',)


class FuncionarioEscola(models.Model):
    ativo = models.BooleanField('ativo', null=False)
    unidade = models.ForeignKey('unidade.Unidade', on_delete=models.CASCADE,
                                related_name='%(app_label)s_%(class)s_related', db_column='unidade_id')
    funcionario = models.ForeignKey('Funcionario', on_delete=models.CASCADE,
                                    related_name='%(app_label)s_%(class)s_related', db_column='funcionario_id')

    @property
    def grade_curso(self):
        return GradeCurso.objects.filter(professor=self.funcionario)

    def __str__(self):
        return self.unidade.nome + ' - ' + self.funcionario.pessoafisica.nome

    class Meta:
        managed = False
        db_table = 'funcionarioescola'
        ordering = ('id',)
