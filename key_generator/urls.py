
from django.contrib import admin
from django.urls import path
from .views import GenerateKeyView

urlpatterns = [
    path('keys', GenerateKeyView.as_view(), name='key-list')
]
