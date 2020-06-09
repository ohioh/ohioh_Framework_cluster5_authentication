
from django.urls import path
from .views import GenerateKeyView, GetUserAccessKeyView

urlpatterns = [
    path('keys/create', GenerateKeyView.as_view(), name='create-key'),
    path('keys/get', GetUserAccessKeyView.as_view(), name='get-key')
]
