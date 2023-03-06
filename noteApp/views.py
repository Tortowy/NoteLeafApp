from django.shortcuts import render

from django.views.generic import (
    DetailView,
    ListView,
    CreateView,
    DeleteView,
    UpdateView,
    View
)



# Create your views here.

class MainPageView(View):
    template_name = "main.html"
