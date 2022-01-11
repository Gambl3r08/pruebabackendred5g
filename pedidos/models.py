from django.db import models
from django.db.models.deletion import PROTECT
from articulos.models import Articulo
from estados.models import Estado

class Pedido(models.Model):
    nombreCliente = models.CharField(max_length=200)
    fechaPedido = models.DateField(auto_now_add=True)
    horaPedido = models.TimeField(auto_now=True)
    articulo = models.ForeignKey(Articulo, on_delete=PROTECT)
    cantidad = models.IntegerField()
    valorTotal = models.IntegerField()
    direccion = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=200)
    telefonoCliente = models.CharField(max_length=200)
    estado =  models.ForeignKey(Estado, on_delete=PROTECT, default=1)
    
    

    class Meta:
        db_table = "pedidos_pedido"
    
    def __str__(self):
        return str(self.nombreCliente)


