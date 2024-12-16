from django.db import models
from django.contrib.auth.models import User
from app_local.models import Provincia, Departamento, Localidad

# Create your models here.

class Activo(models.Model):

    nombre = models.CharField(max_length=50, default='Activo', verbose_name='Estado de la agencia')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    updated = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de alta')

    class Meta:
        ordering = ('id',)
    
    def __str__(self):

        return f"{self.nombre}"


class Agencia(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    n_agencia = models.IntegerField(verbose_name='Numero de agencia')
    estado = models.ForeignKey(Activo, on_delete=models.CASCADE, verbose_name='Estado de la agencia')
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE, verbose_name='Provincia')
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, verbose_name='Departamento')
    localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE, verbose_name='Localidad')
    barrio = models.CharField(max_length=50, verbose_name='Barrio')
    n_casa = models.IntegerField(verbose_name='Numero de casa')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    updated = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de alta')

    class Meta:

        ordering = ('id', 'n_agencia')

    def __str__(self):

        return f"{self.n_agencia}"
    



