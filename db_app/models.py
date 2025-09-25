from django.db import models
from datetime import date
from uuid import uuid4
from django.core.exceptions import ValidationError
from .defaults import DEFAULT_STATE_UUID, DEFAULT_OFFICE_UUID, DEFAULT_COUNTRY_UUID
from django.contrib.gis.db import models

from core.models import Base

"""class AddressPerson(Base):
    address = models.ForeignKey("Address", on_delete=models.PROTECT, verbose_name="Adresse")
    person = models.ForeignKey("Person", on_delete=models.PROTECT, verbose_name="Person")

    care_of_person = models.ForeignKey("Person", on_delete=models.PROTECT, null=True, blank=True, related_name="care_of", verbose_name="c/o (Person)")
    care_of_company = models.ForeignKey("Firma", on_delete=models.PROTECT, null=True, blank=True, related_name="care_of_person", verbose_name="c/o (Firma)")

    class Meta:
        ordering = ("address",)
        verbose_name = "Adresse-Person-Zuordnung"
        verbose_name_plural = "Adresse-Person-Zuordnungen"

    def get_address(self) -> list[str]:
        address: list[str] = [f"{self.person}", f"{self.address.street}", f"{self.address.door}", f"{self.address.zipcode}", f"{self.address.city}", f"{self.address.state}", f"{self.address.country}"]
        if self.care_of_person:
            address.append(f"{self.care_of_person}") # calls the "__str__" method from "Person"
        elif self.care_of_company:
            address.append(f"{self.care_of_company}") # calls the "__str__" method from "Person"
        return address"""

"""class AddressCompany(Base):
    address = models.ForeignKey("Address", on_delete=models.PROTECT, verbose_name="Adresse")
    company = models.ForeignKey("Person", on_delete=models.PROTECT, verbose_name="Firma")
    for_the_attention_of_person = models.ForeignKey("Person", on_delete=models.PROTECT, null=True, blank=True, verbose_name="FOA (Person)")
    for_the_attention_of_department = models.ForeignKey("Department", on_delete=models.PROTECT, null=True, blank=True, verbose_name="FOA (Abteilung)")
    care_of_person = models.ForeignKey("Person", on_delete=models.PROTECT, null=True, blank=True, verbose_name="c/o (Person)")
    care_of_company = models.ForeignKey("Firma", on_delete=models.PROTECT, null=True, blank=True, verbose_name="c/o (Firma)")

    class Meta:
        verbose_name = "Adresse-Firma-Zuordnung"
        verbose_name_plural = "Adresse-Firma-Zuordnungen"""""



"""class WorkLog(Base):
    date = models.DateField(default=date.today, verbose_name="Datum")
    duration = models.DurationField(verbose_name="Dauer")
    employee = models.ForeignKey("persons.employee", on_delete=models.PROTECT, related_name="works", null=True, blank=True, verbose_name="interner Mitarbeiter")
    #work_type = models.ForeignKey("WorkType", on_delete=models.PROTECT, related_name="works", null=True, blank=True, verbose_name="Arbeit-Art")
    order = models.ForeignKey("orders.Order", on_delete=models.PROTECT, related_name="works", verbose_name="Auftrag")

    class Meta:
        ordering = ("date",)
        verbose_name = "Arbeit-Protokoll"
        verbose_name_plural = "Arbeit-Protokolle"""


