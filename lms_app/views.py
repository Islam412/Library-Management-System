from django.shortcuts import render

# Create your views here.

def demo(requset):
    x={'name':'demo'}
    return render(requset,'demo.html',x)