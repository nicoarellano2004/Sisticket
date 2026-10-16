from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_tickets, name='listar_tickets'),
    path('crear/', views.crear_ticket, name='crear_ticket'),
]