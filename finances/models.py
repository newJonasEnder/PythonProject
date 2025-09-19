from django.db import models
from datetime import date
from core.models import Base
from core.defaults import Defaults

class Document(Base):
    external_id = models.IntegerField(null=True, blank=True, verbose_name="externe ID")
    date = models.DateField(default=date.today, verbose_name="Datum")
    net_amount = models.IntegerField(verbose_name="Nettobetrag", help_text="Nettobetrag in Cent")
    notes = models.TextField(verbose_name="Notizen")

    def __str__(self):
        return f"{self.internal_id}"

    @property
    def get_gross_amount(self):
        gross_amount = self.net_amount * Defaults.TAX_RATE
        return gross_amount

    class Meta:
        abstract = True
        verbose_name = "Dokument"
        verbose_name_plural = "Dokumente"

class Offer(Document):

    class Meta:
        verbose_name = "Angebot"
        verbose_name_plural = "Angebote"

class CounterOffer(Document):

    class Meta:
        verbose_name = "Gegenangebot"
        verbose_name_plural = "Gegenangebote"

class Contract(Document):

    @property
    def number_of_invoices(self):
        return self.invoice.count()

    def remaining_amount(self):
        amount = self.net_amount
        for invoice in self.invoice:
            amount = invoice.net_amount
        return amount

    class Meta:
        verbose_name = "Vertrag"
        verbose_name_plural = "Vertrage"

class Invoice(Base):
    date = models.DateField(default=date.today, verbose_name="Datum")
    receiver = models.ForeignKey("persons.Client", on_delete=models.PROTECT, related_name="receiver_invoice", verbose_name="Empfänger")
    orders = models.ManyToManyField("orders.Order", through="InvoiceOrder", related_name="orders_invoices", verbose_name="Aufträge")
    contract = models.ForeignKey("Contract", on_delete=models.PROTECT, related_name="contract_invoice", verbose_name="Vertrag")
    net_amount = models.IntegerField(verbose_name="Nettobetrag", help_text="Nettobetrag in Cent")

    def __str__(self):
        return f"{self.id}"

    @property
    def percentage(self):
        percentage = self.net_amount / self.contract.net_amount * 100
        return percentage

    class Meta:
        verbose_name = "Rechnung"
        verbose_name_plural = "Rechnungen"

class InvoiceOrder(Base):
    invoice = models.ForeignKey("Invoice", on_delete=models.PROTECT, verbose_name="Rechnung")
    order = models.ForeignKey("orders.Order", on_delete=models.PROTECT, verbose_name="Auftrag")

    def __str__(self):
        return f"{self.invoice}-{self.order}"

    class Meta:
        verbose_name = "Rechnung-Auftrag-Zuordnung"
        verbose_name_plural = "Rechnungen-Auftrag-Zuordnungen"

class BankAccount(Base):
    iban = models.CharField(verbose_name="IBAN")

    class Meta:
        ordering = ("iban",)
        verbose_name = "Bankverbindung"
        verbose_name_plural = "Bankverbindungen"

    def __str__(self):
        return f"{self.iban}"


class Payment(Base):
    date = models.DateField(default=date.today, verbose_name="Datum")
    amount = models.PositiveIntegerField(help_text="Betrag in Cent", verbose_name="Betrag")

    class Meta:
        ordering = ("date",)
        verbose_name = "Zahlung"
        verbose_name_plural = "Zahlungen"



