from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from .models import Pizza


# Create your views here.
# def index(request):
#     return HttpResponse("Hello, Pizza!")


class PizzaList(generic.ListView):
    queryset = Pizza.objects.all()
    template_name = "pizza/index.html"
