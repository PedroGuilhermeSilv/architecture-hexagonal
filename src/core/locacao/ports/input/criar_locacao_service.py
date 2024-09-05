from dataclasses import dataclass, field
from random import randint

from src.core.jogo.domain.entity_jogo_plataforma import JogoPlataforma
from src.core.locacao.domain.locacao.entity_locacao import Locacao
from src.core.locacao.ports.output.locacao_repositoy import LocacaoRepository


@dataclass
class ItemLocacao:
    jogo_plataforma: JogoPlataforma
    dias: int
    quantidade: int


@dataclass
class InputLocacao:
    data: str
    itens: list[ItemLocacao]
    id: int = field(default_factory=lambda: randint(1, 1000))


class CriarLocacao:
    def __init__(self, locacao_repository: LocacaoRepository):
        self.locacao_repository = locacao_repository

    def execute(self, locacao: InputLocacao) -> Locacao:
        _locacao = Locacao(
            id=locacao.id,
            data=locacao.data,
            itens=[
                ItemLocacao(
                    jogo_plataforma=item.jogo_plataforma,
                    dias=item.dias,
                    quantidade=item.quantidade,
                )
                for item in locacao.itens
            ],
        )
        return self.locacao_repository.save(_locacao)
