from dataclasses import dataclass, field
from random import randint


@dataclass
class Plataforma:
    nome: str
    id: int = field(default_factory=lambda: randint(1, 1000))
