from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def inicio(request):
    
    return render(request, "blog/index.html")

def software(request):
    
    return render(request, "blog/software.html")

def hardware(request):
    
    return render(request, "blog/hardware.html")

def curiosidades(request):
    
    return render(request, "blog/curiosidades.html")

