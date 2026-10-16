from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_mantenciones, name='listar_mantenciones'),
    path('crear/', views.crear_mantencion, name='crear_mantencion'),
]