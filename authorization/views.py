from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from authorization.models import User
from authorization.forms import UserRegisterForm

from .forms import *
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import PasswordChangeView
from django.views import generic

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


class RegisterUser(generic.CreateView):
    form_class = UserRegisterForm
    template_name = 'blog/register.html'
    success_url = reverse_lazy('login')

def logout_request(request):
    logout(request)
    return redirect('inicio')


class EditarPerfil(generic.UpdateView):
    form_class = UserEditForm
    template_name = 'blog/editar_perfil.html'
    success_url = reverse_lazy('inicio')
    
    def get_object(self):
        return self.request.user


#Creamos avatar 
@login_required
def editar_avatar(request):
    
    if request.method == "POST":
            
        form = AvatarForm(request.POST, request.FILES)

        if form.is_valid():

            user = User.objects.get(username=request.user.username) # usuario con el que estamos loggueados

            avatar = Avatar(usuario=user, imagen=form.cleaned_data["imagen"])

            avatar.save()

            return redirect("inicio")

    else:
        form = AvatarForm()
    
    return render(request,"blog/editar_avatar.html",{"form":form})

class PasswordsChangeView(PasswordChangeView):
    form_class= PasswordChangingForm
    success_url = reverse_lazy('editar_perfil')


