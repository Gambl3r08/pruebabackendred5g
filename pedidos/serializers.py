from rest_framework import serializers
from .models import Pedido
from articulos.serializers import ArticuloSerializer
from articulos.models import Articulo
from estados.serializers import EstadoSerializer
from estados.models import Estado


class PedidoSerializer(serializers.HyperlinkedModelSerializer):
    articulo = ArticuloSerializer(read_only=True)
    articulo_id = serializers.PrimaryKeyRelatedField(write_only = True, 
    queryset  = Articulo.objects.all())

    estado = EstadoSerializer(read_only=True)
    estado_id = serializers.PrimaryKeyRelatedField(write_only = True,
     queryset = Estado.objects.all())
        
    class Meta:
        model = Pedido
        fields = ['id', 'nombreCliente', 'fechaPedido', 'horaPedido', 'articulo', 'articulo_id', 
        'cantidad', 'valorTotal', 'direccion', 'ciudad', 'telefonoCliente', 'estado', 'estado_id']
