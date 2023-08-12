from django.urls import path
from . import views


urlpatterns = [
    path('books',views.books,name='books'),
    path('delete',views.delete,name='delete'),
    path('',views.index,name='index'),
    path('update',views.update,name='update'),
]

