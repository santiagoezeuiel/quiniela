from django.contrib import admin
from .models import Agenciero
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


# Register your models here.


class UserProfileInline(admin.StackedInline):
    model = Agenciero
    can_delete = False
    verbose_name_plural = 'Perfiles de usuario'



class UserAdmin(BaseUserAdmin):
    inlines = [UserProfileInline]



admin.site.unregister(User)
admin.site.register(User, UserAdmin)