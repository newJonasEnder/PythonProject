from django.contrib import admin
from core.custom_admins import custom_admin
from orders.models import Order, OrderClient

class OrderClientInline(admin.TabularInline):
    model = OrderClient
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderClientInline]
    search_fields = ["date"]
    list_display = ["date"]

    class Media:
        js = ("js/toggle.js",)

custom_admin.register(Order, OrderAdmin)

# Register your models here.
