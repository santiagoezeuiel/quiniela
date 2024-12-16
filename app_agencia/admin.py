from django.contrib import admin
from .models import *

# Register your models here.


class ActivoAdmin(admin.ModelAdmin):

    list_display = ('id', 'nombre', 'created',)
    list_filter = ('id',)
    search_fields = ('id',)
    readonly_fields = ('created', 'updated',)

class AgenciaAdmin(admin.ModelAdmin):

    list_display = ('id', 'user', 'created',)
    list_filter = ('id', 'user',)
    search_fields = ('id',)
    readonly_fields = ('created', 'updated')


admin.site.register(Activo, ActivoAdmin)
admin.site.register(Agencia, AgenciaAdmin)