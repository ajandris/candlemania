from django.shortcuts import render
from django.contrib.auth.models import User

"""
Home page functions
"""
def index(request):
    contents = {
    }
    return render(request, 'main/index.html', context=contents)

