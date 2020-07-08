from django.shortcuts import render, redirect, get_object_or_404
from .models import Destination
from .forms import DestinationForm, RawDestinationForm

# Create your views here.
def addDestination(request):
    if request.method == "POST":
        form = DestinationForm(request.POST)
        if form.is_valid():
            Destination.save()
            return redirect('/')

    else:
        form = DestinationForm()


    context = {
            'form': form
            }

    return render(request,"addDestination.html", context)


def addDestination1(request):
    if request.method == 'POST':
        nombreCiudad = request.POST['nombreCiudad']
        imagenCiudad = request.POST['imagenCiudad']
        descripcionCiudad = request.POST['descripcionCiudad']
        precioTour = request.POST['precioTour']
        ofertaTour = request.POST['ofertaTour']

        if Destination.objects.filter(nombreCiudad=nombreCiudad).exists():
            messages.info(request,'Esta ciudad ya fue agregada')
            return redirect('addDestination')
        else:

            Destination.objects.all()
            destino = Destination.objects.create(nombreCiudad=nombreCiudad, imagenCiudad=imagenciudad,descripcionciudad=descripcionCiudad, precioTour=precioTour,ofertaTour=ofertaTour)
            destino.save()
            return redirect('/')

    else:
        return render(request,'addDestination.html')

def insertDestination(request):
    form = RawDestinationForm()
    if request.method == "POST":
        if form.is_valid():
            Destination.objects.create(**form.cleaned_data)
            print("form.cleaned_data")
        else:
            print("form.errors")

    context = {
            'form':form,
            }

    return render(request,'insertDestination.html', context)

def editDestination(request, myID):
    obj = Destination.objects.get(id = myID)
    form = DestinationForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        form = DestinationForm()
    context = {
            'form': form,
            }
    return render(request,"editDestination.html", context)


def showDestination(request, myID):
    obj = Destination.objects.get(id = myID)
    context = {
            'object': obj,
            }
    return render(request,"showDestination.html", context)


def listDestinations(request):
    queryset = Destination.objects.all()
    context = {
            'objectList':queryset,
            }

    return render(request, 'showListDestinations.html', context)


def deleteDestination(request, myID):
    obj = get_object_or_404(Destination, id=myID)

    if request.method == 'POST':
        obj.delete()
        print("borrado con exito")
        return redirec("/")

    context = {
            'object':obj
            }

    return render(request,"deleteDestination.html", context)
