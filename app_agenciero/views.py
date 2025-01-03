from django.shortcuts import render, get_object_or_404, redirect
from .models import Agenciero
from .models import *

# Create your views here.


def home(request):
    
    return render(request, 'home/home.html',{
        'title' : 'Home',
    })


def lista_agenciero(request):

    agencieros = Quinielero.objects.all()

    return render(request, 'agenciero/lista.html', {
        'title' : 'Lista de agencieros',
        'agencieros' : agencieros,
    })


def detalle_agenciero(request, id):

    agencieros = get_object_or_404(Quinielero, pk=id)


    return render(request, 'agenciero/agenciero.html', {
        'title' : 'Agenciero',
        'agencieros' : agencieros,
    })