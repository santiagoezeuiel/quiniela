from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import *
from .models import *

# Create your views here.



def lista_rendicion(request):

    rendicion = Rendicion.objects.all()

    return render(request, 'rendicion/lista.html', {
        'title' : 'Lista de rendicion',
        'rendicion' : rendicion,
    })


def crear_rendicion(request):
    if request.method == 'POST':
        form = FormularioRendicion(request.POST, request.FILES)
        if form.is_valid():
            new_form = form.save(commit = False)
            new_form.user_id = request.user.id
            new_form.save()
            messages.success(request, 'La rendicion fue agregada exitosamente')
            return redirect('lista_rendicion')
        else:
            print(form.errors)
    else:
        form = FormularioRendicion()
    return render (request, 'rendicion/formulario.html', {
        'title' : 'Formulario de rendicion',
        'form' : form,
    })