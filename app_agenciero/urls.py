from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('lista_agencieros', views.lista_agenciero, name='lista_agenciero'),
    path('lista_agenciero/<int:id>', views.detalle_agenciero, name='detalle_agenciero'),
]
