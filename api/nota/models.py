from django.db import models
from django.db.models import Avg, Max


# Create your models here.
class AlunoNotaMes(models.Model):
    nota = models.DecimalField(max_digits=5, decimal_places=2)

    bimestre = models.ForeignKey('bimestre.Bimestre', on_delete=models.CASCADE,
                                 related_name='%(app_label)s_%(class)s_related', db_column='bimestre_id')
    sequencia = models.IntegerField(null=True)
    disciplinaaluno = models.ForeignKey('grade.DisciplinaAluno', on_delete=models.CASCADE,
                                        related_name='%(app_label)s_%(class)s_related', db_column='disciplinaaluno_id')
    inseridofechamento = models.BooleanField(default=False)
    tipolancamentonota = models.CharField(max_length=255)
    anoletivo = models.ForeignKey('grade.AnoLetivo', on_delete=models.CASCADE, null=True,
                                  related_name='%(app_label)s_%(class)s_related', db_column='ano_letivo')
    matricula = models.ForeignKey('aluno.Matricula', on_delete=models.CASCADE,
                                  related_name='%(app_label)s_%(class)s_related', db_column='matricula_id')
    unidade = models.ForeignKey('unidade.Unidade', on_delete=models.CASCADE, null=True,
                                related_name='%(app_label)s_%(class)s_related', db_column='id_unidade')
    disciplina = models.ForeignKey('grade.Disciplina', on_delete=models.CASCADE,
                                   related_name='%(app_label)s_%(class)s_related', db_column='disciplina_id')
    datahora = models.DateTimeField()
    usuario = models.ForeignKey('pessoa.Usuario', on_delete=models.CASCADE, null=True,
                                related_name='%(app_label)s_%(class)s_related', db_column='usuario_id')

    # def save(self, *args, **kwargs):
    #     if (self.id == None):
    #         ultimoid = AlunoNotaMes.objects.all().aggregate(Max('id'))
    #         self.id = ultimoid['id__max'] + 1
    #         super(AlunoNotaMes, self).save()

    class Meta:
        managed = False
        db_table = 'alunonotames'
        ordering = ('id',)
