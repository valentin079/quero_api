from django.contrib import admin
from quero_delivery.models import Endereco, Pedido

class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'bairro', 'municipio', 'uf', 'num_casa', 'complemento', 'referencia' )
    list_display_links = ('descricao', 'bairro')
    search_fields = ('descricao',)
    list_per_page = 20
admin.site.register(Endereco, EnderecoAdmin)

class PedidoAdmin(admin.ModelAdmin):
    list_display = ('endereco', 'produtos' )
    list_per_page = 20

admin.site.register(Pedido, PedidoAdmin)