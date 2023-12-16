from django.shortcuts import render
from django.views.generic import ListView

from .models import Services


class MainView(ListView):
    model = Services
    template_name = 'main_temp/temp/main.html'
