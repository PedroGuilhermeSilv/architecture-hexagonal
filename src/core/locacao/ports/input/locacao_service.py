from src.core.locacao.domain.locacao.entity_locacao import Locacao
from src.core.locacao.ports.output.locacao_repositoy import LocacaoRepository


class CriarLocacao:
    def __init__(self, locacao_repository: LocacaoRepository):
        self.locacao_repository = locacao_repository

    def criar(self, locacao) -> Locacao:
        return self.locacao_repository.criar(locacao)
