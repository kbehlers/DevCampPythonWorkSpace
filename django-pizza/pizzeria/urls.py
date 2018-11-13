"""Defines URL patterns for Pizzeria"""

from django.urls import path

from . import views

app_name = 'pizzeria'
urlpatterns = [
    #Home page
    path('', views.index, name='index'),

    #Pizza List Page
    path('pizzas/', views.pizzas, name='pizzas'),

    #Detail page for toppings
    path('pizzas/<int:pizza_id>/', views.pizza, name='pizza'),
]