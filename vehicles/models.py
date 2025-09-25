from django.db import models

from datetime import date

from core.models import Base

from core.helper import get_year

from persons.models import Employee

from lookups.models import PoliticalMunicipality

class Car(Base):
    """A lookup table"""
    brand = models.CharField(max_length=100, verbose_name="Marke")
    license_plates = models.ManyToManyField("LicensePlate", through="CarLicensePlate", verbose_name="Kennzeichen")
    model = models.CharField(max_length=100, verbose_name="Model")
    vin = models.CharField(max_length=17, unique=True, verbose_name="FIN") # vehicle identification number



    class Meta:
        verbose_name = "Auto"
        verbose_name_plural = "Autos"

    def __str__(self):
        return f"{self.brand} {self.model}"

class LicensePlate(Base):
    """A lookup table"""
    registration = models.CharField(max_length=100, unique=True, verbose_name="Kennzeichen")
    cars = models.ManyToManyField("Car", through="CarLicensePlate", verbose_name="Autos")

    class Meta:
        verbose_name = "Kennzeichen"
        verbose_name_plural = "Kennzeichen"

    def __str__(self):
        return f"{self.registration}"

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
        verbose_name = "Fahrtprotokoll"
        verbose_name_plural = "Fahrtprotokolle"

class Trip(Base):
    #date = models.DateField(default=date.today, verbose_name="Datum")
    #car = models.ForeignKey("Car", on_delete=models.PROTECT, related_name="car_trips", verbose_name="Auto")
    driver = models.ForeignKey("persons.Employee", on_delete=models.PROTECT, related_name="driver_trips", verbose_name="Fahrer")
    start = models.ForeignKey("lookups.PoliticalMunicipality", on_delete=models.PROTECT, related_name="start_trips", verbose_name="Start")
    end = models.ForeignKey("lookups.PoliticalMunicipality", on_delete=models.PROTECT, related_name="end_trips", verbose_name="Ziel")

    class Meta:
        verbose_name = "Fahrt"
        verbose_name_plural = "Fahrten"

