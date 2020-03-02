import json
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from rest_framework.views import APIView

from AppEstudio.forms import MascotaForm, PersonaForm
from AppEstudio.models import Mascota, Persona

# Create your views here.
from AppEstudio.serializers import MascotaSerializer


def index(request):
    return render(request, 'estudio/index.html')


def mascota_view(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('mascota:mascota_listar')
    else:
        form = MascotaForm()
    return render(request, 'estudio/mascota_form.html', {'form': form})


def mascota_list(request):
    mascota = Mascota.objects.all().order_by('id')
    contexto = {'mascotas': mascota}
    return render(request, 'estudio/mascota_list.html', contexto)



def mascota_edit(request, id_mascota):
    mascota = Mascota.objects.get(id=id_mascota)
    if request.method == 'GET':
        form = MascotaForm(instance=mascota)
    else:
        form = MascotaForm(request.POST, instance=mascota)
        if form.is_valid():
            form.save()
        return redirect('mascota:mascota_listar')
    return render(request, 'estudio/mascota_form.html', {'form': form})

def mascota_delete(request, id_mascota):
    mascota = Mascota.objects.get(id=id_mascota)
    if request.method == 'POST':
        mascota.delete()
        return redirect('mascota:mascota_listar')
    return render(request, 'estudio/mascota_delete.html', {'mascota': mascota})

"""Vistas Genericas Programar orientado a clases Genericas"""

class MascotaList(ListView):
    paginate_by = 10
    model = Mascota
    queryset = Mascota.objects.all().order_by('id')
    template_name = 'estudio/mascota_list.html'

class MascotaCreate(CreateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'estudio/mascota_form.html'
    success_url = reverse_lazy('mascota:mascota_listar')

class MascotaUpdate(UpdateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'estudio/mascota_form.html'
    success_url = reverse_lazy('mascota:mascota_listar')


class MascotaDelete(DeleteView):
    model = Mascota
    template_name = 'estudio/mascota_delete.html'
    success_url = reverse_lazy('mascota:mascota_listar')

""" CRUD Persona Vistas Genericas """

class PersonaList(ListView):
    paginate_by = 10
    model = Persona
    queryset = Persona.objects.all().order_by('id')
    template_name = 'estudio/persona_list.html'

class PersonaCreate(CreateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'estudio/persona_form.html'
    success_url = reverse_lazy('mascota:persona_listar')

"""Servicio Mascota Json"""

class MascotaAPI(APIView):
    serializer = MascotaSerializer

    def get(self, request, format=None):
        lista = Mascota.objects.all()
        response = self.serializer(lista, many=True)
        return HttpResponse(json.dumps(response.data), content_type='application/json')



