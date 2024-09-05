from dataclasses import dataclass

from src.core.jogo.domain.entity_jogo_plataforma import JogoPlataforma
from src.core.locacao.domain.locacao.entity_locacao import Locacao
from src.core.locacao.ports.output.locacao_repositoy import LocacaoRepository


@dataclass
class InputItemLocacao:
    jogo_plataforma: JogoPlataforma
    dias: int
    quantidade: int


class AdicionarJogoService:
    def __init__(self, locacao_repository: LocacaoRepository):
        self.locacao_repository = locacao_repository

    def execute(self, item: InputItemLocacao, id_locacao: int) -> Locacao:
        locacao = self.locacao_repository.get_by_id(id_locacao)
        locacao.adicionar_jogo(item)
        return self.locacao_repository.update(locacao)
