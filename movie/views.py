from django.shortcuts import render
from django.http import HttpResponse
from .models import movie

def home(request):
    #return HttpResponse('<h1>Welcome to Home Page<h1>')
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movies = movie.objects.filter(title__icontains = searchTerm)
    else: 
        movies = movie.objects.all()
    return render(request, 'home.html', {'searchTerm': searchTerm, 'movies': movies})
# Create your views here.


def about(request):
    return render(request, 'about.html', {'name': 'Luisa María Alvarez'})