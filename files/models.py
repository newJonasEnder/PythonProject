from django.db import models

from datetime import date

from core.models import Base

from django.core.exceptions import ValidationError

class File(Base):
    date = models.DateField(default=date.today, verbose_name="Datum")
    number = models.CharField(verbose_name="Geschäftszahl")
    parent_file = models.ForeignKey("File", on_delete=models.PROTECT, null=True, blank=True, related_name="parent_file_child_files", verbose_name="Vorakt")

    def __str__(self):
        return f"{self.number}"

    def clean(self):
        super().clean()
        if self.parent_file and self.parent_file.uuid == self.uuid:
            raise ValidationError("Vorakt und Akt dürfen nicht identisch sein.")

    class Meta:
        verbose_name = "Akt"
        verbose_name_plural = "Akte"

class FileLog(Base):
    date = models.DateField(default=date.today, verbose_name="Datum")
    file = models.ForeignKey("File", on_delete=models.PROTECT, verbose_name="Datei")
    file_status = models.ForeignKey("FileStatus", on_delete=models.PROTECT, null=True, blank=True,
                                    verbose_name="Status")

    def __str__(self):
        return f"{self.date}"

    class Meta:
        ordering = ("date",)
        verbose_name = "Zustandsänderung"
        verbose_name_plural = "Zustandsänderungen"

class FileStatus(Base):
    """A lookup table"""
    name = models.CharField(max_length=100, verbose_name="Name")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ("name",)
        verbose_name = "Zustand"
        verbose_name_plural = "Zustände"

class FileNote(Base):
    date = models.DateField(default=date.today, verbose_name="Datum")
    file = models.ForeignKey("File", on_delete=models.PROTECT, related_name="file_file_notes", verbose_name="Akt")
    note = models.TextField(verbose_name="Notiz")

    def __str__(self):
        return f"{self.file}"

    class Meta:
        verbose_name = "Notiz"
        verbose_name_plural = "Notizen"