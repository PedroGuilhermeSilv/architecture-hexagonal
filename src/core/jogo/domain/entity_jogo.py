from dataclasses import dataclass, field

from src.core.plataforma.domain.entity_plataforma import Plataforma


@dataclass
class Jogo:
    id: int
    titulo: str
    plataformas: list[Plataforma] = field(default_factory=list)
