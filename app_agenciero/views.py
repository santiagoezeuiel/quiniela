from django.shortcuts import render
from .models import Agenciero
from .models import *

# Create your views here.


def home(request):
    
    return render(request, 'home/home.html',{
        'title' : 'Home',
    })


def lista_agenciero(request):

    agenciero = Agenciero.objects.all()

    return render(request, 'agenciero/lista.html', {
        'title' : 'Lista de agencieros',
        'agenciero' : agenciero,
    })

