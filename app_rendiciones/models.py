from django.db import models
from django.contrib.auth.models import User
from app_agencia.models import Agencia

# Create your models here.


class Rendicion(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario')
    agencia = models.ForeignKey(Agencia, on_delete=models.CASCADE, verbose_name='Numero de agencia')
    imagen = models.ImageField(upload_to='Rendicion/', verbose_name='Comprobante')
    monto = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Monto')
    n_comprobante = models.PositiveBigIntegerField(verbose_name='Numuro de comprobante')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.agencia}'

    class Meta:
        ordering = ('-id', '-created')

