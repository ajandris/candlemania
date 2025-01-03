from django.shortcuts import render
from django.contrib.auth.models import User

"""
Home page functions
"""
def index(request):
    context = {
        "active_menu": "home"
    }
    return render(request, 'main/index.html', context=context)

def about(request):
    context = {
        "active_menu": "about"
    }
    return render(request, 'main/about.html', context=context)
