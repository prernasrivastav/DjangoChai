from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse("Hello, Welcome to Home page!")
    return render(request, 'website/index.html')

def about(reuest):
    return HttpResponse("Hello, Welcome to About page!")

def contact(reuest):
    return HttpResponse("Hello, Welcome to Contact page!")