from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from .models import Voluntario
from .forms import VoluntarioForm

# Create your views here.

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
    succes_url = reverse_lazy('voluntarios')


class VoluntarioDelete(DeleteView):
    model = Voluntario
    succes_url = reverse_lazy('index')
 
from django.views import generic
class VoluntarioListView(generic.ListView):
    model = Voluntario

from django.views import generic
class VoluntarioDetailView(generic.DetailView):
    model = Voluntario