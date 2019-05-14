from django.db import models

# Create your models here.
from funcionario.models import Funcionario


class Usuario(models.Model):
    ativo = models.BooleanField()
    login = models.CharField(max_length=255)
    matricula = models.CharField(max_length=255)
    senha = models.CharField(max_length=255)
    pessoafisica = models.ForeignKey('PessoaFisica', on_delete=models.CASCADE,
                                     related_name='%(app_label)s_%(class)s_related',
                                     db_column='pessoafisica_id')
    perfil = models.ForeignKey('Perfil', on_delete=models.CASCADE,
                               related_name='%(app_label)s_%(class)s_related',
                               db_column='perfil')

    class Meta:
        managed = False
        db_table = 'usuario'
        ordering = ('id',)


class Perfil(models.Model):
    descricao = models.CharField(max_length=255)
    perfilexterno = models.BooleanField()
    vertodasasescolas = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'perfil'
        ordering = ('id',)


class PessoaFisica(models.Model):
    cpf = models.CharField('cpf', null=True, max_length=255)
    datanascimento = models.DateField('datanascimento')
    nome = models.CharField('nome', null=False, max_length=255)
    rg = models.CharField('rg', null=True, max_length=255)
    nacionalidade = models.CharField('nacionalidade', max_length=255, null=False)
    sexo = models.CharField('sexo', max_length=255, null=False)
    email = models.CharField('email', max_length=255, null=True)
    senha = models.CharField('senha', max_length=255, null=True)

    @property
    def usuario(self):
        return Usuario.objects.get(pessoafisica=self)

    def __str__(self):
        return self.nome

    class Meta:
        managed = False
        db_table = 'pessoafisica'
        ordering = ('id',)
