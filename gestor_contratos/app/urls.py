from django.urls import path
from .views.contrato_views import *
from .views.usuario_views import *

urlpatterns = [
    path('', logar_usuario, name='logar_usuario'),
    path('listar_contratos/', listar_contratos, name='listar_contratos'),
    path('cadastrar_contrato/', cadastrar_contrato, name='cadastrar_contrato'),
    path('editar_contrato/<int:id>', editar_contrato, name='editar_contrato'),
    path('remover_contrato/<int:id>', remover_contrato, name='remover_contrato'),
    path('cadastrar_usuario/', cadastrar_usuario, name='cadastrar_usuario'),
    path('logar_usuario/', logar_usuario, name='logar_usuario'),
    path('deslogar_usuario/', deslogar_usuario, name='deslogar_usuario'),
]
