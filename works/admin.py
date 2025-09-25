from django.contrib import admin
from core.custom_admins import custom_admin
from works.models import Work

@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = ["name"]

custom_admin.register(Work, WorkAdmin)