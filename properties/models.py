from django.db import models

class Owner(models.Model):
    person = models.OneToOneField("persons.Person", on_delete=models.PROTECT, related_name="person_owner", verbose_name="Person")
    company = models.OneToOneField("companies.Company", on_delete=models.PROTECT, related_name="company_owner", verbose_name="Firma")
    properties = models.ManyToManyField("Property", through="Ownership", related_name="property_owners", verbose_name="Grundstück")

    def __str__(self):
        if self.person:
            return self.person
        elif self.company:
            return self.company
        else:
            return None

    class Meta:
        verbose_name = "Besitzer"
        verbose_name_plural = "Besitzer"

class Property(models.Model):
    number = models.IntegerField(verbose_name="Nummer")
    owners = models.ManyToManyField("Owner", through="Ownership", related_name="owner_properties", verbose_name="Besitzer")
    order = models.ManyToManyField("orders.Order", through="orders.OrderProperty", related_name="order_properties", verbose_name="Aufträge")

    def __str__(self):
        return f"{self.number}"

    class Meta:
        verbose_name = "Grundstück"
        verbose_name_plural = "Grundstücke"

class Ownership(models.Model):
    owner = models.ForeignKey("Owner", on_delete=models.PROTECT)
    property = models.ForeignKey("Property", on_delete=models.PROTECT)
    numerator = models.IntegerField()
    denominator = models.IntegerField()
