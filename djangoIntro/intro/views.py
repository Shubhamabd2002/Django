from django.shortcuts import render

# Create your views here.

def all_intro(request):
    return render(request, 'intro/all_intro.html')
