from django.db import models

# Create your models here.



class Provincia (models.Model):

    nombre = models.CharField(max_length=50, verbose_name='Provincia')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    updated = models.DateTimeField(auto_created=True, verbose_name='Fecha de alta')

    class Meta:
        ordering = ('id', 'nombre')
    
    def __str__(self):

        return f"{self.nombre}"
    
class Departamento(models.Model):

    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE, verbose_name='Provincia')
    nombre = models.CharField(max_length=50, verbose_name='Departamento')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    updated = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de alta')
    
    class Meta:
        ordering = ('id', 'provincia')

    def __str__(self):
        
        return f"{self.nombre}"
    
class Localidad(models.Model):

    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, verbose_name='Departamento')
    nombre = models.CharField(max_length=50, verbose_name='Localidad')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    updated = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de alta')

    class Meta:
        ordering = ('id', 'departamento')

    def __str__(self):

        return f"{self.nombre}"