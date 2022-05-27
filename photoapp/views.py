from django.shortcuts import render
from .models import Image, Location, Category

def home(request):
    categories = Category.objects.all()
    context = {}
    context['categories'] = categories
    return render(request, 'main/index.html', context)

def categoryPage(request):
    
    category = Category.objects.get()
    
    images = Image.objects.filter (category=category)[:6]
    for x in images:
      x.shortDescription = x.description[:100]

    context = {}
    context['images'] = images
    context['category'] = category

    return render(request, 'main/category.html', context) 

def imageDetailPage(request):

    category = Category.objects.get()   
    image = Image.objects.get()

    context = {}
    context['category'] = category
    context['images'] = image
    

    return render(request, 'main/image.html', context) 

