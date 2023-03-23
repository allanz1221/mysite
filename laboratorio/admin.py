from django.contrib import admin

# Register your models here.
from .models import Personal, Equipo, Prestamo

admin.site.register(Personal)
admin.site.register(Equipo)
admin.site.register(Prestamo)