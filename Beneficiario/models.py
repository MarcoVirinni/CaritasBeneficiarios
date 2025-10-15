from django.db import models

class Beneficiario(models.Model):
    TIPO_VIVIENDA_CHOICES = [
        ('propia', 'Propia'),
        ('alquilada', 'Alquilada'),
        ('prestada', 'Prestada'),
    ]

    apellido = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    domicilio = models.TextField()
    cuil_dni = models.CharField(max_length=20, unique=True)
    edad = models.PositiveIntegerField()
    telefono = models.CharField(max_length=20)
    con_quien_vive = models.CharField(max_length=100)
    tipo_vivienda = models.CharField(max_length=10, choices=TIPO_VIVIENDA_CHOICES)
    tiene_beneficio = models.BooleanField(default=False)
    cual_beneficio = models.TextField(blank=True, null=True)
    retira = models.TextField(blank=True, null=True, help_text="Ej: un par de zapatillas, una remera, un bolsón de comida, etc.")

    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.apellido}, {self.nombre} - {self.cuil_dni}'
