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
            'total_render',
            'active',
            'status',
            'category',
        ]
    widgets = {
        'title' : forms.TextInput(attrs={'class':'from-control'}),
        'author' : forms.TextInput(attrs={'class':'from-control'}),
        'photo_book' : forms.FileInput(attrs={'class':'from-control'}),
        'photo_author' : forms.FileInput(attrs={'class':'from-control'}),
        'pages' : forms.NumberInput(attrs={'class':'from-control'}),
        'price' : forms.NumberInput(attrs={'class':'from-control'}),
        'retal_price_day' : forms.NumberInput(attrs={'class':'from-control', 'id' : 'rentalprice'}),
        'retal_period' : forms.NumberInput(attrs={'class':'from-control', 'id' : 'rentalday'}),
        'total_render' : forms.NumberInput(attrs={'class':'from-control', 'id' : 'rentaltotal'}),
        'active' : forms.TextInput(attrs={'class':'from-control'}),
        'status' : forms.Select(attrs={'class':'from-control'}),
        'category' : forms.Select(attrs={'class':'from-control'}),
        
    }    



class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['name']
    widgets = {
        'name' : forms.TextInput(attrs={'class':'from-control'}),
    }