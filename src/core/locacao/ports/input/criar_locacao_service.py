from dataclasses import dataclass

from src.core.client.domain.entity_client import Cliente
from src.core.jogo.domain.entity_jogo_plataforma import JogoPlataforma
from src.core.locacao.domain.entity_locacao import Locacao
from src.core.locacao.ports.output.locacao_repositoy import LocacaoRepository


@dataclass
class ItemLocacao:
    jogo_plataforma: JogoPlataforma
    dias: int
    quantidade: int


@dataclass
class InputCliente:
    id: int
    nome: str
    email: str
    telefone: str


@dataclass
class InputLocacao:
    data: str
    itens: list[ItemLocacao]
    cliente: InputCliente


class CriarLocacao:
    def __init__(self, locacao_repository: LocacaoRepository):
        self.locacao_repository = locacao_repository

    def execute(self, locacao: InputLocacao) -> Locacao:
        _locacao = Locacao(
            data=locacao.data,
            itens=[
                ItemLocacao(
                    jogo_plataforma=item.jogo_plataforma,
                    dias=item.dias,
                    quantidade=item.quantidade,
                )
                for item in locacao.itens
            ],
            cliente=Cliente(
                id=locacao.cliente.id,
                nome=locacao.cliente.nome,
                email=locacao.cliente.email,
                telefone=locacao.cliente.telefone,
            ),
        )
        return self.locacao_repository.save(_locacao)
