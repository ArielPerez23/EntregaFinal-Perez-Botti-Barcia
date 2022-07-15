from django.shortcuts import redirect, render
from django.http import HttpResponse

from .models import User
from .forms import UserRegisterForm

from .forms import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

def login_request(request):

    if request.method == "POST":
        
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password= password)
            
            if user is not None:
                login(request, user)
                return redirect("inicio")
            else:
                return redirect("login")
        else:
            return redirect("login")
    
    form = AuthenticationForm()

    return render(request, "blog/login.html",{"form":form})


def register_request(request):

    if request.method == "POST":
        
        form = UserRegisterForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1') # primer contraseña, no la confirmacion

            form.save() # registramos el usuario
            user = authenticate(username=username, password=password)# iniciamos la sesion

            if user is not None:
                login(request, user)
                return redirect("inicio")
            else:
                return redirect("login")

        return render(request,"blog/register.html",{"form":form})

    form = UserRegisterForm()

    return render(request,"blog/register.html",{"form":form})