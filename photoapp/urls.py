from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
  path('',views.home, name='home'),
  path('search', views.search, name='search'),
  path('category/<int:category_id>/',views.categoryPage , name='image-category'),
  path('location/<int:location_id>/',views.locationPage , name='image-location'),
  path('image/', views.imagePage, name='image-details'),
  path('search/', views.search, name='search'),
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)






