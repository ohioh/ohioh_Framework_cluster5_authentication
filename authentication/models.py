from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    developer = models.BooleanField(default=False)
    public_entity = models.BooleanField(default=False)
    analyst = models.BooleanField(default=False)
    grann_pad = models.BooleanField(default=False)
    permission_granted = models.BooleanField(default=False)
