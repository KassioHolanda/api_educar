from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


# Create your models here.
from pessoa.models import PessoaFisica

class Usuario(AbstractUser):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    REQUIRED_FIELDS = ['nome']

    def __str__(self):
        return str(self.nome)

    # def salvar_todos_usuarios(self):
    #     todasPessoas = PessoaFisica.objects.all()
    #     for pessoa in todasPessoas:
    #         User.objects.create