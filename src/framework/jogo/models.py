from django.db import models
from src.framework.plataforma.models import Plataforma


class Jogo(models.Model):
    titulo = models.CharField(max_length=200)
    plataformas = models.ManyToManyField(Plataforma, through="JogoPlataforma")

    def __str__(self):
        return self.titulo

    class Meta:
        db_table = "jogo"


class JogoPlataforma(models.Model):
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE)
    plataforma = models.ForeignKey(Plataforma, on_delete=models.CASCADE)
    preco_diario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.jogo.titulo} - {self.plataforma.nome} (${self.preco_diario})"

    class Meta:
        db_table = "jogo_jogoplataforma"
