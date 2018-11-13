from django.shortcuts import render

from .models import Pizza

# Create your views here.

def index(request):
    """The home page for the pizzeria"""
    return render(request, 'pizzeria/index.html')

def pizzas(request):
    """The list of pizzas page"""
    pizzas = Pizza.objects.order_by('id')
    context = {'pizzas': pizzas}
    return render(request, 'pizzeria/pizzas.html', context)

def pizza(request, pizza_id):
    """Show toppings for a pizza"""
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.order_by('id')
    print(toppings)
    context = {'pizza': pizza, 'toppings': toppings }
    return render(request, 'pizzeria/pizza.html', context)