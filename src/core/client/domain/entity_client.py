from dataclasses import dataclass, field

from core.locacao.domain.entity.entity_locacao import Locacao


@dataclass
class Cliente:
    id: int
    email: str
    telefone: str
    nome: str
    senha: str
    locacao: list[Locacao] = field(default_factory=list)
