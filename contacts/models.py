from django.db import models

#-----------------------------------------------------------------------------------------------------------------------

class Contact(models.Model):
    person = models.ForeignKey("persons.Person", on_delete=models.PROTECT, null=True, blank=True, related_name="person_contacts")
    company = models.ForeignKey("companies.Company", on_delete=models.PROTECT, null=True, blank=True, related_name="company_contacts")
    class Meta:
        verbose_name = "Kontakt"
        verbose_name_plural = "Kontakte"

#-----------------------------------------------------------------------------------------------------------------------