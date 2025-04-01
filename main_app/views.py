from django.shortcuts import render
from .models import Cat
from django.http import HttpResponse

# Create your views here.
def cat_index(request):
    cats = Cat.objects.all()  # look familiar?
    return render(request, 'cats/index.html', {'cats': cats})

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cat_index(request):
    # Render the cats/index.html template with the cats data
    cat = Cat.objects.all()
    return render(request, 'cats/index.html', {'cats': cat})

def cat_detail(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    return render(request, 'cat/detail.html', {'cat': cat})