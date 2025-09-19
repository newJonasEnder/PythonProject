#from django.contrib.gis.db import models

#from core.models import Base

from django.core.exceptions import ValidationError

#class Place(Base):
    #point = models.PointField(geography=True, verbose_name="Standort")

    #def __str__(self):
        #return self.coordinates

    #@property
    #def coordinates(self):
        #return f"{self.point.x}, {self.point.y}"

    #class Meta:
        #verbose_name = "Ort"
        #verbose_name_plural = "Orte"

from django.db import models

from core.models import Base


class Address(Base):
    street = models.CharField(max_length=100,
                              verbose_name="Straße")
    door = models.CharField(max_length=100,
                            verbose_name="Tür")
    zipcode = models.CharField(max_length=10,
                               null=True,
                               verbose_name="Postleitzahl")
    city = models.CharField(max_length=100,
                            null=True,
                            verbose_name="Stadt")
    state = models.ForeignKey("lookups.State",
                              null=True,
                              on_delete=models.PROTECT,
                              #default=DEFAULT_STATE_UUID,
                              related_name="state_address",
                              verbose_name="Bundesland")
    country = models.ForeignKey("lookups.Country",
                                null=True,
                                on_delete=models.PROTECT,
                                related_name="country_address",
                                #default=DEFAULT_COUNTRY_UUID,
                                verbose_name="Land")

    person = models.ManyToManyField("persons.Person",
                                    through="AddressPerson",
                                    blank=True,
                                    related_name="persons_addresses",
                                    verbose_name="Person")
    company = models.ManyToManyField("persons.Company",
                                     related_name="companies_addresses",
                                     through="AddressCompany",
                                     blank=True,
                                    verbose_name="Firma")

    def clean(self):
        super().clean()
        if self.person and self.company:
            raise ValidationError("Bitte entweder Person oder Firma eingeben, nicht beides.")

    class Meta:
        verbose_name = "Adresse"
        verbose_name_plural = "Adressen"

class AddressPerson(Base):
    person = models.ForeignKey("persons.Person",
                                    on_delete=models.PROTECT,
                                    related_name="addresses",
                                    blank=True,
                                    verbose_name="Person")
    address = models.ForeignKey("Address", on_delete=models.PROTECT, blank=True, verbose_name="Adresse")

    def __str__(self):
        return f"{self.street}"

    class Meta:
        verbose_name = "Adresse-Person-Zuordnung"
        verbose_name_plural = "Adresse-Person-Zuordnungen"


class AddressCompany(Base):
    company = models.ForeignKey("persons.Company",
                               on_delete=models.PROTECT,
                               related_name="addresses",
                               blank=True,
                               verbose_name="Firma")
    address = models.ForeignKey("Address", on_delete=models.PROTECT, blank=True, verbose_name="Adresse")

    def __str__(self):
        return f"{self.street}"

    class Meta:
        verbose_name = "Adresse-Person-Zuordnung"
        verbose_name_plural = "Adresse-Person-Zuordnungen"