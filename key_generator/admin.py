from django.contrib import admin
from .models import GeneratedKey


class GeneratedKeyAdmin(admin.ModelAdmin):
    list_display = ['user', 'access_key', 'created_at', 'last_update']
    search_fields = ('access_key', )
admin.site.register(GeneratedKey, GeneratedKeyAdmin)
