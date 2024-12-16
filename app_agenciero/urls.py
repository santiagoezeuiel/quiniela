from django.urls import path
from . import views

urlpatterns = [
    path('', views.agenciero, name='lista'),
]
