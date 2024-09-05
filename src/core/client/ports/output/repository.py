from abc import ABC, abstractmethod

from src.core.client.domain.entity_client import Cliente


class ClienteRepository(ABC):

    @abstractmethod
    def get_by_email(self, email: str) -> Cliente:
        pass
