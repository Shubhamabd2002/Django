from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse("Django Introduction Home page")
    return render(request, './website/index.html')

def about(request):
    return HttpResponse("Django Introduction About page")

def contact(request):
    return HttpResponse("Django Introduction Contact page")
