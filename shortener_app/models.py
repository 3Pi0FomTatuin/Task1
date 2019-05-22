import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CASCADE


class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # To make it unguessable


class Shortening(models.Model):
    long_url = models.CharField(max_length=2048)  # 2048: https://stackoverflow.com/a/417184/8390594
    short_url = models.CharField(max_length=55)  # 55: len(ENCODER.encode_url(10**100))
    owner = models.ForeignKey(CustomUser, related_name='urls', on_delete=CASCADE, null=True)
