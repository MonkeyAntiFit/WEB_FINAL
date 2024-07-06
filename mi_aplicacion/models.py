
from django.db import models
from django.contrib.auth.models import User


class usuario(models.Model):
    nombre_usuario = models.CharField(max_length=20,unique=True, blank=True,null=True)
    nombre = models.CharField(max_length=200, default=' ')
    apellido = models.CharField(max_length=200, default=' ')
    rut = models.CharField(primary_key=True, max_length=200, default=' ')
    correo = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    contrasena = models.CharField(max_length=100)

    def str(self):
        return f'{self.nombre} {self.apellido}'



class candidato(models.Model):
    nombreCandidato = models.CharField(max_length=200, default=' ') 
    apellidoCandidato = models.CharField(max_length=200, default=' ')
    correo = models.EmailField(unique=True, max_length=100,
    blank=True, null=True)
    rut = models.CharField(primary_key=True, max_length=200, default=' ')
    edad = models.CharField(max_length=2) 

    def __str__(self):
        return f'{self.nombreCandidato} {self.apellidoCandidato}'

class Producto(models.Model):
    CATEGORIAS = [
        ('roller', 'Roller'),
        ('skate', 'Skate'),
        ('surf', 'Surf'),
        ('accesoriosurf', 'AccesorioSurf'),
        ('accesorioskate', 'AccesorioSkate'),
        ('accesorioroller', 'AccesorioRoller'),
    ]
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='productos/')
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)

    def __str__(self):
        return self.nombre

class Carrito(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto, through='CarritoItem')

    def get_carrito_data(self):
        items = self.carritoitem_set.all()
        return [{'producto': item.producto.nombre, 'cantidad': item.cantidad} for item in items]

    def __str__(self):
        return f'Carrito de {self.usuario.username}'

class CarritoItem(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.cantidad} x {self.producto.nombre}'
