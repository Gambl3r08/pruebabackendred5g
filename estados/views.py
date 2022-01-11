from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import EstadoSerializer
from .models import Estado


class EstadoViewSet(viewsets.ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer


