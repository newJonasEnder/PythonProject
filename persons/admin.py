from django.contrib import admin

from core.custom_admins import custom_admin

from persons.models import Person, Employee, EmployeeOrder, InternalEmployee, Role, EmployeeRole

class EmployeeInline(admin.TabularInline):
    model = Employee
    extra = 0
    classes = ["collapse"]
    show_change_link = True
    verbose_name = "Beschäftigung"
    verbose_name_plural = "Beschäftigungen"

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

from django.contrib import admin
from django.utils.translation import gettext_lazy as _

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    readonly_fields = ("uuid", "created_at", "updated_at")
    fieldsets = (("Test", {"fields": ("uuid", "active", "created_at", "updated_at")}),)







    #search_fields = ["first_name", "last_name", "birth_date", "title", "gender", "deceased"]
    #list_display = ["first_name", "last_name", "birth_date", "title", "gender", "deceased"]
    #inlines = [EmployeeInline]



custom_admin.register(Person, PersonAdmin)

class EmployeeOrderInline(admin.TabularInline):
    model = EmployeeOrder
    extra = 0
    verbose_name = "Arbeitnehmer-Auftrag-Zuweisung"
    verbose_name_plural = "Arbeitnehmer-Auftrag-Zuweisungen"

class EmployeeRoleInline(admin.TabularInline):
    show_change_link = True
    model = EmployeeRole
    extra = 0

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    inlines = [EmployeeOrderInline, EmployeeRoleInline]
    search_fields = ["person",]
    list_display = ["person"]

    class Media:
        js = ("js/toggle.js",)

custom_admin.register(Employee, EmployeeAdmin)

@admin.register(InternalEmployee)
class InternalEmployeeAdmin(admin.ModelAdmin):
    search_fields = ["employee", "social_security_number", "wage"]
    list_fields = ["employee", "social_security_number", "wage"]

custom_admin.register(InternalEmployee, InternalEmployeeAdmin)

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    view_on_site = True
    search_fields = ["name"]
    list_display = ["name"]

custom_admin.register(Role, RoleAdmin)



