from abc import ABC, abstractmethod

from src.core.locacao.domain.locacao.entity_locacao import Locacao


class LocacaoRepository(ABC):
    @abstractmethod
    def save(self, locacao: Locacao) -> Locacao:
        pass
