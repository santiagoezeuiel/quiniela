from django.contrib import admin
from .models import *

# Register your models here.


class CajeroAdmin(admin.ModelAdmin):

    list_display = ('id', 'numero_caja', 'created')
    list_filter = ('id', 'numero_caja')
    search_fields = ('numero_caja', 'user')
    readonly_fields = ('created', 'updated')




admin.site.register(Cajero, CajeroAdmin)