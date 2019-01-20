from django.db import models


# Create your models here.
class Aluno(models.Model):
    pessoafisica = models.ForeignKey('pessoa.PessoaFisica', null=False, on_delete=models.CASCADE,
                                     related_name='%(app_label)s_%(class)s_related', db_column='pessoafisica_id')
    datacadastro = models.DateField('datacadastro', null=False)

    def __str__(self):
        return self.pessoafisica.nome

    class Meta:
        managed = False
        db_table = 'aluno'
        ordering = ('id',)


class Matricula(models.Model):
    aluno = models.ForeignKey('Aluno', on_delete=models.CASCADE, related_name='%(app_label)s_%(class)s_related',
                              db_column='aluno_id')
    turma = models.ForeignKey('unidade.Turma', on_delete=models.CASCADE, related_name='%(app_label)s_%(class)s_related',
                              db_column='turma_id')
    statusmatricula = models.CharField(max_length=255, null=False)
    datamatricula = models.DateField()
    statusatual = models.CharField(max_length=255)
    serie = models.ForeignKey('unidade.Serie', on_delete=models.CASCADE, related_name='%(app_label)s_%(class)s_related',
                              db_column='serie_id')

    def __str__(self):
        return self.statusmatricula

    class Meta:
        managed = False
        db_table = 'matricula'
        ordering = ('id',)


class AlunoFrequenciaMes(models.Model):
    totalfaltas = models.IntegerField(null=False)
    matricula = models.ForeignKey('Matricula', on_delete=models.CASCADE, related_name='%(app_label)s_%(class)s_related',
                                  db_column='matricula_id')
    bimestre = models.ForeignKey('bimestre.Bimestre', on_delete=models.CASCADE,
                                 related_name='%(app_label)s_%(class)s_related',
                                 db_column='bimestre_id')

    disciplina = models.ForeignKey('grade.Disciplina', on_delete=models.CASCADE,
                                 related_name='%(app_label)s_%(class)s_related',
                                 db_column='disciplina_id')

    class Meta:
        managed = False
        db_table = 'alunofrequenciames'
        ordering = ('id',)
