from rest_framework import serializers
from .models import Estado
class EstadoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Estado
        fields = ['id', 'estado',]
    
