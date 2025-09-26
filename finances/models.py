"""from datetime import date
from django.db import models
#-----------------------------------------------------------------------------------------------------------------------
from core.models import Base
from core.defaults import Defaults
#-----------------------------------------------------------------------------------------------------------------------
class BankAccount(Base):
    companies = models.ManyToManyField("companies.Company", related_name="company_bank_accounts",
                                       blank=True, verbose_name="Firmen")
    iban = models.CharField(verbose_name="IBAN")
    internal_employee = models.ManyToManyField("persons.InternalEmployee", related_name="person_bank_accounts", blank=True,
                                     verbose_name="Personen")

    def __str__(self):
        return f"{self.iban}"

    class Meta:
        ordering = ("iban",)
        verbose_name = "Bankverbindung"
        verbose_name_plural = "Bankverbindungen"
#-----------------------------------------------------------------------------------------------------------------------
class FinanceBase(Base):
    date = models.DateField(default=date.today, verbose_name="Datum")
    external_id = models.IntegerField(null=True, blank=True, verbose_name="externe ID")
    net_amount = models.IntegerField(verbose_name="Nettobetrag", help_text="Nettobetrag in Cent")
    notes = models.TextField(verbose_name="Notizen")

    @property
    def get_gross_amount(self):
        gross_amount = self.net_amount * Defaults.TAX_RATE
        return gross_amount

    class Meta:
        abstract = True


    @property
    def number_of_invoices(self):
        return self.contract_invoices.count()

    @property
    def remaining_amount(self):
        amount = self.net_amount
        for invoice in self.contract_invoices.all():
            amount = invoice.net_amount
        return amount

    class Meta:
        verbose_name = "Auftrag"
        verbose_name_plural = "Aufträge"
#-----------------------------------------------------------------------------------------------------------------------
class CounterOffer(Base):
    class Meta:
        verbose_name = "Gegenangebot"
        verbose_name_plural = "Gegenangebote"
#-----------------------------------------------------------------------------------------------------------------------
class Invoice(Base):
    date = models.DateField(default=date.today, verbose_name="Datum")
    receiver = models.ForeignKey("clients.Client", on_delete=models.PROTECT, related_name="receiver_invoice",
                                 verbose_name="Empfänger")
    orders = models.ManyToManyField("orders.Order", through="InvoiceOrder", related_name="orders_invoices",
                                    verbose_name="Aufträge")
    net_amount = models.IntegerField(verbose_name="Nettobetrag", help_text="Nettobetrag in Cent")

    @property
    def percentage(self):
        percentage = self.net_amount / self.contract.net_amount * 100
        return percentage

    class Meta:
        verbose_name = "Rechnung"
        verbose_name_plural = "Rechnungen"
#-----------------------------------------------------------------------------------------------------------------------
class InvoiceOrder(Base):
    invoice = models.ForeignKey("Invoice", on_delete=models.PROTECT, verbose_name="Rechnung")
    order = models.ForeignKey("orders.Order", on_delete=models.PROTECT, verbose_name="Auftrag")

    def __str__(self):
        return f"{self.invoice}-{self.order}"

    class Meta:
        verbose_name = "Rechnung-Auftrag-Zuordnung"
        verbose_name_plural = "Rechnungen-Auftrag-Zuordnungen"
#-----------------------------------------------------------------------------------------------------------------------
class Offer(FinanceBase):
    class Meta:
        verbose_name = "Angebot"
        verbose_name_plural = "Angebote"
#-----------------------------------------------------------------------------------------------------------------------
class Payment(Base):
    date = models.DateField(default=date.today, verbose_name="Datum")
    amount = models.PositiveIntegerField(help_text="Betrag in Cent", verbose_name="Betrag")


    class Meta:
        ordering = ("date",)
        verbose_name = "Zahlung"
        verbose_name_plural = "Zahlungen"""



