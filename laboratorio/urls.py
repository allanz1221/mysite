from django.urls import path

# Create your views here.
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("guardarEquipo", views.registroEquipo, name="guardarEquipo"),
    path("eliminarEquipo/<int:id>", views.eliminarEquipo, name="eliminarEquipo"),
]