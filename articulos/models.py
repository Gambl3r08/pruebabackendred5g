from django.db import models

class Articulo(models.Model):
    nombre = models.CharField(max_length=200)
    valor = models.IntegerField()

    class Meta:
        db_table = "articulos_articulo"
    
    def __str__(self):
        return str(self.nombre)



