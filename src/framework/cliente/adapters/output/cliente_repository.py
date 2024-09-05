from src.core.client.domain.entity_client import Cliente
from src.core.client.ports.output.repository import ClienteRepository
from src.framework.cliente.models import Cliente as ClienteModel


class DjangoORMClienteRepository(ClienteRepository):
    def get_by_email(self, email: str) -> Cliente:
        cliente = ClienteModel.objects.get(email=email)
        return Cliente(
            id=cliente.id,
            email=cliente.email,
            telefone=cliente.telefone,
            nome=cliente.nome,
            senha=cliente.senha,
        )
