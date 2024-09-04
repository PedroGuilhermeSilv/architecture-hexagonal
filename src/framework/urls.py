from django.contrib import admin
from django.urls import path
from rest_framework import routers
from src.framework.locacao.adapters.input.views import LocacaoViewSet

router = routers.DefaultRouter()

router.register(r"api/locacao", LocacaoViewSet, basename="locacao")


urlpatterns = [
    path("admin/", admin.site.urls),
] + router.urls
