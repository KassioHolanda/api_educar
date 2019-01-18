from django.db import models


# Create your models here.
class Unidade(models.Model):
    abreviacao = models.CharField('abreviacao', max_length=255)
    cnpj = models.CharField('cnpj', max_length=255)
    nome = models.CharField('nome', max_length=255)

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
