from django.shortcuts import render
from .models import *

# Create your views here.

def books(requset):
    return render(requset,'pages/books.html')

def delete(requset):
    return render(requset,'pages/delete.html')

def index(requset):
    context = {
        'category' : Category.objects.all(),
        'books': Book.objects.all(),
    }
    return render(requset,'pages/index.html', context)

def update(requset):
    return render(requset,'pages/update.html')