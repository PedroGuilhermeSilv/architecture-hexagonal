from rest_framework import status, viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from src.core.client.domain.entity_client import Cliente
from src.core.jogo.domain.entity_jogo import Jogo
from src.core.locacao.domain.entity_locacao import ItemLocacao, JogoPlataforma
from src.core.locacao.ports.input.criar_locacao_service import (
    CriarLocacao,
    InputLocacao,
    InputCliente
)
from src.core.plataforma.domain.entity_plataforma import Plataforma
from src.framework.locacao.adapters.input.serializers import (
    LocacaoInputSerializer,
    LocacaoOutputSerializer,
)
from src.framework.locacao.adapters.output.repository import DjangoORMLocacaoRepository


class CreateLocacaoViewSet(viewsets.ViewSet):
    def create(self, request: Request) -> Response:
        try:
            serializer = LocacaoInputSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            service = CriarLocacao(locacao_repository=DjangoORMLocacaoRepository())

            input = InputLocacao(
                data=serializer.validated_data["data"],
                itens=[
                    ItemLocacao(
                        jogo_plataforma=JogoPlataforma(
                            jogo=Jogo(
                                titulo=item["jogo_plataforma"]["jogo"]["titulo"],
                            ),
                            plataforma=Plataforma(
                                nome=item["jogo_plataforma"]["plataforma"]["nome"],
                            ),
                            preco_diario=item["jogo_plataforma"]["preco_diario"],
                        ),
                        dias=item["dias"],
                        quantidade=item["quantidade"],
                    )
                    for item in serializer.validated_data["itens"]
                ],
                cliente=InputCliente(
                    id=serializer.validated_data["cliente"]["id"],
                    nome=serializer.validated_data["cliente"]["nome"],
                    email=serializer.validated_data["cliente"]["email"],
                    telefone=serializer.validated_data["cliente"]["telefone"],
                ),
            )
            output = service.execute(
                locacao=input,
            )
            response = LocacaoOutputSerializer(output)

        except Exception as error:
            print(error)
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={"error": str(error)},
            )

        return Response(
            status=status.HTTP_201_CREATED,
            data=(response.data),
        )
