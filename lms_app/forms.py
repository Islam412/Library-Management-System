from django import forms
from .models import Book , Category



class BookForm(forms.ModelForm):
    
    class Meta:
        model = Book
        fields = [
            'title',
            'author',
            'photo_book',
            'photo_author',
            'pages',
            'price',
            'retal_price_day',
            'retal_period',
            'active',
            'status',
            'category',
        ]
    widgets = {
        'title' : forms.TextInput(attrs={'class':'from-control'}),
    }    



class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['name']
    widgets = {
        'name' : forms.TextInput(attrs={'class':'from-control'}),
    }