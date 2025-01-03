from django.contrib import admin
from .models import Agenciero, Genero,  Tipo_telefono, Quinielero
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


# Register your models here.

class GeneroAdmin(admin.ModelAdmin):
    
    list_display = ('id', 'nombre', 'created')
    list_filter = ('nombre', )
    search_fields = ('nombre', 'id')
    readonly_fields = ('created', 'updated')

class Tipo_telefonoAdmin(admin.ModelAdmin):
    
    list_display = ('id', 'nombre', 'created')
    list_filter = ('id', 'nombre')
    search_fields = ('nombre',)
    readonly_fields = ('created', 'updated')

class QuinieleroAdmin(admin.ModelAdmin):

    list_display = ('id', 'user', 'created')
    list_filter = ('user', )
    search_fields = ('user', )
    readonly_fields = ('created', 'updated')


class UserProfileInline(admin.StackedInline):
    model = Agenciero
    can_delete = False
    verbose_name_plural = 'Perfiles de usuario'



class UserAdmin(BaseUserAdmin):
    inlines = [UserProfileInline]



admin.site.register(Quinielero, QuinieleroAdmin)
admin.site.register(Tipo_telefono, Tipo_telefonoAdmin)
admin.site.register(Genero, GeneroAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)