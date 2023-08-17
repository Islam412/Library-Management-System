from django.shortcuts import render, redirect
from .models import *
from. forms import BookForm, CategoryForm
from django.views.generic import DeleteView
# Create your views here.
def books(requset):
    if requset.method == 'POST':
        add_Category= CategoryForm(requset.POST)
        if add_Category.is_valid():
             add_Category.save()
    
    context = {
        'category' : Category.objects.all(),
        'books' : Book.objects.all(),
        'category' : Category.objects.all(),
        'forms' : CategoryForm(),
    }
    return render(requset,'pages/books.html', context)




def index(requset):
    if requset.method == 'POST':
        add_Category= CategoryForm(requset.POST)
        if add_Category.is_valid():
             add_Category.save()
    
    if requset.method == 'POST':
        add_book = BookForm(requset.POST, requset.FILES)
        if add_book.is_valid():
            add_book.save()
    context = {
        'category' : Category.objects.all(),
        'books': Book.objects.all(),
        'form' : BookForm(),
        'forms' : CategoryForm()

    }
    return render(requset,'pages/index.html', context)



def update(requset, id):
    book_id = Book.objects.get(id = id)
    if requset.method == 'POST':
        book_save = BookForm(requset.POST, requset.FILES, instance=book_id)
        if book_save.is_valid():
            book_save.save()
            return redirect('/')
    else:
        book_save = BookForm(instance=book_id)
    context = {
        'form':book_save,
    }
    return render(requset, 'pages/update.html', context)



class delete_Book(DeleteView):
    model = Book
    template_name = 'delete.html'
    success_url ='/'

