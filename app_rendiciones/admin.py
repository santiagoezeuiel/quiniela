from django.contrib import admin
from .models import *


# Register your models here.


class RendicionAdmin(admin.ModelAdmin):

    list_display = ('id', 'user', 'agencia')
    list_filter = ('user', 'agencia')
    search_fields = ('user', 'agencia')
    readonly_fields = ('created', 'updated')



admin.site.register(Rendicion, RendicionAdmin)