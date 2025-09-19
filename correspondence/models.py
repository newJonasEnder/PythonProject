from django.db import models
from core.models import Base

class EMail(Base):
    address = models.CharField(max_length=100, verbose_name="E-Mail-Adresse")

    def __str__(self):
        return f"{self.address}"

    class Meta:
        abstract = True
        verbose_name = "E-Mail-Adresse"
        verbose_name_plural = "E-Mails-Adressen"

class PrivateEMail(EMail):
    person = models.ForeignKey("persons.Person", on_delete=models.PROTECT, related_name="private_email_address", verbose_name="Person")

    class Meta:
        verbose_name = "private E-Mail-Adresse"
        verbose_name_plural = "private E-Mail-Adressen"

class BusinessEMail(EMail):
    employee = models.ForeignKey("persons.Employee", on_delete=models.PROTECT, related_name="business_email_address", verbose_name="Mitarbeiter")

    class Meta:
        verbose_name = "geschäftliche E-Mail-Adresse"
        verbose_name_plural = "geschäftliche E-Mail-Adressen"

class PhoneNumber(Base):
    number = models.CharField(max_length=100, verbose_name="Telefonnummer")

    def __str__(self):
        return f"{self.number}"

    class Meta:
        abstract = True
        verbose_name = "Telefonnummer"
        verbose_name_plural = "Telefonnummern"

class PrivatePhoneNumber(PhoneNumber):
    person = models.ForeignKey("persons.Person", on_delete=models.PROTECT, related_name="private_phone_number")

    class Meta:
        verbose_name = "private Telefonnummer"
        verbose_name_plural = "private Telefonnummern"

class BusinessPhoneNumber(PhoneNumber):
    employee = models.ForeignKey("persons.Employee", on_delete=models.PROTECT, related_name="business_phone_number")

    class Meta:
        verbose_name = "geschäftliche Telefonnummer"
        verbose_name_plural = "geschäftliche Telefonnummern"