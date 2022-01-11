from django.contrib import admin
from .models import Pedido

class PedidoAdmin(admin.ModelAdmin):
    list_display = ('nombreCliente', 'fechaPedido', 'horaPedido', 'articulo', 'cantidad', 
    'valorTotal', 'direccion', 'ciudad', 'telefonoCliente', 'estado',)

admin.site.register(Pedido, PedidoAdmin)
