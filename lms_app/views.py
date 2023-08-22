from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DeleteView
from .models import *
from .models import Book
from. forms import *




# Create your views here.
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
        'forms' : CategoryForm(),
        'allbooks' : Book.objects.filter(active=True).count(),
        'booksold' : Book.objects.filter(status='sold').count(),
        'bookrented' : Book.objects.filter(status='rented').count(),
        'bookavailable' : Book.objects.filter(status='available').count(),

    }
    return render(requset,'pages/index.html', context)




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



def delete_book(request, id):
        book_delete = get_object_or_404(Book, id=id)
        book_delete.delete()
        return redirect('/')  # Redirect to a success page


'''
def delete_book(requset, id):
        book_delete = get_object_or_404(Book, id = id)
        if requset.method == 'POST':
            book_delete.delete()
            return redirect('/') 
        return render(requset, 'pages/delete.html')
'''