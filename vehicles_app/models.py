from django.db import models

class Vehiculo(models.Model):
    marca = models.CharField(max_length=150)
    numero_registration = models.CharField(max_length=100, unique=True)
    disponibilidad = models.BooleanField(default=True) 
    año = models.PositiveSmallIntegerField()  
    estado = models.TextField()

    def __str__(self):
        return f"{self.marca} - {self.numero_registration}"

