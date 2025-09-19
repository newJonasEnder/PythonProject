from django.db import models
from core.models import Base

class Property(Base):
    number = models.IntegerField(verbose_name="Nummer")
    owners = models.ManyToManyField("PropertyOwner",
                                    related_name="owners_properties",
                                    verbose_name="Besitzer")

    class Meta:
        verbose_name = "Grundstück"
        verbose_name_plural = "Grundstücke"

    def __str__(self):
        return f"{self.number}"

class PropertyOwner(Base):
    person = models.OneToOneField("persons.Person",
                                  on_delete=models.CASCADE,
                                  related_name="person_property_owner",
                                  verbose_name="Person")
    properties = models.ManyToManyField("Property",
                                        related_name="properties_owners",
                                        verbose_name="Grundstück")

    class Meta:
        verbose_name = "Grundstückseigentümer"
        verbose_name_plural = "Grundstückseigentümer"

    def __str__(self):
        return self.person

class PropertyPropertyOwner(Base):
    property = models.ForeignKey("Property",
                                 on_delete=models.PROTECT,
                                 verbose_name="Grundstück")
    property_owner = models.ForeignKey("PropertyOwner",
                                       on_delete=models.PROTECT,
                                       verbose_name="Grundstücksbesitzer")
    ...


    class Meta:
        verbose_name = "Grundstück-Grundstücksbesitzer-Zuordnung"
        verbose_name_plural = "Grundstück-Grundstückbesitzer-Zuordnung"

# Create your models here.
