from rest_framework import status, viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from src.core.jogo.domain.entity_jogo import Jogo
from src.core.locacao.domain.locacao.entity_locacao import ItemLocacao, JogoPlataforma
from src.core.locacao.ports.input.adicionar_jogo_service import (
    AdicionarJogoService,
    InputItemLocacao,
)
from src.core.locacao.ports.input.calcular_custo_total import (
    CalculaCustoTotalService,
)
from src.core.locacao.ports.input.criar_locacao_service import (
    CriarLocacao,
    InputLocacao,
)
from src.core.plataforma.domain.entity_plataforma import Plataforma
from src.framework.locacao.adapters.input.serializers import (
    CustoTotalOutputSerializer,
    ItemLocacaoUpdateSerializer,
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
            )
            output = service.execute(
                locacao=input,
            )
            response = LocacaoOutputSerializer(output)

        except Exception as error:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={"error": str(error)},
            )

        return Response(
            status=status.HTTP_201_CREATED,
            data=(response.data),
        )

    def partial_update(self, request: Request, pk=None) -> Response:
        try:
            id = int(pk)
            serializer = ItemLocacaoUpdateSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            service = AdicionarJogoService(locacao_repository=DjangoORMRepository())

            input = InputItemLocacao(
                jogo_plataforma=JogoPlataforma(
                    id=serializer.validated_data["jogo_plataforma"]["id"],
                    jogo=Jogo(
                        id=serializer.validated_data["jogo_plataforma"]["jogo"]["id"],
                        titulo=serializer.validated_data["jogo_plataforma"]["jogo"][
                            "titulo"
                        ],
                    ),
                    plataforma=Plataforma(
                        id=serializer.validated_data["jogo_plataforma"]["plataforma"][
                            "id"
                        ],
                        nome=serializer.validated_data["jogo_plataforma"]["plataforma"][
                            "nome"
                        ],
                    ),
                    preco_diario=serializer.validated_data["jogo_plataforma"][
                        "preco_diario"
                    ],
                ),
                dias=serializer.validated_data["dias"],
                quantidade=serializer.validated_data["quantidade"],
            )
            output = service.execute(
                item=input,
                id_locacao=id,
            )
            response = LocacaoOutputSerializer(instance=output)

        except Exception as error:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={"error": str(error)},
            )

        return Response(
            status=status.HTTP_200_OK,
            data=(response.data),
        )

    def retrieve(self, request: Request, pk=None) -> Response:
        try:
            id = int(pk)
            service = CalculaCustoTotalService(locacao_repository=DjangoORMRepository())
            output = service.execute(id_locacao=id)
            response = CustoTotalOutputSerializer(output)

        except Exception as error:
            print("error", error)
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={"error": str(error)},
            )

        return Response(
            status=status.HTTP_200_OK,
            data=(response.data),
        )
