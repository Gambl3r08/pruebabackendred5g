from django.contrib import admin
from .models import Registro


class RegistroAdmin(admin.ModelAdmin):
    list_display = ('pedido', 'estado', 'fecha', 'hora', 'accion')

admin.site.register(Registro, RegistroAdmin)