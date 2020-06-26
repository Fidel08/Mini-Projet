from django.contrib import admin
from .models import Patient,Parrain
# Register your models here.

# création de la ressource d'import export
from import_export import resources
class PatientResource(resources.ModelResource):
    class Meta:
        model = Patient
        import_id_fields = ('code_patient',)
		
# Intégration simultanée dans l'espace d'administration de django de reversion et import-export
from import_export.admin import ImportExportModelAdmin
from reversion.admin import VersionAdmin



class PatientAdmin(ImportExportModelAdmin,VersionAdmin,admin.ModelAdmin):
    list_display=('code_patient','nom','prenom','sexe','age','cohorte_actuelle','numero1','numero2','date_enrol','observation') # Affichage des champs particulier lors de la modification dans l'espace d'admin (ajout supplementaire de admin.ModelAdmin dans la classe)
    search_fields=['code_patient','nom','prenom']
    list_filter=('sexe','date_enrol',cohorte_actuelleFilter)
    resource_class = PatientResource
    list_per_page = 15
admin.site.register(Patient, PatientAdmin)




class ParrainAdmin(VersionAdmin):
    pass
admin.site.register(Parrain)