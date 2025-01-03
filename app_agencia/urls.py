from django.urls import path
from . import views

urlpatterns = [
    path('lista_agencia', views.lista_agencia, name='lista_agencia'),
    path('detalle_agencias/<int:id>', views.detalle_agencias, name='detalle_agencias'),
]
