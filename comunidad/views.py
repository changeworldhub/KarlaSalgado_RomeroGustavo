from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import  UserCreationForm
from django.template.context_processors import request
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from .models import Voluntario
from .forms import VoluntarioForm
from .forms import RegistroForm

# Create your views here.


# class RegistroUsuario(CreateView):
#     model = User
#     template_name = "registrar.html"
#     form_class = UserCreationForm
#     success_url = reverse_lazy('voluntarios')

def register(request):
    status=''
    if request.method=='POST':
        user=User()
        try: 
            user=User.objects.create_user(username=request.POST.get('username'),
            password=request.POST.get('password1'),
            email=request.POST.get('email'),
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name')
            )
        except:
            status='Error'
            print(status)
            return render(
                    request,
                    'registrar.html',
                    {'status':status}
            )
        user.save()
        status='ok'
        print(status)
    return render(
            request,
            'registrar.html',
            {'status':status}
    )


def index(request):
        return render(
                request,
                'index.html',
                {}
        )


def nosotros(request):
    return render(
           request,
           'nosotros.html',
           {}
    )

def suscripcion_view(request):
    return render(
           request,
           'suscripcion.html',
           {}
    )



def Login(request):
    status = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        user = authenticate(request, username = username, password = password)
        if user:
            login(request, user)
            status = 'ok'
            return HttpResponseRedirect(reverse('index'))
        else:
            status = 'Error'
            messages.error(request,'Error al iniciar sesion')
        variables = {'status':status}
        # return render(request,'Login.html'variables)
        return render(request,'Login.html',variables)
    return render(request,'Login.html')

@login_required(login_url = 'Login')
def logout_view(request):
    logout(request)
    return redirect('Login')



def voluntario_create(request):
    if request.method == 'POST':
        form = VoluntarioForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('suscribir')
    else:
         form =VoluntarioForm() 
    return render(request, 'formulario.html',{'form':form})


class VoluntarioUpdate(UpdateView):
    model = Voluntario
    form_class = VoluntarioForm
    template_name = 'formulario.html'
    success_url = reverse_lazy('voluntarios')

class VoluntarioDelete(DeleteView):
    model = Voluntario
    success_url = reverse_lazy('index')
 
from django.views import generic
class VoluntarioListView(generic.ListView):
    model = Voluntario

from django.views import generic
class VoluntarioDetailView(generic.DetailView):
    model = Voluntario
