from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
  path('',views.home, name='home'),
  path('category/<int:category_id>/',views.categoryPage , name='image-category'),
  path('image/', views.imageDetailPage, name='image-detail'),

  # path('search/', views.search_results, name='search-results')
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)






