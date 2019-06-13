from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Persona
# Register your models here.


@admin.register(Persona)
class PersonaAdmin(ImportExportModelAdmin):
    pass
