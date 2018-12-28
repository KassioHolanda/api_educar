from django.db import models


# Create your models here.
class Bimestre(models.Model):
    descricao = models.CharField(max_length=255)
    sequencia = models.IntegerField()
    temnota = models.BooleanField()

    def __str__(self):
        return self.descricao

    class Meta:
        managed = False
        db_table = 'bimestre'
        ordering = ('id',)
