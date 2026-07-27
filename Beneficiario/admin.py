from django.contrib import admin
from django.core.exceptions import ValidationError
from django import forms
from .models import Beneficiario


class BeneficiarioForm(forms.ModelForm):
    fecha_nacimiento = forms.DateField(
        required=False,
        input_formats=['%d/%m/%Y'],
        widget=forms.DateInput(
            format='%d/%m/%Y',
            attrs={
                'placeholder': 'DD/MM/AAAA'
            }
        )
    )

    class Meta:
        model = Beneficiario
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        tiene_beneficio = cleaned_data.get("tiene_beneficio")
        cual_beneficio = cleaned_data.get("cual_beneficio")

        if tiene_beneficio and not cual_beneficio:
            raise ValidationError("Debés especificar cuál beneficio recibe.")

        if not tiene_beneficio and cual_beneficio:
            raise ValidationError("Marcá 'Tiene beneficio' si especificás cuál.")

        return cleaned_data


@admin.register(Beneficiario)
class BeneficiarioAdmin(admin.ModelAdmin):
    form = BeneficiarioForm

    list_display = (
        'apellido',
        'nombre',
        'fecha_nacimiento',
        'cuil_dni',
        'telefono',
        'tipo_vivienda',
        'tiene_beneficio'
    )

    search_fields = (
        'apellido',
        'nombre',
        'cuil_dni',
        'telefono'
    )

    list_filter = (
        'tipo_vivienda',
        'tiene_beneficio'
    )

    class Media:
        js = ('admin/js/beneficiario.js',)
