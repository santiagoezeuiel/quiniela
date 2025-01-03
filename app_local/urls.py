from django.urls import path
from . import views

urlpatterns = [
    path('lista_provincia', views.lista_provincia, name='lista_provincia'),
]
