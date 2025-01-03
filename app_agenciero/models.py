from django.db import models
from django.contrib.auth.models import User
from app_local.models import *
from django.core.validators import RegexValidator

# Create your models here.


class Genero(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Genero')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    updated = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de alta')

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return f"{self.nombre}"
    
class Tipo_telefono(models.Model):

    nombre = models.CharField(max_length=50, verbose_name='Tipo de telefono')
    created = models.DateTimeField(auto_created=True, verbose_name='Creado')
    updated = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de alta')

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return f"{self.nombre}"

class Agenciero(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuario')
    foto = models.ImageField(upload_to='agenciero', default='imagenes/user/user.png')
    dni = models.CharField(max_length=11, unique=True, validators=[RegexValidator(r'^\d+$'),], help_text='Introduzca el DNI:', verbose_name='D.N.I')
    cuil = models.CharField(max_length=14, unique=True, validators=[RegexValidator(r'^\d+$')], help_text='Introduzca en numero de C.U.I.L', verbose_name='C.U.I.L')
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, verbose_name='Genero')
    cbu = models.CharField(max_length=22, unique=True, validators=[RegexValidator(r'^\d{22}$')], help_text='Introduzca el numero de CBU maximo 22 dijitos', verbose_name='CBU')
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE, verbose_name='Provincia')
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, verbose_name='Departamento')
    localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE, verbose_name='Localidad')
    barrio = models.CharField(max_length=50, verbose_name='Nombre del Barrio')
    calle = models.CharField(max_length=50, verbose_name='Nombre de calle')
    n_casa = models.IntegerField(verbose_name='Numero de casa')

    class Meta:
         ordering = ('-id', 'user',)

    def __str__(self):
        return f"{self.user}"
    

class Quinielero(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, help_text='Nombre del agenciero')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:

        ordering = ('-id', 'user')

    def __str__(self):
        return f"{self.user}"