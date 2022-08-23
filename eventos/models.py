from django.db import models

class Evento(models.Model):
    nome = models.CharField(max_length=200, null=False)


    def __str__(self):
        return self.nome
