from django.db import models

from core.models import Base

from datetime import date


class File(Base):
    number = models.PositiveIntegerField(unique=True, verbose_name="Nummer")
    parent = models.ForeignKey("File", on_delete=models.PROTECT, null=True, blank=True, related_name="parents", verbose_name="übergeordnete Datei")

    class Meta:
        ordering = ("number",)
        verbose_name = "Datei"
        verbose_name_plural = "Dateien"

    def __str__(self):
        return f"{self.number}"

class FileLog(Base):
    date = models.DateField(default=date.today, verbose_name="Datum")
    file = models.ForeignKey("File", on_delete=models.PROTECT, verbose_name="Datei")
    file_status = models.ForeignKey("FileStatus", on_delete=models.PROTECT, null=True, blank=True, verbose_name="Datei-Status")

    class Meta:
        ordering = ("date",)
        verbose_name = "Datei-Protokoll"
        verbose_name_plural = "Datei-Protokolle"

class FileStatus(Base):
    """A lookup table"""
    name = models.CharField(max_length=100, verbose_name="Status")

    class Meta:
        ordering = ("name",)
        verbose_name = "Datei-Status"
        verbose_name_plural = "Datei-Status"

    def __str__(self):
        return f"{self.name}"

# Create your models here.
