from django.contrib.auth.models import AbstractUser
from django.db import models

class Recibos(models.Model):
    titulo = models.CharField(max_length=70, blank=False, default='')
    descricao = models.CharField(max_length=200,blank=False, default='')
    data = models.DateField()

    def __str__(self):
        return f'{self.titulo}'