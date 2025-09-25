from datetime import date
from django.db import models
#-----------------------------------------------------------------------------------------------------------------------
from core.models import Base
#-----------------------------------------------------------------------------------------------------------------------
class WorkLog(Base):
    date = models.DateField(default=date.today, verbose_name="Datum")
    duration = models.DurationField(verbose_name="Dauer")
    internal_employee = models.ForeignKey("persons.InternalEmployee", on_delete=models.PROTECT,
                                          related_name="internal_employee_work_logs",
                                          verbose_name="interner Arbeitnehmer")
    order = models.ForeignKey("orders.Order", on_delete=models.PROTECT, related_name="order_work_logs",
                              verbose_name="Auftrag")
    work = models.ForeignKey("Work", related_name="+", on_delete=models.PROTECT, verbose_name="Arbeit")

    def __str__(self):
        return f"{self.date}"

    class Meta:
        ordering = ("date",)
        verbose_name = "Arbeitsprotokoll"
        verbose_name_plural = "Arbeitsprotokolle"
#-----------------------------------------------------------------------------------------------------------------------
class Work(Base):
    """A lookup table"""
    name = models.CharField(max_length=100, verbose_name="Name")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Arbeit"
        verbose_name_plural = "Arbeiten"
#-----------------------------------------------------------------------------------------------------------------------