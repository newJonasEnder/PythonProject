from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    uid = models.CharField(max_length=100, null=True, blank=True, verbose_name="UID")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Firma"
        verbose_name_plural = "Firmen"
