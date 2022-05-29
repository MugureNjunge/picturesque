from django.urls import path
from . import views

urlpatterns = [
  path('',views.home, name='home'),
  path('category/',views.categoryPage , name='image-category'),
  path('category/', views.imageDetailPage, name='image-detail'),

  # path('search/', views.search_results, name='search-results')
]



