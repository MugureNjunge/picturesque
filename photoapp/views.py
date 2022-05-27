from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    render(request, 'main/index.html', {})

