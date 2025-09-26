from django.contrib import admin
from core.custom_admins import custom_admin
from files.models import File, FileLog, FileNote
from django.urls import reverse
from django.utils.html import format_html
from orders.models import Order

class ChildFileInline(admin.TabularInline):
    model = File
    fk_name = "parent_file"
    fields = ["date", "number_link", "active", "created_at", "updated_at"]
    readonly_fields = ["date", "number_link", "active", "created_at", "updated_at"]
    extra = 0
    verbose_name = "Nachakt"
    verbose_name_plural = "Nachakte"

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def number_link(self, obj):
        if not obj.pk:
            return "-"
        url = reverse(f"custom_admin:files_file_change", args=[obj.pk],)
        return format_html("<a href=\"{}\">{}</a>", url, obj.number)
    number_link.short_description = "Geschäftszahl"
    number_link.admin_order_field = "number"

class OrderInline(admin.TabularInline):
    model = Order
    fk_name = "file"
    fields = ["date", "id_link"]
    readonly_fields = ["id_link"]
    extra = 0
    verbose_name = "Auftrag"
    verbose_name_plural = "Aufträge"

    def id_link(self, obj):
        if not obj.pk:
            return "-"
        url = reverse(f"custom_admin:orders_order_change", args=[obj.pk],)
        return format_html("<a href=\"{}\">{}</a>", url, obj.id)
    id_link.short_description = "ID"
    id_link.admin_order_field = "id"

class FileLogInline(admin.TabularInline):
    model = FileLog
    fk_name = "file"
    fields = ["date", "file_status", "active", "created_at", "updated_at"]
    readonly_fields = ["created_at", "updated_at"]
    extra = 0
    verbose_name = "Zustansänderung"
    verbose_name_plural = "Zustandsänderungen"

class FileNoteInline(admin.TabularInline):
    model = FileNote
    fk_name = "file"
    fields = ["date", "note", "active", "created_at", "updated_at"]
    readonly_fields = ["created_at", "updated_at"]
    extra = 0
    verbose_name = "Notiz"
    verbose_name_plural = "Notizen"

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    inlines = [OrderInline, FileLogInline, FileNoteInline, ChildFileInline]
    search_fields = ["date", "number"]
    list_display = ["date", "number"]

    class Media:
        js = ("js/toggle.js",)

custom_admin.register(File, FileAdmin)


