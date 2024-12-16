from django.shortcuts import render
from .models import Agenciero
from .models import *

# Create your views here.


def agenciero(request):

    agenciero = Agenciero.objects.all()

    return render(request, 'agenciero/lista.html', {
        'title' : 'Lista de agencieros',
        'agenciero' : agenciero,
    })

