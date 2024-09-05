from django.contrib import admin
from django.urls import path
from rest_framework import routers

from framework.locacao.adapters.input.controller import LocacaoViewSet

router = routers.DefaultRouter()

router.register(r"api/locacao", LocacaoViewSet, basename="locacao")


urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "api/locacao/",
        LocacaoViewSet.as_view({"post": "create"}),
        name="locacao-list",
    ),
    path(
        "api/locacao/<int:pk>/jogo/",
        LocacaoViewSet.as_view({"patch": "partial_update"}),
        name="add-item-locacao",
    ),
    path(
        "api/locacao/<int:pk>/custo/",
        LocacaoViewSet.as_view({"get": "retrieve"}),
        name="locacao-detail",
    ),
]
