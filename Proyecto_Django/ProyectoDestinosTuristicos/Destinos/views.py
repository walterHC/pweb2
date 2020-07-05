from django.shortcuts import render
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

def insertNewDestination(request):
    form = RawDestinationForm()
    if request.method == "POST":
        if form.is_valid():
            print(form.cleaned_data)
            Destination.objects.create(**form.cleaned_data)
        else:
            print(form.errors)
    context = {
            'form':form,
            }

    return render(request,'insertDestination.html', context)

def destinationList(request):
    queryset = Destination.objects.all()
    context = {
            'objectList':queryset,

            }
    return render(request, 'showDestination.html', context)

