from django.shortcuts import render
from Destinos.models import Destination

# Create your views here.

def index(request):
    dests = Destination.objects.all()

    return render(request,"index.html",{'dests':dests})
