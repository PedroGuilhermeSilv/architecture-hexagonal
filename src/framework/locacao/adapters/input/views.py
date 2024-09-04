from rest_framework import status, viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from src.core.jogo.domain.entity_jogo import Jogo
from src.core.locacao.domain.locacao.entity_locacao import ItemLocacao, JogoPlataforma
from src.core.locacao.ports.input.locacao_service import (
    CriarLocacao,
    InputLocacao,
)
from src.core.plataforma.domain.entity_plataforma import Plataforma
from src.framework.locacao.adapters.input.serializers import (
    LocacaoInputSerializer,
    LocacaoOutputSerializer,
)
from src.framework.locacao.adapters.output.repository import DjangoORMRepository


class LocacaoViewSet(viewsets.ViewSet):
    def create(self, request: Request) -> Response:
        try:
            serializer = LocacaoInputSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            service = CriarLocacao(locacao_repository=DjangoORMRepository())

            print("1")

            input = InputLocacao(
                id=serializer.validated_data["id"],
                data=serializer.validated_data["data"],
                itens=[
                    ItemLocacao(
                        jogo_plataforma=JogoPlataforma(
                            id=item["jogo_plataforma"]["id"],
                            jogo=Jogo(
                                id=item["jogo_plataforma"]["jogo"]["id"],
                                titulo=item["jogo_plataforma"]["jogo"]["titulo"],
                            ),
                            plataforma=Plataforma(
                                id=item["jogo_plataforma"]["plataforma"]["id"],
                                nome=item["jogo_plataforma"]["plataforma"]["nome"],
                            ),
                            preco_diario=item["jogo_plataforma"]["preco_diario"],
                        ),
                        dias=item["dias"],
                        quantidade=item["quantidade"],
                    )
                    for item in serializer.validated_data["itens"]
                ],
            )
            print("1")
            response = service.criar(
                locacao=input,
            )
            print("1")

        except Exception as error:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={"error": str(error)},
            )

        return Response(
            status=status.HTTP_201_CREATED,
            data=(LocacaoOutputSerializer(response).data),
        )
