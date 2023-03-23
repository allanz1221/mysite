from django.shortcuts import render, redirect, get_object_or_404
from .models import Personal, Equipo, Prestamo
from django.http import HttpResponse, JsonResponse

# Create your views here.
def index(request):
    equipos = Equipo.objects.all()
    context = {
        "equipos":equipos
    }
    return render(request, "index.html", context)

def registroEquipo(request):
    if request.method == 'POST':
        equipo = Equipo()
        equipo.nombre = request.POST.get('nombre')
        equipo.descripcion = request.POST.get('descripcion')
        equipo.save()
        return JsonResponse(["Listo"], safe=False)  

def eliminarEquipo(request, id):
    data = get_object_or_404(Equipo, id=id) 
    data.delete()
    return redirect('index')
