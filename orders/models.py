from django.db import models
from core.models import Base
from datetime import date

from clients.models import Client

#-----------------------------------------------------------------------------------------------------------------------

class Order(Base):
    id = models.CharField(max_length=100, verbose_name="ID", null=True)
    date = models.DateField(default=date.today, verbose_name="Datum")
    file = models.ForeignKey("files.File", on_delete=models.PROTECT, related_name="file_orders", verbose_name="Geschäftsfall")
    clients = models.ManyToManyField("clients.Client", through="OrderClient", related_name="client_orders", verbose_name="Kunden")
    contacts = models.ManyToManyField("contacts.Contact", through="OrderContact", related_name="contact_orders", verbose_name="Kontakte")
    properties = models.ManyToManyField("properties.Property", through="OrderProperty", related_name="property_orders", verbose_name="Grundstücke")

    class Meta:
        verbose_name = "Auftrag"
        verbose_name_plural = "Aufträge"

class OrderContact(models.Model):
    order = models.ForeignKey("Order", on_delete=models.PROTECT)
    contact = models.ForeignKey("contacts.Contact", on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Auftrag-Kontakt-Beziehung"
        verbose_name_plural = "Auftrag-Kontakt-Beziehungen"

class OrderProperty(models.Model):
    order = models.ForeignKey("Order", on_delete=models.PROTECT, verbose_name="Auftrag")
    property = models.ForeignKey("properties.Property", on_delete=models.PROTECT, verbose_name="Grundstück")

#-----------------------------------------------------------------------------------------------------------------------

class OrderExtension(Base):
    order = models.OneToOneField("Order", on_delete=models.PROTECT, related_name="order_types", verbose_name="Auftrag")

    def __str__(self):
        return f"{self.order}"

    class Meta:
        abstract = True
        verbose_name = "Auftrag-Erweiterung"
        verbose_name_plural = "Auftrag-Erweiterungen"

class Division(OrderExtension):

    class Meta:
        verbose_name = "Teilung"
        verbose_name_plural = "Teilungen"

class OrderLog(Base):
    date = models.DateField(default=date.today, verbose_name="Datum")
    order = models.ForeignKey("Order", on_delete=models.PROTECT, verbose_name="Auftrag")
    order_status = models.ForeignKey("OrderStatus", on_delete=models.PROTECT, null=True, blank=True, verbose_name="Auftrag-Status")

    class Meta:
        ordering = ("date",)
        verbose_name = "Zustandsänderung"
        verbose_name_plural = "Zustandsänderungen"

class OrderStatus(Base):
    """A lookup table"""
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ("name",)
        verbose_name = "Auftrag-Status"
        verbose_name_plural = "Auftrag-Status"

    def __str__(self):
        return f"{self.name}"

class OrderType(Base):
    """A lookup table"""
    name = models.CharField(max_length=100, verbose_name="Name")

    class Meta:
        ordering = ("name",)
        verbose_name = "Auftrag-Art"
        verbose_name_plural = "Auftrag-Arten"

    def __str__(self):
        return f"{self.name}"

class OrderClient(Base):
    order = models.ForeignKey("orders.Order", on_delete=models.PROTECT, verbose_name="Auftrag")
    client = models.ForeignKey("clients.Client", on_delete=models.PROTECT, verbose_name="Kunde")

    def __str__(self):
        return f"{self.order}-{self.client}"

    class Meta:
        verbose_name = "Auftrag-Kunde-Zuordnung"
        verbose_name_plural = "Auftrag-Kunde-Zuordnungen"

class ConsentForm(Base):

    def __str__(self):
        return f"{self.id}"

    @property
    def amount_requests(self):
        return self.consent_form_requests.count()

    @property
    def amount_replies(self):
        return self.consent_form_replies.count()

    class Meta:
        verbose_name = "Zustimmung"
        verbose_name_plural = "Zustimmungen"

class ConsentFormRequests(Base):
    date = models.DateField(default=date.today, verbose_name="Datum")
    person = models.ForeignKey("persons.Person", on_delete=models.PROTECT, verbose_name="Person")
    consent_form = models.ForeignKey("ConsentForm", on_delete=models.PROTECT, related_name="consent_form_requests", verbose_name="Einverständnis")

    def __str__(self):
        return self.person

    class Meta:
        verbose_name = "Zustimmungserklärung-Anfrage"
        verbose_name_plural = "Zustimmungserklärung-Anfragen"

class ConsentFormReplies(Base):
    date = models.DateField(default=date.today, verbose_name="Datum")
    person = models.ForeignKey("persons.Person", on_delete=models.PROTECT, related_name="consent_form_replies", verbose_name="Person")
    consent_form = models.ForeignKey("ConsentForm",on_delete=models.PROTECT, related_name="consent_form_replies", verbose_name="Einverständnis")

    def __str__(self):
        return self.person

    class Meta:
        verbose_name = "Zustimmungserklärung-Antwort"
        verbose_name_plural = "Zustimmungserklärung-Antworten"