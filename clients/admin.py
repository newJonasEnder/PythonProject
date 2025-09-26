from django.contrib import admin

from core.custom_admins import custom_admin

from clients.models import Client, PrivateClient, BusinessClient

from orders.models import OrderClient

class OrderInline(admin.TabularInline):
    model = OrderClient
    extra = 0

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    search_fields = ["private_client", "business_client"]
    list_display = ["private_client", "business_client"]
    inlines = [OrderInline]

    class Media:
        js = ("files/js/toggle.js",)

custom_admin.register(Client, ClientAdmin)

@admin.register(PrivateClient)
class PrivateClientAdmin(admin.ModelAdmin):
    search_fields = ["person"]
    list_display = ["person"]

    class Media:
        js = ("files/js/toggle.js",)

custom_admin.register(PrivateClient, PrivateClientAdmin)

@admin.register(BusinessClient)
class BusinessClientAdmin(admin.ModelAdmin):
    search_fields = ["company"]
    list_display = ["company"]

    class Media:
        js = ("js/toggle.js",)

custom_admin.register(BusinessClient, BusinessClientAdmin)

