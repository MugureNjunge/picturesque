from django.http import Http404
from django.shortcuts import render
from .models import Image, Category, Location


def home(request):
    images = Image.objects.all()
    categories = Category.objects.all() 
    locations = Location.objects.all()


    return render(request, 'main/index.html', { "categories" : categories , "images" : images, "locations" : locations} )

def imagePage(request, image_id):
    
    try:
        image = Image.objects.get(id=image_id)

    except Image.DoesNotExist:
        raise Http404()

    return render(request, 'main/image.html', {"image" : image})        

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



