from django.contrib import admin
from .models import *

# Register your models here.

class ProvinciaAdmin(admin.ModelAdmin):

    list_display = ('id', 'nombre', 'created')
    list_filter = ('nombre',)
    search_fields = ('nombre',)
    readonly_fields = ('created', 'updated',)


class DepartamentoAdmin(admin.ModelAdmin):

    list_display = ('id', 'nombre', 'provincia', 'created')
    list_filter = ('nombre',)
    search_fields = ('nombre', 'provincia',)
    readonly_fields = ('created', 'updated',)

class LocalidadAdmin(admin.ModelAdmin):

    list_display = ('id', 'nombre', 'departamento', 'created',)
    list_filter = ('nombre',)
    search_fields = ('nombre',)
    readonly_fields = ('created', 'updated',)


admin.site.register(Provincia, ProvinciaAdmin)
admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(Localidad, LocalidadAdmin)