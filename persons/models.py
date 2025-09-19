from django.db import models
from django.core.exceptions import ValidationError
from core.models import Base
from django.db.models import Q

PRECEDING_TITLES = ("Mag.", "Dr.", "Dipl.-Ing.")

class Person(Base):
    first_name = models.CharField(max_length=100, verbose_name="Vorname")
    last_name = models.CharField(max_length=100, verbose_name="Nachname")
    birth_date = models.DateField(verbose_name="Datum")
    title = models.CharField(max_length=100, verbose_name="Titel")
    gender = models.CharField(max_length=100, verbose_name="Geschlecht")
    deceased = models.BooleanField(default=False, verbose_name="Verstorben")

    class Meta:
        ordering = ("first_name", "last_name")
        verbose_name = "Person"
        verbose_name_plural = "Personen"

    def __str__(self):
        self.get_address()

    def get_address(self):
        if self.title:
            if self.title in PRECEDING_TITLES:
                return f"{self.title} {self.first_name} {self.last_name}"
            else:
                return f"{self.first_name} {self.last_name}, {self.title}"
        else:
            return f"{self.first_name} {self.last_name}"

class Company(Base):
    name = models.CharField(max_length=100, verbose_name="Name")
    uid = models.CharField(max_length=100, null=True, blank=True, verbose_name="UID")
    parent_company = models.ForeignKey("Company", on_delete=models.PROTECT, null=True, blank=True, related_name="subsidiary", verbose_name="Mutterfirma")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Firma"
        verbose_name_plural = "Firmen"

class Department(Base):
    name = models.CharField(max_length=100, verbose_name="Name")
    uid = models.CharField(max_length=100, null=True, blank=True, verbose_name="UID")
    company = models.ForeignKey("Company", on_delete=models.PROTECT, related_name="department", verbose_name="Firma")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Abteilung"
        verbose_name_plural = "Abteilungen"

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

class Client(Base):
    person = models.ForeignKey(Person, on_delete=models.PROTECT, null=True, blank=True, related_name="private_client", verbose_name="Person")
    company = models.ForeignKey(Person, on_delete=models.PROTECT, null=True, blank=True, related_name="corporate_client", verbose_name="Firma")
    orders = models.ManyToManyField("orders.Order", through="orders.OrderClient", blank=True, related_name="orders_clients", verbose_name="Aufträge")

    def __str__(self):
        if self.person:
            return f"{self.person}"
        elif self.company:
            return f"{self.company}"
        else:
            return f"{self.id}"

    def clean(self):
        super().clean()
        if self.person and self.company:
            raise ValidationError

    class Meta:
        verbose_name = "Kunde"
        verbose_name_plural = "Kunden"
        constraints = [models.CheckConstraint(check=((Q(person__isnull=True)&Q(company__isnull=False))&(Q(person__isnull=False) & Q(company__isnull=True))), name="person_true_and_company_false_or_person_false_and_company_true")]

class Role(Base):
    name = models.CharField()
    employees = models.ManyToManyField("Employee", through="EmployeeRole")

class EmployeeRole(Base):
    employee = models.ForeignKey("Employee", on_delete=models.PROTECT)
    role = models.ForeignKey("Role", on_delete=models.PROTECT)

class EmployeeOrder(Base):
    order = models.ForeignKey("orders.Order", on_delete=models.PROTECT)
    employee = models.ForeignKey("Employee", on_delete=models.PROTECT)