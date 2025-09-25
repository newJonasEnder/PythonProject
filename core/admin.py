from django.contrib import admin
from core.custom_admins import custom_admin, DateSearch
from django.apps import apps
from django.contrib.admin.sites import AlreadyRegistered
#-----------------------------------------------------------------------------------------------------------------------
from works.models import Work, WorkLog
#-----------------------------------------------------------------------------------------------------------------------
from orders.models import Order

print(type(custom_admin))

class OrderInline(admin.TabularInline):
    model = Order
    fields = ["date"]
    extra = 1

#class ContractInline(admin.TabularInline):
    #model = Contract
    #fields = ["date", "net_amount"]
    #extra = 1


#-----------------------------------------------------------------------------------------------------------------------
"""from files.models import File, FileLog, FileStatus
#-----------------------------------------------------------------------------------------------------------------------
@custom_admin.register(File)
class FileAdmin(admin.ModelAdmin):
    inlines = [OrderInline]
    search_fields = ["number",]
    list_display = ["number",]

@custom_admin.register(FileLog)
class FileLogAdmin(admin.ModelAdmin):
    search_fields = ["date", "file", "file_status"]
    list_display = ["date", "file", "file_status"]

@custom_admin.register(FileStatus)
class FileStatusAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = ["name"]
#-----------------------------------------------------------------------------------------------------------------------
from finances.models import BankAccount, CounterOffer, Invoice, InvoiceOrder, Offer, Payment
#-----------------------------------------------------------------------------------------------------------------------
@custom_admin.register(BankAccount)
class BankAccountAdmin(DateSearch, admin.ModelAdmin):
    list_display = ["iban"]
    search_fields = ["iban"]

"""""""@custom_admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ["date","external_id", "net_amount", "notes", "number_of_invoices_display",
                    "remaining_amount_display"]
    search_fields = ["date", "external_id", "net_amount", "notes"]

    def number_of_invoices_display(self, obj):
        return obj.number_of_invoices
    number_of_invoices_display.short_description = "Rechnungsanzahl"

    def remaining_amount_display(self, obj):
        return obj.remaining_amount
    remaining_amount_display.short_description = "Restbetrag""""""""

@custom_admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ["date", "receiver", "net_amount"]
    search_fields = ["date", "receiver", "orders", "contract", "net_amount"]

    def percentage_display(self, obj):
        return obj.percentage
    percentage_display.short_description = "Prozentanteil"
#-----------------------------------------------------------------------------------------------------------------------
from persons.models import Person
#-----------------------------------------------------------------------------------------------------------------------
@admin.site.register(Person)
class PersonAdmin(DateSearch, admin.ModelAdmin):
    search_fields = ["first_name", "last_name", "birth_date"]
#----------------------------------------------------------------------------------------------------------------------
from vehicles.models import Car, LicensePlate, CarLicensePlate, CarLog, Trip

@custom_admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ["brand", "model", "vin"]
    search_fields = ["brand", "model", "vin"]

@custom_admin.register(LicensePlate)
class CarLicensePlateAdmin(admin.ModelAdmin):
    list_display = ["registration"]
    search_fields = ["registration"]

@custom_admin.register(CarLicensePlate)
class CarLicensePlateAdmin(admin.ModelAdmin):
    list_display = ["car", "license_plate", "date_of_registration"]
    search_fields = ["car", "license_plate", "date_of_registration"]

@custom_admin.register(CarLog)
class CarLogAdmin(admin.ModelAdmin):
    list_display = ["date", "car", "mileage"]
    search_fields = ["date", "car", "mileage"]

#@custom_admin.register(Trip)
#class TripAdmin(admin.ModelAdmin):
    #list_display = ["date", "car", "driver", "start", "end"]
    #search_display = ["date", "car", "driver", "start", "end"]

#@custom_admin.register(File)
#class FileAdmin(admin.ModelAdmin):
    #search_fields = ["number", "parent"]
    #list_display = ["number", "parent"]"""
