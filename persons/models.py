from django.db import models
from django.core.exceptions import ValidationError
from django.db.models import Q
#-----------------------------------------------------------------------------------------------------------------------
from core.defaults import Defaults
from core.models import Base
#-----------------------------------------------------------------------------------------------------------------------
class Person(Base):
    first_name = models.CharField(max_length=100, verbose_name="Vorname")
    last_name = models.CharField(max_length=100, verbose_name="Nachname")
    birth_date = models.DateField(verbose_name="Datum")
    title = models.CharField(max_length=100, null=True, blank=True, verbose_name="Titel")
    gender = models.CharField(max_length=100, verbose_name="Geschlecht")
    deceased = models.BooleanField(default=False, verbose_name="Verstorben")
    bank_account = models.ManyToManyField("finances.BankAccount", blank=True,
                                          related_name="bank_account_persons", verbose_name="Bankkonto")

    class Meta:
        ordering = ("first_name", "last_name")
        verbose_name = "Person"
        verbose_name_plural = "Personen"

    def __str__(self):
        return self.get_address()

    def get_address(self):
        if self.title:
            if self.title in Defaults.PRECEDING_TITLES:
                return f"{self.title} {self.first_name} {self.last_name}"
            else:
                return f"{self.first_name} {self.last_name}, {self.title}"
        else:
            return f"{self.first_name} {self.last_name}"
#-----------------------------------------------------------------------------------------------------------------------
class Company(Base):
    bank_account = models.ManyToManyField("finances.BankAccount", blank=True,
                                          related_name="bank_account_companies", verbose_name="Bankkonto")
    name = models.CharField(max_length=100, verbose_name="Name")
    parent_company = models.ForeignKey("Company", on_delete=models.PROTECT, null=True, blank=True,
                                       related_name="child_companies", verbose_name="übergeordnete Firma")
    uid = models.CharField(max_length=100, null=True, blank=True, verbose_name="UID")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Firma"
        verbose_name_plural = "Firmen"
#-----------------------------------------------------------------------------------------------------------------------
class Employee(Base):  # a.k.a PersonCompany
    person = models.ForeignKey("Person", on_delete=models.PROTECT, related_name="employee", verbose_name="Person")
    company = models.ForeignKey("Company", on_delete=models.PROTECT, related_name="employee", verbose_name="Firma")
    orders = models.ManyToManyField("orders.Order", through="EmployeeOrder", related_name="employee", verbose_name="Aufträge")
    roles = models.ManyToManyField("Role", through="EmployeeRole", related_name="employee", verbose_name="Rollen")

    def __str__(self):
        return self.person

    class Meta:
        verbose_name = "Mitarbeiter"
        verbose_name_plural = "Mitarbeiter"

class InternalEmployee(Base):
    employee = models.OneToOneField("Employee", on_delete=models.PROTECT, related_name="internal_employee", verbose_name="Mitarbeiter")
    social_security_number = models.IntegerField(verbose_name="SVN")
    wage = models.IntegerField(verbose_name="Stundengehalt", help_text="Stundengehalt in Cent")

    def __str__(self):
        return f"{self.employee}"

    class Meta:
        verbose_name = "interner Mitarbeiter"
        verbose_name_plural = "interne Mitarbeiter"
#-----------------------------------------------------------------------------------------------------------------------

class Client(Base):
    person = models.OneToOneField("Person", on_delete=models.PROTECT, null=True, blank=True,
                                  related_name="person_client", verbose_name="Person")
    company = models.OneToOneField("Company", on_delete=models.PROTECT, null=True, blank=True,
                                   related_name="company_client", verbose_name="Firma")
    #orders = models.ManyToManyField("orders.Order", through="orders.OrderClient", blank=True,
                                    #related_name="orders_clients", verbose_name="Aufträge")

    def __str__(self):
        if self.person:
            return f"{self.person}"
        elif self.company:
            return f"{self.company}"
        else:
            return f"{self.uuid}"

    def clean(self):
        super().clean()
        if self.person and self.company:
            raise ValidationError("Error")
        elif not self.person and not self.company:
            raise ValidationError("Error")

    class Meta:
        verbose_name = "Kunde"
        verbose_name_plural = "Kunden"
        constraints = [models.CheckConstraint(check=((Q(person__isnull=True)&Q(company__isnull=False)) | (Q(person__isnull=False) & Q(company__isnull=True))), name="person_true_and_company_false_or_person_false_and_company_true")]

class Role(Base):
    name = models.CharField()
    employees = models.ManyToManyField("Employee", through="EmployeeRole")

class EmployeeRole(Base):
    employee = models.ForeignKey("Employee", on_delete=models.PROTECT)
    role = models.ForeignKey("Role", on_delete=models.PROTECT)

class EmployeeOrder(Base):
    order = models.ForeignKey("orders.Order", on_delete=models.PROTECT)
    employee = models.ForeignKey("Employee", on_delete=models.PROTECT)