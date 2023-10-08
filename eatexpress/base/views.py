from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import (
    ListView
)
from .models import Dish


def home(request):
    context = {
        'title': 'Home'
    }
    return render(request, 'eatexpress/index.html', context)



def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'eatexpress/about.html', context)

def menu(request):
    context = {
        'title': 'Menu'
    }
    return render(request, 'eatexpress/menu.html', context)

def get_dishes(request):
    dishes = Dish.objects.all()
    data = [
        {
            'name': dish.name,
            'image': dish.image.url,
            'price': dish.price
        }
        for dish in dishes
    ]
    return JsonResponse(data, safe=False)


def services(request):
    return render(request, 'eatexpress/services.html')