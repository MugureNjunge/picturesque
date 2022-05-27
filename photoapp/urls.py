from django.urls import pathfrom

from photoapp import path
from . import views

urlpattersn = [
  path('',views.home, name='home'),

]