from django.db import models
from src.framework.cliente.models import Cliente
from src.framework.jogo.models import JogoPlataforma


class Locacao(models.Model):
    data = models.DateTimeField(auto_now=True)
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        default=None,
        null=True,
    )


class ItemLocacao(models.Model):
    locacao = models.ForeignKey(
        Locacao,
        on_delete=models.CASCADE,
        default=None,
        null=True,
    )
    dias = models.IntegerField()
    quantidade = models.IntegerField()
    jogo_plataforma = models.ForeignKey(JogoPlataforma, on_delete=models.CASCADE)
