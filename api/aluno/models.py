from django.db import models
from django.db.models import Avg, Max

# Create your models here.
from grade.models import DisciplinaAluno
from nota.models import AlunoNotaMes
from ocorrencia.models import Ocorrencia


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

    anoletivo = models.ForeignKey('grade.AnoLetivo', on_delete=models.CASCADE,
                                  related_name='%(app_label)s_%(class)s_related',
                                  db_column='anoletivo_id')

    @property
    def aluno_frequencia_mes(self):
        return AlunoFrequenciaMes.objects.filter(matricula=self)

    @property
    def ocorrencias(self):
        return Ocorrencia.objects.filter(matriculaaluno=self)

    @property
    def aluno_nota_mes(self):
        return AlunoNotaMes.objects.filter(matricula=self)

    @property
    def todas_disciplinas_aluno(self):
        return DisciplinaAluno.objects.filter(matricula=self)

    @property
    def todas_alunos_notas_mes(self):
        return AlunoNotaMes.objects.filter(matricula=self)

    def __str__(self):
        return self.statusmatricula

    class Meta:
        managed = False
        db_table = 'matricula'
        ordering = ('id',)


class AlunoFrequenciaMes(models.Model):
    totalfaltas = models.IntegerField(null=False)
    tipolancamentofrequencia = models.CharField(null=True, max_length=255)

    matricula = models.ForeignKey('Matricula', on_delete=models.CASCADE, related_name='%(app_label)s_%(class)s_related',
                                  db_column='matricula_id')

    bimestre = models.ForeignKey('bimestre.Bimestre', on_delete=models.CASCADE,
                                 related_name='%(app_label)s_%(class)s_related',
                                 db_column='bimestre_id')

    disciplina = models.ForeignKey('grade.Disciplina', on_delete=models.CASCADE, null=True,
                                   related_name='%(app_label)s_%(class)s_related',
                                   db_column='disciplina_id')

    disciplinaaluno = models.ForeignKey('grade.DisciplinaAluno', on_delete=models.CASCADE,
                                        related_name='%(app_label)s_%(class)s_related',
                                        db_column='disciplinaaluno_id')

    class Meta:
        managed = False
        db_table = 'alunofrequenciames'
        ordering = ('id',)
    #
    # def save(self, *args, **kwargs):
    #     ultimoid = AlunoFrequenciaMes.objects.all().aggregate(Max('id'))
    #     self.id = ultimoid['id__max'] + 1
    #     super(AlunoFrequenciaMes, self).save()
    #
    #
    #
