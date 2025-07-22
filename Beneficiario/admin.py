from django.contrib import admin
from .models import Beneficiario

@admin.register(Beneficiario)
class BeneficiarioAdmin(admin.ModelAdmin):
    list_display = ('apellido', 'nombre', 'cuil_dni', 'telefono', 'tipo_vivienda')
    search_fields = ('apellido', 'nombre', 'cuil_dni', 'telefono')
    list_filter = ('tipo_vivienda', 'tiene_beneficio')
