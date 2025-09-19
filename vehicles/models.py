from django.db import models

from datetime import date

from core.models import Base

from core.helper import return_current_year

from persons.models import Employee

from lookups.models import PoliticalMunicipality

class Car(Base):
    """A lookup table"""
    brand = models.CharField(max_length=100, verbose_name="Marke")
    model = models.CharField(max_length=100, verbose_name="Model")
    year_of_manufacture = models.PositiveIntegerField(default=return_current_year, verbose_name="Baujahr")
    vin = models.CharField(max_length=17, unique=True, null=True, blank=True, verbose_name="FIN") # vehicle identification number
    license_plates = models.ManyToManyField("LicensePlate", through="CarLicensePlate", verbose_name="Kennzeichen")

    class Meta:
        verbose_name = "Auto"
        verbose_name_plural = "Autos"

    def __str__(self):
        return f"{self.brand} {self.model}"

class LicensePlate(Base):
    """A lookup table"""
    license_plate = models.CharField(max_length=100, unique=True, verbose_name="Kennzeichen")
    cars = models.ManyToManyField("Car", through="CarLicensePlate", verbose_name="Autos")

    class Meta:
        verbose_name = "Kennzeichen"
        verbose_name_plural = "Kennzeichen"

    def __str__(self):
        return f"{self.license_plate}"

class CarLicensePlate(Base):
    car = models.ForeignKey(Car, on_delete=models.PROTECT, verbose_name="Auto")
    license_plate = models.ForeignKey("LicensePlate", on_delete=models.PROTECT, verbose_name="Kennzeichen")
    date_of_registration = models.DateField(default=date.today, verbose_name="Datum")

    class Meta:
        unique_together = ("car", "license_plate")
        verbose_name = "Auto-Kennzeichen-Zuordnung"
        verbose_name_plural = "Auto-Kennzeichen-Zuordnungen"

class CarLog(Base):
    date = models.DateField(default=date.today, verbose_name="Datum")
    car = models.ForeignKey("Car", on_delete=models.PROTECT, verbose_name="Auto")
    mileage = models.PositiveIntegerField(verbose_name="Kilometerstand")

    class Meta:
        verbose_name = "Auto-Protokoll"
        verbose_name_plural = "Auto-Protokolle"

class Trip(Base):
    date = models.DateField(default=date.today, verbose_name="Datum")
    car = models.ForeignKey("Car", on_delete=models.PROTECT, related_name="trips", verbose_name="Auto")
    driver = models.ForeignKey("persons.Employee", on_delete=models.PROTECT, related_name="trips", verbose_name="Fahrer")
    start = models.ForeignKey("lookups.PoliticalMunicipality", on_delete=models.PROTECT, related_name="trips_starting", verbose_name="Start")
    end = models.ForeignKey("lookups.PoliticalMunicipality", on_delete=models.PROTECT, related_name="trips_ending", verbose_name="Ziel")

    class Meta:
        ordering = ("date",)
        verbose_name = "Fahrt"
        verbose_name_plural = "Fahrten"

