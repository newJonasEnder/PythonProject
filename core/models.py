from django.db import models
from uuid import uuid4

class Base(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True