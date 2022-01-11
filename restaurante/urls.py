from django.contrib import admin
from django.urls import include, path
from estados.views import EstadoViewSet
from articulos.views import ArticuloViewSet
from pedidos.views import PedidoViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'estados', EstadoViewSet)
router.register(r'articulos', ArticuloViewSet)
router.register(r'pedidos', PedidoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
