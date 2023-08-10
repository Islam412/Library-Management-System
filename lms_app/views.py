from django.shortcuts import render

# Create your views here.

def demo(requset):
    return render(requset,'pages/index.html')