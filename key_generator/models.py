from django.db import models
from authentication.models import User


class GeneratedKey(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    access_key = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField()