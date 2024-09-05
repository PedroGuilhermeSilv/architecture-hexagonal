from rest_framework import status, viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from src.core.locacao.ports.input.calcular_custo_total import (
    CalculaCustoTotalService,
)
from src.framework.locacao.adapters.input.serializers import (
    CustoTotalOutputSerializer,
)
from src.framework.locacao.adapters.output.repository import DjangoORMLocacaoRepository


class CustoTotalViewSet(viewsets.ViewSet):
    def retrieve(self, request: Request, pk=None) -> Response:
        try:
            id = int(pk)
            service = CalculaCustoTotalService(
                locacao_repository=DjangoORMLocacaoRepository(),
            )
            output = service.execute(id_locacao=id)
            response = CustoTotalOutputSerializer(output)

        except Exception as error:
            print(error)
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={"error": str(error)},
            )

        return Response(
            status=status.HTTP_200_OK,
            data=(response.data),
        )
