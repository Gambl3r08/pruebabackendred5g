from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import ArticuloSerializer
from .models import Articulo

class ArticuloViewSet(viewsets.ModelViewSet):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer
