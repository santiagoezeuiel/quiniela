from django.shortcuts import render
from itertools import chain  #Para combinar consultar de django queryset
from .models import *

# Create your views here.

def lista_provincia(request):

    provincias = Provincia.objects.all()

    departamentos = Departamento.objects.all()

    localidades = Localidad.objects.all()

    return render(request, 'localidad/provincia.html', {
        'title' : 'Provincias',
        'provincias' : provincias,
        'departamentos' : departamentos,
        'localidades' : localidades,
    })


