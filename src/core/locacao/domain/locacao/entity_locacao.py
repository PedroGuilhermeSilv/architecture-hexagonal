from dataclasses import dataclass, field
from datetime import datetime
from random import randint
from typing import Optional

from src.core.jogo.domain.entity_jogo_plataforma import JogoPlataforma


@dataclass
class ItemLocacao:
    jogo_plataforma: JogoPlataforma
    dias: int
    quantidade: int
    locacao: Optional["Locacao"] = None


@dataclass
class Locacao:
    id: int = field(default_factory=lambda: randint(1, 1000))
    data: datetime = field(default_factory=datetime.now)
    itens: list[ItemLocacao] | None = field(default_factory=list)  # noqa: F821

    def adicionar_jogo(self, item: ItemLocacao):
        self.itens.append(item)
