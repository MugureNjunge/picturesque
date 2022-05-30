from django.http import Http404
from django.shortcuts import render
from .models import *


def home(request):
    images = Image.objects.all()
    categories = Category.objects.all() 
    locations = Location.objects.all()

    try:
        images = Image.getImages()
    except Image.DoesNotExist:
        raise Http404()

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


def search(request):
    locations = Location.objects.all()
    categories = Category.objects.all()

    if 'searchedImage' in request.GET and request.GET["searchedImage"]:
        search_term = request.GET.get("searchedImage")
        searchedImages = Image.searchImage(search_term)
        message=f"{search_term}"
        return render (request, 'main/search.html',{"message":message,"searchedImages": searchedImages, "categories": categories, "locations": locations})
    else:
        message = "Kindly add a search item"
        return render(request, 'search.html',{"message":message, "categories": categories, "locations": locations})        



