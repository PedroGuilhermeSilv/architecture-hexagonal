from django.db import models


class Cliente(models.Model):
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    nome = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
