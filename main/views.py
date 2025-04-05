from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def mainpage(request):
    return render(request, 'main/mainpage.html')

def secondpage(request):
    return render(request, 'main/secondpage.html')
