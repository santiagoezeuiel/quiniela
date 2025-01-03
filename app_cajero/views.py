from django.shortcuts import render, get_object_or_404, redirect
from .models import *



# Create your views here.


def lista_cajero(request):

    cajeros = Cajero.objects.all()

    return render(request, 'cajero/lista.html', {
        'title' : 'Lista de cajeros',
        'cajeros' : cajeros,
    })


def detalle_cajero(request, id):

    cajeros = get_object_or_404(Cajero, pk=id)

    return render(request, 'cajero/cajero.html', {
        'title' : 'Cajero',
        'cajeros' : cajeros,
    })