from django.db import models
from django.db.models import Avg, Max


# Create your models here.
class TipoOcorrencia(models.Model):
    descricao = models.CharField(max_length=255)
    codigo = models.IntegerField()

    def __str__(self):
        return self.descricao

    class Meta:
        managed = False
        db_table = 'tipoocorrencia'
        ordering = ('id',)


class Ocorrencia(models.Model):
    datahora = models.DateTimeField()
    datahoracadastro = models.DateTimeField()
    funcionarioescola = models.ForeignKey('funcionario.FuncionarioEscola', on_delete=models.CASCADE,
                                          related_name='%(app_label)s_%(class)s_related',
                                          db_column='funcionarioescola_id')

    descricao = models.CharField(max_length=255, null=True)
    matriculaaluno = models.ForeignKey('aluno.Matricula', on_delete=models.CASCADE,
                                       related_name='%(app_label)s_%(class)s_related',
                                       db_column='matriculaaluno_id')

    tipoocorrencia = models.ForeignKey('TipoOcorrencia', on_delete=models.CASCADE,
                                       related_name='%(app_label)s_%(class)s_related',
                                       db_column='tipoocorrencia_id')

    aluno = models.ForeignKey('aluno.Aluno', on_delete=models.CASCADE, related_name='%(app_label)s_%(class)s_related', db_column='aluno_id')
    anoletivo = models.ForeignKey('grade.AnoLetivo', on_delete=models.CASCADE,
                                  related_name='%(app_label)s_%(class)s_related',
                                  db_column='anoletivo_id')

    funcionario = models.ForeignKey('funcionario.Funcionario', on_delete=models.CASCADE,
                                    related_name='%(app_label)s_%(class)s_related',
                                    db_column='funcionario_id')

    unidade = models.ForeignKey('unidade.Unidade', on_delete=models.CASCADE,
                                related_name='%(app_label)s_%(class)s_related',
                                db_column='unidade_id')

    enviadosms = models.BooleanField()
    anoletivo = models.ForeignKey('grade.AnoLetivo', on_delete=models.CASCADE,
                                  related_name='%(app_label)s_%(class)s_related',
                                  db_column='ano_letivo', null=True)

    dataenviosms = models.DateTimeField(null=True)
    resumosms = models.CharField(max_length=255, null=True)
    observacao = models.CharField(max_length=255, null=True)
    numerotelefone = models.IntegerField(null=True)


    def __str__(self):
        return self.aluno + ' - ' + self.tipoocorrencia

    def save(self, *args, **kwargs):
        ultimoid = Ocorrencia.objects.all().aggregate(Max('id'))
        self.id = ultimoid['id__max'] + 1
        super(Ocorrencia, self).save()

    class Meta:
        managed = False
        db_table = 'ocorrencia'
        ordering = ('id',)
