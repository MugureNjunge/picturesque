from django.shortcuts import render
from .models import Image, Location, Category

def home(request):
    categories = Category.objects.all()
    context = {}
    context['categories'] = categories
    return render(request, 'main/index.html', {})

def categoryPage(request):
    
    category = Category.objects.all()
    
    images = Image.objects.filter (category=category)
    for x in images:
      x.shortDescription = x.description[:100]

    context = {}
    context['images'] = images
    context['category'] = category

    return render(request, 'main/category.html', context) 
