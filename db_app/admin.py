from django.contrib import admin
from django.apps import apps
from reversion.admin import VersionAdmin
from django.contrib import admin
#from georeferenced_data.models import Place


#@admin.register(Place)
#class PlaceAdmin(LeafletGeoAdmin):
    #list_display = ("point",)

#app = apps.get_app_config('db_app')

#for model_name, model in app.models.items():
    #try:
        #@admin.register(model)
        #class DefaultVersionAdmin(VersionAdmin):
            #pass
    #except admin.sites.AlreadyRegistered:
        #pass

# alle Felder in der Listenansicht
#@admin.register(Order)
#class OrderAdmin(admin.ModelAdmin):
    #list_display = [f.name for f in Order._meta.fields]  # zeigt alle Spalten
    #search_fields = [f.name for f in Order._meta.fields]  # macht alle Spalten durchsuchbar
    #list_filter = [f.name for f in Order._meta.fields if f.get_internal_type() in ('CharField','IntegerField','DateField')]

# alle Felder in der Listenansicht
#@admin.register(Person)
#class PersonAdmin(admin.ModelAdmin):
    #list_display = [f.name for f in Person._meta.fields]  # zeigt alle Spalten
    #search_fields = [f.name for f in Person._meta.fields]  # macht alle Spalten durchsuchbar
    #list_filter = [f.name for f in Person._meta.fields if f.get_internal_type() in ('CharField','IntegerField','DateField')]

#@admin.register(Customer)
#class CustomerAdmin(admin.ModelAdmin):
    #raw_id_fields = ("person", "company")









