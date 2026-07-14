from django.urls import path

from app.views import consulta_views, pet_views
from .views import cliente_views

urlpatterns = [
    # Rotas de clientes
    path('cliente/cadastro', cliente_views.cadastrar_cliente, name='cadastrar_cliente'),
    path('cliente/lista', cliente_views.listar_clientes, name='listar_clientes'),
    path('cliente/<int:id>', cliente_views.buscar_cliente_id, name='detalhes_cliente_id'),
    path('cliente/editar/<int:id>', cliente_views.editar_cliente, name='editar_cliente'),
    path('cliente/excluir/<int:id>', cliente_views.remover_cliente, name='remover_cliente'),
    # Rotas de pets
    path('pet/cadastro/<int:id>', pet_views.inserir_pet, name='cadastrar_pet'),
    path('pet/<int:id>', pet_views.buscar_pet_id, name='buscar_pet_id'),
    # Rotas de consultas
    path('consulta/cadastro/<int:id>', consulta_views.inserir_consulta, name='cadastrar_consulta'),
    path('consulta/<int:id>', consulta_views.buscar_consulta_id, name='buscar_consulta_id'),
]