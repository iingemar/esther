from django.shortcuts import render
from django.shortcuts import render_to_response

from models import Food, Category


def home(request):
    return senaste(request)

def senaste(request):
    foods = Food.objects.all().order_by('-created')
    context = {
        'foods': foods,
        'header': 'Senaste mat'
    }
    return render(request, 'food_list.html', context)


def favoriter(request):
    foods = Food.objects.filter(rating=5)
    context = {
        'foods': foods,
        'header': 'Favoriter'
    }
    return render(request, 'food_list.html', context)


def kategorier(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'header': 'Kategorier'
    }
    return render(request, 'category.html', context)


def kategori(request, category):
    foods = Food.objects.filter(categories__name=category)
    context = {
        'foods': foods
    }
    return render(request, 'food_list.html', context)
