from django.db import models
from django.db.models import Q

from core.models import Base

#-----------------------------------------------------------------------------------------------------------------------

class Client(Base):
    private_client = models.OneToOneField("PrivateClient", on_delete=models.PROTECT)
    business_client = models.OneToOneField("BusinessClient", on_delete=models.PROTECT)
    orders = models.ManyToManyField("orders.Order", through="orders.OrderClient")
    class Meta:
        constraints = [models.CheckConstraint(check=((Q(private_client__isnull=True)&Q(business_client__isnull=False)) | (Q(private_client__isnull=False) & Q(business_client__isnull=True))), name="private_client_true_and_business_client_false_or_private_client_false_and_business_client_true")]
        verbose_name = "Kunde"
        verbose_name_plural = "Kunden"

class PrivateClient(Base):
    person = models.ForeignKey("persons.Person", on_delete=models.PROTECT)
    class Meta:
        verbose_name = "Privatkunde"
        verbose_name_plural = "Privatkunden"

class BusinessClient(Base):
    company = models.ForeignKey("companies.Company", on_delete=models.PROTECT)
    class Meta:
        verbose_name = "Geschäftskunde"
        verbose_name_plural = "Geschäftskunden"

#-----------------------------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------------------------

