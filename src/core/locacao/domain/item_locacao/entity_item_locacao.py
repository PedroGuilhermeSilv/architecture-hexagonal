from dataclasses import dataclass

from core.jogo.domain.entity_jogo_plataforma import JogoPlataforma
from core.locacao.domain.locacao.entity_locacao import Locacao


@dataclass
class ItemLocacao:
    locacao: Locacao | None
    jogo_plataforma: JogoPlataforma
    dias: int
    quantidade: int

    def __post_init__(self):
        self.locacao.itens.append(self)
