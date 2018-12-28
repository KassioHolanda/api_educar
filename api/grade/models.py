from django.db import models


# Create your models here.
class Disciplina(models.Model):
    descricao = models.CharField('descricao', max_length=255, null=True)
    codigo = models.IntegerField('codigo')

    class Meta:
        managed = False
        db_table = 'disciplina'
        ordering = ('id',)



class GradeCurso(models.Model):
    professor = models.ForeignKey('funcionario.Funcionario', on_delete=models.CASCADE,
                                  related_name='%(app_label)s_%(class)s_related', db_column='professor_id')
    seriedisciplina = models.ForeignKey('SerieDisciplina', on_delete=models.CASCADE,
                                        related_name='%(app_label)s_%(class)s_related', db_column='seriedisciplina_id')
    turma = models.ForeignKey('unidade.Turma', on_delete=models.CASCADE, related_name='%(app_label)s_%(class)s_related',
                              db_column='turma_id')
    disciplina = models.ForeignKey('Disciplina', on_delete=models.CASCADE,
                                   related_name='%(app_label)s_%(class)s_related', db_column='disciplina_id')

    class Meta:
        managed = False
        db_table = 'gradecurso'
        ordering = ('id',)


class AnoLetivo(models.Model):
    descricao = models.CharField('descricao', max_length=255)
    datafinal = models.DateField('datafinal')
    datainicio = models.DateField('datainicio')
    fechadonota = models.BooleanField('fechadonota')

    def __str__(self):
        return self.descricao

    class Meta:
        managed = False
        db_table = 'anoletivo'
        ordering = ('id',)


class DisciplinaAluno(models.Model):
    cargahoraria = models.IntegerField()
    statusdisciplinaaluno = models.CharField(max_length=255)
    statusatual = models.CharField(max_length=255)
    matricula = models.ForeignKey('aluno.Matricula', on_delete=models.CASCADE,
                                  related_name='%(app_label)s_%(class)s_related', db_column='matricula_id')
    seriedisciplina = models.ForeignKey('grade.SerieDisciplina', on_delete=models.CASCADE,
                                        related_name='%(app_label)s_%(class)s_related', db_column='seriedisciplina_id')
    mediaacumulada = models.DecimalField(max_digits=5, decimal_places=2)
    mesesfechadosnota = models.IntegerField()
    notaacumulada = models.DecimalField(max_digits=5, decimal_places=2)
    datacadastroprovafinal = models.DateTimeField()
    notaprovafinal = models.DecimalField(max_digits=5, decimal_places=2)
    fechadoprovafinal = models.BooleanField()
    datacadastroatualizacaoprovafinal = models.DateTimeField()
    notaantigaprovafinal = models.DecimalField(max_digits=5, decimal_places=2)

    usuarioatualizacaoprovafinal = models.ForeignKey('pessoa.Usuario', on_delete=models.CASCADE,
                                                     related_name='%(app_label)s_%(class)s_related',
                                                     db_column='usuarioatualizacaoprovafinal_id')

    class Meta:
        managed = False
        db_table = 'disciplinaaluno'
        ordering = ('id',)


class SerieDisciplina(models.Model):
    disciplina = models.ForeignKey('grade.Disciplina', on_delete=models.CASCADE,
                                   related_name='%(app_label)s_%(class)s_related', db_column='disciplina_id')
    serie = models.ForeignKey('unidade.Serie', on_delete=models.CASCADE, related_name='%(app_label)s_%(class)s_related',
                              db_column='serie_id')

    class Meta:
        managed = False
        db_table = 'seriedisciplina'
        ordering = ('id',)


class SituacaoTurmaMes(models.Model):
    datahora = models.DateTimeField()
    status = models.CharField(max_length=255)
    turma = models.ForeignKey('unidade.Turma', on_delete=models.CASCADE,
                              related_name='%(app_label)s_%(class)s_related',
                              db_column='turma_id')
    quantidadeaproados = models.IntegerField()
    quantidadereprovados = models.IntegerField()
    bimestre = models.ForeignKey('bimestre.Bimestre', on_delete=models.CASCADE,
                                 related_name='%(app_label)s_%(class)s_related',
                                 db_column='bimestre_id')

    class Meta:
        managed = False
        db_table = 'situacaoturmames'
        ordering = ('id',)
