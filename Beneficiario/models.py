from django.db import models
class Beneficiario(models.Model):
    TIPO_VIVIENDA_CHOICES = [
        ('propia', 'Propia'),
        ('alquilada', 'Alquilada'),
        ('prestada', 'Prestada'),
        ('calle', 'Situación de calle'),
    ]

    apellido = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)

    domicilio = models.TextField(blank=True, null=True)
    cuil_dni = models.CharField(max_length=20, unique=True, blank=True, null=True)
    edad = models.PositiveIntegerField(blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True)
    con_quien_vive = models.CharField(max_length=100, blank=True)

    tipo_vivienda = models.CharField(
        max_length=10,
        choices=TIPO_VIVIENDA_CHOICES,
        blank=True
    )

    tiene_beneficio = models.BooleanField(default=False)
    cual_beneficio = models.TextField(blank=True, null=True)

    retira = models.TextField(
        blank=True,
        null=True,
        help_text="Ej: un par de zapatillas, una remera, un bolsón de comida, etc."
    )

    observaciones = models.TextField(blank=True, null=True)