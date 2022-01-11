from rest_framework import viewsets
from .serializers import PedidoSerializer
from .models import Pedido
from rest_framework.response import Response
from rest_framework.decorators import action, permission_classes
from rest_framework import permissions
from registro.models import Registro


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action in ['create', 'update',]:
            permission_classes = [permissions.AllowAny]

        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        #import pdb; pdb.set_trace()
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(
                articulo_id = request.data['articulo_id'],
                estado_id  = request.data['estado_id']
            )
            return Response(serializer.data)
        else:
            return Response("Datos no validos")
    
    def update(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        #import pdb; pdb.set_trace()
        if serializer.is_valid():
            articulo_id = request.data['articulo_id']
            estado_id  = request.data['estado_id']
            serializer.save(
                articulo_id = request.data['articulo_id'],
                estado_id  = request.data['estado_id']
            )

            id = self.kwargs['pk']
            registro = Registro()
            registro.pedido_id = id
            registro.estado_id = estado_id
            registro.accion = "Actualización de estado"
            registro.save()

            return Response(serializer.data)
        else:
            return Response("Datos no validos")
    
