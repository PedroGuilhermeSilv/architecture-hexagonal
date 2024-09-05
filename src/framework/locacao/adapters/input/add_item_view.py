from rest_framework import status, viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from src.core.jogo.domain.entity_jogo import Jogo
from src.core.locacao.domain.entity_locacao import JogoPlataforma
from src.core.locacao.ports.input.adicionar_jogo_service import (
    AdicionarJogoService,
    InputItemLocacao,
)
from src.core.plataforma.domain.entity_plataforma import Plataforma
from src.framework.locacao.adapters.input.serializers import (
    ItemLocacaoUpdateSerializer,
    LocacaoOutputSerializer,
)
from src.framework.locacao.adapters.output.repository import DjangoORMLocacaoRepository


class AddItemInLocacaoViewSet(viewsets.ViewSet):
    def partial_update(self, request: Request, pk=None) -> Response:
        try:
            id = int(pk)
            serializer = ItemLocacaoUpdateSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            service = AdicionarJogoService(
                locacao_repository=DjangoORMLocacaoRepository(),
            )

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
