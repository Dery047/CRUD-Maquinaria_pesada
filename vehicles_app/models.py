from django.db import models

#creating Vehiculo model and its fields.
class Vehiculo(models.Model):
    marca = models.CharField(max_length=150)
    numero_registration = models.CharField(max_length=100, unique=True)
    disponibilidad = models.BooleanField(default=True) 
    año = models.PositiveSmallIntegerField()  
    estado = models.TextField()

    def __str__(self):
        return f"{self.marca} - {self.numero_registration}"

# Nota: este programa solo permite el registro de los vehiculos y que puedan ser almacenados en una database
# A futuro se le agregarán otros metodos como la eliminación de vehiculos y otras características segun sea necesario.

# Note: This program currently only allows vehicle registration and stores them in a database.
# Additional features like vehicle deletion and other functionalities will be added in the future as needed.
