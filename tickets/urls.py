from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_tickets, name='listar_tickets'),
    path('crear/', views.crear_ticket, name='crear_ticket'),
    path('editar/<int:pk>/', views.editar_ticket, name='editar_ticket'),
    path('eliminar/<int:pk>/', views.eliminar_ticket, name='eliminar_ticket'),
]