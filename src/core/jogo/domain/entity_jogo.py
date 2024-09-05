from dataclasses import dataclass, field
from random import randint

from src.core.plataforma.domain.entity_plataforma import Plataforma


@dataclass
class Jogo:
    titulo: str
    id: int = field(default_factory=lambda: randint(1, 1000))
    plataformas: list[Plataforma] = field(default_factory=list)
