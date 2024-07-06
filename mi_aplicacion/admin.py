from django.contrib import admin
from .models import usuario, candidato
from .models import Producto

admin.site.register(usuario)
admin.site.register(candidato)
admin.site.register(Producto)