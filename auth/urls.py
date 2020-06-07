from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/authentication/', include('authentication.urls')),
    path('api/v1/key-generator/', include('key_generator.urls'))
]
