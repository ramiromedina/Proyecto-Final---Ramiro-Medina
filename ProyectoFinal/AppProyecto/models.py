from django.db import models

# Create your models here.
class Tazas(models.Model):
    categoria=models.CharField(max_length=30)
    nombre=models.CharField(max_length=30)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    informacion = models.CharField(max_length=600)
    colores = models.CharField(max_length=30)
    imagenTaza = models.CharField(max_length=500)
    
    def _str_(self):
         return f"Categoria: {self.categoria} Nombre de la Taza: {self.nombre} Precio: ${self.precio} Información: {self.informacion} Colores disponibles: {self.colores}"


class Funkos(models.Model):
    categoria=models.CharField(max_length=30)
    nombre=models.CharField(max_length=30)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    informacion = models.CharField(max_length=600)
    imagenFunko = models.CharField(max_length=500)
    
    def _str_(self):
         return f"Categoria: {self.categoria} Nombre del Funko: {self.nombre} Precio: ${self.precio} Información: {self.informacion}"


class Remeras(models.Model):
    categoria=models.CharField(max_length=30)
    nombre=models.CharField(max_length=30)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    talle = models.CharField(max_length=30)
    imagenRemera = models.CharField(max_length=500)
    
    def _str_(self):
         return f"Categoria: {self.categoria} Nombre de la remera: {self.nombre} Precio: ${self.precio} Talle: {self.talle}"