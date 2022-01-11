from django.db import models
from django.db.models.deletion import PROTECT
from estados.models import Estado
from pedidos.models import Pedido


class Registro(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=PROTECT)
    estado = models.ForeignKey(Estado, on_delete=PROTECT)
    fecha = models.DateField(auto_now_add=True)
    hora = models.TimeField(auto_now=True)
    accion = models.CharField(max_length=100)

