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


def search_results(request):
  
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'photoapp/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'photoapp/search.html',{"message":message})


