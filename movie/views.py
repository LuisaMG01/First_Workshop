from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    #return HttpResponse('<h1>Welcome to Home Page<h1>')
    return render(request, 'home.html', {'name': 'Luisa María'})
# Create your views here.
