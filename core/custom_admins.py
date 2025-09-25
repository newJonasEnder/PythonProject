from datetime import datetime
from django.contrib.admin import AdminSite

class DateSearch:
    def get_search_results(self, request, queryset, search_term):
        try:
            date = datetime.strptime(search_term, "%d.%m.%Y").date()
            search_term = date.strftime("%Y-%m-%d")
        except ValueError:
            pass
        return super().get_search_results(request, queryset, search_term)

class CustomAdminSite(AdminSite):
    site_header = "Custom Admin"
    site_title = "Custom Admin Portal"
    index_title = "Welcome to the Custom Admin"
    def get_app_list(self, request):
        app_list = super().get_app_list(request)
        preceding_apps = ["works", "files", "orders"]
        ordered_app_list = []
        for preceding_app in preceding_apps:
            for app in app_list:
                if app["app_label"] == preceding_app:
                    ordered_app_list.append(app)
                else:
                    pass
        for app in app_list:
            if app["app_label"] not in preceding_apps:
                ordered_app_list.append(app)
            else:
                pass
        return ordered_app_list

custom_admin = CustomAdminSite(name="custom_admin")

