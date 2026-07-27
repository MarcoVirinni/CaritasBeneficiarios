# admin.py
from django.contrib import admin
from django.contrib.auth.models import Group
admin.site.site_header = "Parroquia San José"
admin.site.site_title = "Voluntarias Caritas"
admin.site.index_title = "Panel de control - Beneficiarios"

admin.site.unregister(Group)
