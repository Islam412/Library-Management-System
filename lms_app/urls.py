from django.urls import path
from . import views


urlpatterns = [
    #path('<int:pk>/delete', delete_Book.as_view(),name='delete'),
    path('books',views.books,name='books'),
    path('',views.index,name='index'),
    path('update/<int:id>', views.update, name='update'),
]

