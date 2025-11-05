from django.db import models

# Modelo Producto
class Producto(models.Model):
    nombre = models.CharField(max_length=100, db_index=True)  # Con Índice
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    disponible = models.BooleanField()
