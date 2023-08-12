from django.shortcuts import render

# Create your views here.

def books(requset):
    return render(requset,'pages/books.html')

def delete(requset):
    return render(requset,'pages/delete.html')

def index(requset):
    return render(requset,'pages/index.html')

def update(requset):
    return render(requset,'pages/update.html')