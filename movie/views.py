from django.shortcuts import render
from django.http import HttpResponse
from .models import movie

def home(request):
    #return HttpResponse('<h1>Welcome to Home Page<h1>')
    searchTerm = request.GET.get('searchMovie')
    
    return render(request, 'home.html', {'searchTerm': searchTerm})
# Create your views here.


def about(request):
    return render(request, 'about.html', {'name': 'Luisa María Alvarez'})