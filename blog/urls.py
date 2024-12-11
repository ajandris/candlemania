from django.urls import path, include
from django.shortcuts import render

from . import views

"""
Main URL patterns
"""
urlpatterns = [
    path('', views.blog_index, name='blog-home'),
]

