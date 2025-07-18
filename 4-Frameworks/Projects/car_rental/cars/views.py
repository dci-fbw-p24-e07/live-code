from django.shortcuts import render
from .models import Car

def car_list(request):
    cars = Car.objects.filter(availability=True)
    return render(request, "cars/list.html", {"cars": cars})
