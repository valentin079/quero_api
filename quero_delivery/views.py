from rest_framework import viewsets
from quero_delivery.models import Endereco, Pedido
from quero_delivery.serializer import EnderecoSerializer, PedidoSerializer

class EnderecosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os enderecos"""
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer

class PedidosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os pedidos"""
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer