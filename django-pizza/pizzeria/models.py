from django.db import models

# Create your models here.


class Pizza(models.Model):
    """A pizza"""
    name = models.CharField(max_length=200)
    def __str__(self):
        """Return a string representation of the model."""
        return self.name


class Topping(models.Model):
    """Toppings for a pizza"""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        """Return a string representation of the model."""
        return self.name
