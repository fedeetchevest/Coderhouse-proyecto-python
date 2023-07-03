from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import articulo
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class ArticuloListView(ListView):
    model = articulo
    template_name = 'TechnoStyleApp/index.html'
    
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
class Caracteristicas(DetailView):
    model = articulo
    template_name = 'TechnoStyleApp/caracteristicas.html'

class ModificarProducto(UpdateView):
    model = articulo
    success_url = reverse_lazy("inicio")
    fields = ["id", "marca", "modelo","categoria","precio","descripcion","imagen"]
    template_name = "TechnoStyleApp/update.html"

class BorrarArticulo(DeleteView):
    model = articulo
    success_url = reverse_lazy("inicio")
    template_name = "TechnoStyleApp/delete.html"

