from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    fields = ['username', 'email', 'developer', 'public_entity', 'analyst', 'grann_pad']
admin.site.register(User, UserAdmin)