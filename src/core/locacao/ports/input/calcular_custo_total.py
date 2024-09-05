from dataclasses import dataclass

from src.core.locacao.ports.output.locacao_repositoy import LocacaoRepository


@dataclass
class CustoTotal:
    valor: float


class CalculaCustoTotalService:
    def __init__(self, locacao_repository: LocacaoRepository):
        self.locacao_repository = locacao_repository

    def execute(self, id_locacao: int) -> CustoTotal:
        locacao = self.locacao_repository.get_by_id(id_locacao)
        valor_total = 0
        for item in locacao.itens:
            valor_total += (
                item.jogo_plataforma.preco_diario * item.dias * item.quantidade
            )

        return CustoTotal(valor=valor_total)
