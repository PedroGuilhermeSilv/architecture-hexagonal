from rest_framework import status, viewsets
from rest_framework.request import Request
from rest_framework.response import Response


class LocacaoViewSet(viewsets.ViewSet):
    def create(self, request: Request) -> Response:
        serializer = CreatePostoDeTrabalhoRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        service = CreatePostoDeTrabalho(repository=DjangoORMPostoDeTrabalhoRepository())

        try:
            response = service.execute(
                CreatePostoDeTrabalhoRequest(**serializer.validated_data),
            )

        except InvalidPostoDeTrabalhoError as error:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={"error": str(error)},
            )

        return Response(
            status=status.HTTP_201_CREATED,
            data=CreatePostoDeTrabalhoResponseSerializer(response).data,
        )

