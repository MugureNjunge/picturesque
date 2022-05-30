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
        
    return render(request, 'main/category.html', { "categories" : categories} ) 

def locationPage(request, location_id):
  
    locations = Location.objects.all()
    try:
        
        locations = Image.get_location(location_id)

    except Image.DoesNotExist:

        raise Http404()
        
    return render(request, 'main/location.html', { "locations" : locations} )     

def imagePage(request, image_id):

    images = Image.objects.all()

    try:
        images = Image.get_findImage(image_id)

    except Image.DoesNotExist:
        raise Http404
    return render(request, 'main/image.html', {'images': images} )     

def imageDetailPage(request, image_id):
    pass
  
    # descriptions = Image.description.objects.all()

    # try:
    #     descriptions = Image.get_findImage(image_id)

    # except Image.DoesNotExist:
    #     raise Http404
    # return render(request, 'main/image.html', {'descriptions': descriptions} )          

def searchResult(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = search_term.split.search_by_title(search_term)
        message = f"{search_term}"
        return render(request, 'main/search.html',{"message":message,"articles": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'main/search.html',{"message":message})



