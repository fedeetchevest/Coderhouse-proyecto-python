from django.db import models

class articulo(models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    categoria = models.CharField(max_length=20)
    precio = models.IntegerField()

class clientes(models.Model):
    nombre = models.CharField(max_length=20)
    dni = models.IntegerField()
    correo = models.CharField(max_length=20)
    telefono = models.IntegerField()
    

class sucursales(models.Model):
    nombre = models.CharField(max_length=20)
    numero_sucursal = models.IntegerField()
    direccion = models.CharField(max_length=50)