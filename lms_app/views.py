from django.shortcuts import render
from .models import *
from. forms import BookForm

# Create your views here.
def books(requset):
    context = {
        'category' : Category.objects.all(),
        'books' : Book.objects.all(),
        'form' : BookForm(),
    }
    return render(requset,'pages/books.html', context)

def delete(requset):
    return render(requset,'pages/delete.html')

def index(requset):
    context = {
        'category' : Category.objects.all(),
        'books': Book.objects.all(),
        'form' : BookForm(),

    }
    return render(requset,'pages/index.html', context)

def update(requset):
    return render(requset,'pages/update.html')