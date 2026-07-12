from django.urls import path
from .views import cliente_views

urlpatterns = [
    path('cliente/cadastro', cliente_views.cadastrar_cliente, name='cadastrar_cliente'),
    path('cliente/lista', cliente_views.listar_clientes, name='listar_clientes'),
    path('cliente/<int:id>', cliente_views.buscar_cliente_id, name='detalhes_cliente_id'),
    path('cliente/editar/<int:id>', cliente_views.editar_cliente, name='editar_cliente'),
    path('cliente/excluir/<int:id>', cliente_views.remover_cliente, name='remover_cliente'),
]