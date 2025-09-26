from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Q

from core.models import Base

class Client(Base):
    private_client = models.OneToOneField("PrivateClient", on_delete=models.PROTECT, null=True, blank=True, verbose_name="Privatkunde")
    business_client = models.OneToOneField("BusinessClient", on_delete=models.PROTECT, null=True, blank=True, verbose_name="Geschäfstkunde")
    orders = models.ManyToManyField("orders.Order", through="orders.OrderClient")

    def __str__(self):
        if self.private_client:
            return f"{self.private_client.person}"
        elif self.business_client:
            return f"{self.business_client.company}"
        else:
            return f"{self.uuid}"

    def clean(self):
        super().clean()
        if self.private_client and self.business_client:
            raise ValidationError("Privatkunde und Geschäftskunde dürfen nicht gleichzeitig ausgewählt sein")
        elif not self.private_client and not self.business_client:
            raise ValidationError("Entweder Privatkunde und Geschäftskunde müssen ausgewählt sein")

    class Meta:
        constraints = [models.CheckConstraint(check=((Q(private_client__isnull=True)&Q(business_client__isnull=False)) | (Q(private_client__isnull=False) & Q(business_client__isnull=True))), name="private_client_true_and_business_client_false_or_private_client_false_and_business_client_true")]
        verbose_name = "Kunde"
        verbose_name_plural = "Kunden"

class PrivateClient(Base):
    person = models.ForeignKey("persons.Person", on_delete=models.PROTECT, verbose_name="Person")

    def __str__(self):
        return f"{self.person}"

    class Meta:
        verbose_name = "Privatkunde"
        verbose_name_plural = "Privatkunden"

class BusinessClient(Base):
    company = models.ForeignKey("companies.Company", on_delete=models.PROTECT, verbose_name="Firma")

    def __str__(self):
        return f"{self.company}"

    class Meta:
        verbose_name = "Geschäftskunde"
        verbose_name_plural = "Geschäftskunden"
