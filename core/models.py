from django.db import models
from uuid import uuid4

class Base(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False, verbose_name="UUID")
    active = models.BooleanField(default=True, verbose_name="aktiv")
    created_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name="erstellt am")
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name="verändert am")

    class Meta:
        abstract = True