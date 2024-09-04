from dataclasses import dataclass, field
from random import randint

from src.core.jogo.domain.entity_jogo import Jogo
from src.core.plataforma.domain.entity_plataforma import Plataforma


@dataclass
class JogoPlataforma:
    jogo: Jogo
    plataforma: Plataforma
    preco_diario: float
    id: int = field(default_factory=lambda: randint(1, 1000))

    def __post_init__(self):
        self.jogo.plataformas.append(self)
