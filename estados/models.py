from django.db import models


class Estado(models.Model):
    estado = models.CharField(max_length=50)

    class Meta:
        db_table = "estados_estado"
    
    def __str__(self):
        return str(self.estado)

