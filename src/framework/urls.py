from django.contrib import admin
from django.urls import path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from src.framework.locacao.adapters.input.add_item_view import AddItemInLocacaoViewSet
from src.framework.locacao.adapters.input.create_locaco_view import CreateLocacaoViewSet
from src.framework.locacao.adapters.input.custo_total_view import CustoTotalViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="API Game Rental",
        default_version="v1",
        description="This Django-built API simulates a game rental system using hexagonal architecture.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="pedromoura8970@hotmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
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
