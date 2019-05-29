from django.shortcuts import render, get_object_or_404
from .models import Przedmiot,Nauczyciel,Sprawdzian


# Create your views here.

def home(request):
    return render(request, 'pages/home.html', {})


def przedmiot(request):
    przedmioty = Przedmiot.objects.all()
    return render(request, 'pages/przedmioty.html', {'przedmioty':przedmioty})

def nauczycielePrzedmiot(request, pk):
    nauczyciele = Nauczyciel.objects.filter(id_przedmiotu=pk).values()
    return render(request,'pages/nauczyciele.html',{'nauczyciele':nauczyciele})

def nauczycielSprawdzian(request,kp):
    sprawdziany = Sprawdzian.objects.filter(id_nauczyciela_id=kp).values()
    return render(request,'pages/sprawdziany.html',{'sprawdziany':sprawdziany})