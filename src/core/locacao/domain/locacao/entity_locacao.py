from dataclasses import dataclass, field
from datetime import datetime
from random import randint

from src.core.jogo.domain.entity_jogo_plataforma import JogoPlataforma


@dataclass
class ItemLocacaoDTO:
    locacao: "Locacao"
    jogo_plataforma: JogoPlataforma
    dias: int
    quantidade: int

    def __post_init__(self):
        self.locacao.itens.append(self)


@dataclass
class Locacao:
    id: int = field(default_factory=lambda: randint(1, 1000))
    data: datetime = field(default_factory=datetime.now)
    itens: list["ItemLocacaoDTO"] | None = field(default_factory=list)  # noqa: F821
