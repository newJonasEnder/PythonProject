from django.db import models

from core.models import Base

class Role(Base):
    """A lookup table"""
    name = models.CharField(max_length=100, verbose_name="Name")

    class Meta:
        verbose_name = "Rolle"
        verbose_name_plural = "Rollen"

    def __str__(self):
        return f"{self.name}"

class AcademicTitle(Base):
    abbreviation = models.CharField(max_length=100, verbose_name="Abkürzung")

    class Meta:
        ordering = ("abbreviation",)
        verbose_name = "akademischer Titel"
        verbose_name_plural = "akademische Titel"

    def __str__(self):
        return f"{self.abbreviation}"



class AdminUnit(Base):
    """A lookup table"""
    name = models.CharField(max_length=100, verbose_name="Name")

    class Meta:
        abstract = True
        ordering = ("name",)
        verbose_name = "Verwaltungseinheit"
        verbose_name_plural = "Verwaltungsebenen"

    def __str__(self):
        return f"{self.name}"

class PoliticalMunicipality(AdminUnit):
    """A lookup table"""

    class Meta:
        verbose_name = "Gemeinde"
        verbose_name_plural = "Gemeinden"

class CadastralMunicipality(AdminUnit):
    """A lookup table"""
    political_municipality = models.ForeignKey("PoliticalMunicipality", on_delete=models.PROTECT, verbose_name="politische Gemeinde")

    class Meta:
        verbose_name = "Katastralgemeinde"
        verbose_name_plural = "Katastralgemeinden"

class District(AdminUnit):
    """A lookup table"""
    state = models.ForeignKey("State", on_delete=models.PROTECT, null=True, verbose_name="Bundesland")

    class Meta:
        verbose_name = "Bezirk"
        verbose_name_plural = "Bezirke"

class State(AdminUnit):
    """A lookup table"""
    country = models.ForeignKey("Country", on_delete=models.PROTECT, verbose_name="Land")

    class Meta:
        verbose_name = "Bundesland"
        verbose_name_plural = "Bundesländer"

class Country(AdminUnit):
    """A lookup table"""

    class Meta:
        verbose_name = "Land"
        verbose_name_plural = "Länder"

class WorkType(Base):
    """A lookup table"""
    name = models.CharField(max_length=100, verbose_name="Name")

    class Meta:
        ordering = ("name",)
        verbose_name = "Arbeit-Art"
        verbose_name_plural = "Arbeit-Arten"

    def __str__(self):
        return f"{self.name}"

class Office(Base):
    """A lookup table"""
    address = models.ForeignKey("georeferenced_data.Address", on_delete=models.PROTECT, verbose_name="Adresse")

    class Meta:
        verbose_name = "Büro"
        verbose_name_plural = "Büros"

    def __str__(self):
        return f"{self.address.street}"


class Gender(Base):
    """A lookup table"""
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Geschlecht"
        verbose_name_plural = "Geschlechter"

    def __str__(self):
        return f"{self.name}"


# Create your models here.
