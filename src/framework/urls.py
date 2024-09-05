from django.contrib import admin
from django.urls import path
from src.framework.locacao.adapters.input.add_item_view import AddItemInLocacaoViewSet
from src.framework.locacao.adapters.input.create_locaco_view import CreateLocacaoViewSet
from src.framework.locacao.adapters.input.custo_total_view import CustoTotalViewSet

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "api/locacao/",
        CreateLocacaoViewSet.as_view({"post": "create"}),
        name="locacao-list",
    ),
    path(
        "api/locacao/<int:pk>/jogo/",
        AddItemInLocacaoViewSet.as_view({"patch": "partial_update"}),
        name="add-item-locacao",
    ),
    path(
        "api/locacao/<int:pk>/custo/",
        CustoTotalViewSet.as_view({"get": "retrieve"}),
        name="locacao-detail",
    ),
]
