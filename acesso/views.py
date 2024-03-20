from django.shortcuts import render
from django.views.generic import CreateView
from .models import Predio
from .forms import PredioForm
from django.contrib import messages
from django.urls import reverse
# Create your views here.

class NovoPredio(CreateView):
    template_name = "predio/novo-predio.html"
    model = Predio
    form_class = PredioForm

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Cadastro realizado com sucesso!")
        return reverse('home')