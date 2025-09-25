from django.db import models

from django.contrib.auth.models import AbstractUser

from persons.models import InternalEmployee

class CustomUser(AbstractUser):
    person = models.ForeignKey("persons.Person", on_delete=models.CASCADE)

    @property
    def internal_employee(self):
        return InternalEmployee.objects.filter(employee__person=self).first()

# Create your models here.
