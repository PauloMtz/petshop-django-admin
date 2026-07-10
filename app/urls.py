from django.urls import path
from .views import cliente_views

urlpatterns = [
    path('cliente/cadastro', cliente_views.cadastrar_cliente, name='cadastrar_cliente'),
    path('cliente/lista', cliente_views.listar_clientes, name='listar_clientes'),
]