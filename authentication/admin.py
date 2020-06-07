from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'developer', 'public_entity', 'analyst', 'grann_pad', 'permission_granted']
    search_fields = ('username', 'email', )
    list_filter = ['permission_granted', 'developer', 'public_entity', 'analyst', 'grann_pad']
admin.site.register(User, UserAdmin)