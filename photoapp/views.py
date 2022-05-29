from django.http import Http404
from django.shortcuts import render
from .models import *


def home(request):
    categories = Category.objects.all()
    images = Image.objects.all()
    locations = Location.objects.all()



    return render(request, 'main/index.html', { "categories" : categories , "images" : images, "locations" : locations} )

def categoryPage(request, category_id):

    categories = Category.objects.all()

    try:
        
        categories = Image.get_category(category_id)

    except Image.DoesNotExist:

        raise Http404()
        
        

   
    # try:
        
    #     category = Image.objects.filter()

    # except:
    #     category = Category.objects.filter().first()  
    
    # images = Image.objects.filter (category=category)[:6]
    # for x in images:
    #   x.shortDescription = x.description[:100]

    # context = {}
    # context['categories'] = category
    # context['images'] = images
   

    return render(request, 'main/category.html', { "categories" : categories} ) 

def imageDetailPage(request):

    category = Category.objects.get()  
    location = Location.objects.get()  
    image = Image.objects.get()

    context = {}
    context['category'] = category
    context['location'] = location
    context['images'] = image
    

    return render(request, 'main/image.html', context) 


def searchResult(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = search_term.split.search_by_title(search_term)
        message = f"{search_term}"
        return render(request, 'main/search.html',{"message":message,"articles": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'main/search.html',{"message":message})



