from django.shortcuts import render

# Create your views here.

def index(request):
    """The home page for the pizzeria"""
    return render(request, 'pizzeria/index.html')