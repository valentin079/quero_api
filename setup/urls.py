from django.contrib import admin
from django.urls import path, include
from quero_delivery.views import EnderecosViewSet, PedidosViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('enderecos', EnderecosViewSet, basename = 'Enderecos')
router.register('pedidos', PedidosViewSet, basename = 'Pedidos')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]