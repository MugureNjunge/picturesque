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

# def search_results(request):
  
#     if 'category' in request.GET and request.GET["category"]:
#         search_term = request.GET.get("category")
#         searched_categories = Category.search_by_title(search_term)
#         message = f"{search_term}"

#         return render(request, 'main/search.html',{"message":message,"articles": searched_articles})

#     else:
#         message = "You haven't searched for any category"
#         return render(request, 'main/search.html',{"message":message})


