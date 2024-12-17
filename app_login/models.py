from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.models import Group, User



# Create your views here.


# crear login 

def crear_grupos():

    jefe_group,_ = Group.objects.get_or_create(name='Jefes')
    cajero_group,_ = Group.objects.get_or_create(name='Cajeros')
    agencieros_group,_ = Group.objects.get_or_create(name='Agencieros')




def user_login(request):


    form = AuthenticationForm()

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get('username')
            contraseña = form.cleaned_data.get('password')
            usuario = authenticate(username=nombre, password=contraseña)
            if usuario is not None:
                login(request, usuario)
                if request.user.groups.filter(name='Jefe_area').exists():
                    return render(request, 'home/home1.html')
                elif request.user.groups.filter(name='cajero').exists():
                    return render(request, 'home/home2.html')
                elif request.user.groups.filter(name='agenciero'). exists():
                    return render(request, 'home/home3.html')
            else:
                return render(request, 'home/home.html')
        else:
            messages.error(request, 'El susuario no es valido')  

    return render(request, 'home/home.html', {
        'title' : 'Login',
        'form' : form,
    })

def cerrar(request):

    logout(request)
    return redirect('user_login')