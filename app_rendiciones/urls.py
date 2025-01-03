from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', views.lista_rendicion, name='lista_rendicion'),
    path('crear_rendicion/', views.crear_rendicion, name='crear_rendicion'),
]
