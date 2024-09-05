from abc import ABC, abstractmethod

from src.core.locacao.domain.entity_locacao import Locacao


class LocacaoRepository(ABC):

    @abstractmethod
    def save(self, locacao: Locacao) -> Locacao:
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> Locacao:
        pass

    @abstractmethod
    def update(self, locacao: Locacao) -> Locacao:
        pass
