from django.shortcuts import render, get_object_or_404, redirect
from .models import *

# Create your views here.


def lista_agencia(request):

    agencias = Agencia.objects.all()

    return render(request, 'agencia/lista.html', {
        'title' : 'Lista de agencias',
        'agencias' : agencias,
    })


def detalle_agencias(request, id):

    agencieros = get_object_or_404(Agencia, pk=id)


    return render(request, 'agencia/agencias.html', {
        'title' : 'Agenciero',
        'agencieros' : agencieros,
    })