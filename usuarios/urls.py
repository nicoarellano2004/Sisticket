from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_usuarios, name='listar_usuarios'),
    path('crear/', views.crear_usuario, name='crear_usuario'),
    path('perfil/<int:pk>/', views.perfil_usuario, name='perfil_usuario'),
    path('crear_rol/', views.crear_rol, name='crear_rol'),
]