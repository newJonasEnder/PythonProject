from django.db import models
from core.defaults import Defaults
from core.models import Base

from django.urls import reverse

class Person(Base):
    first_name = models.CharField(max_length=100, verbose_name="Vorname")
    last_name = models.CharField(max_length=100, verbose_name="Nachname")
    birth_date = models.DateField(null=True, blank=True, verbose_name="Geburtsdatum")
    title = models.CharField(max_length=100, null=True, blank=True, verbose_name="Titel")
    gender = models.CharField(max_length=100, choices=[("male", "männlich"), ("female", "weiblich"), ("diverse", "divers")], verbose_name="Geschlecht")
    deceased = models.BooleanField(default=False, verbose_name="verstorben")

    class Meta:
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

class Employee(Base):  # a.k.a PersonCompany
    person = models.ForeignKey("Person", on_delete=models.PROTECT, related_name="employee", verbose_name="Person", blank=True)
    #company = models.ForeignKey("companies.Company", on_delete=models.PROTECT, related_name="employee", verbose_name="Firma", blank=True)
    orders = models.ManyToManyField("orders.Order", through="EmployeeOrder", related_name="employee", verbose_name="Aufträge")
    roles = models.ManyToManyField("Role", through="EmployeeRole", related_name="employee", verbose_name="Rollen")

    def __str__(self):
        return f"{self.person}"

    class Meta:
        verbose_name = "Mitarbeiter"
        verbose_name_plural = "Mitarbeiter"

class InternalEmployee(Base):
    employee = models.OneToOneField("Employee", on_delete=models.PROTECT, related_name="internal_employee", verbose_name="Mitarbeiter")
    social_security_number = models.IntegerField(verbose_name="SVN")
    wage = models.IntegerField(verbose_name="Stundengehalt", help_text="Stundengehalt in Cent")
    #bank_account = models.ManyToManyField("finances.BankAccount", blank=True,
                                          #related_name="bank_account_persons", verbose_name="Bankkonto")

    def __str__(self):
        return f"{self.employee}"

    class Meta:
        verbose_name = "interner Mitarbeiter"
        verbose_name_plural = "interne Mitarbeiter"

class Role(Base):
    name = models.CharField()
    employees = models.ManyToManyField("Employee", through="EmployeeRole")

    def get_absolute_url(self):
        return reverse("Role-detail", args=[str(self.uuid)])

class EmployeeRole(Base):
    employee = models.ForeignKey("Employee", on_delete=models.PROTECT)
    role = models.ForeignKey("Role", on_delete=models.PROTECT)

class EmployeeOrder(Base):
    order = models.ForeignKey("orders.Order", on_delete=models.PROTECT)
    employee = models.ForeignKey("Employee", on_delete=models.PROTECT)