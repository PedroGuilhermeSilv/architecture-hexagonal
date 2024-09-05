from django.contrib import admin

from .models import ItemLocacao, Locacao

admin.site.register(Locacao)
admin.site.register(ItemLocacao)
