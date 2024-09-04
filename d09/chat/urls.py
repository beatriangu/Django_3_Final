from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Página principal con la lista de salas de chat
    path('<str:room_name>/', views.room, name='room'),  # Ruta para las salas de chat específicas
]

