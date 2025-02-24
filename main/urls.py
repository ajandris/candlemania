"""
Module: urls.py

Description: Main URL Configuration
"""

from django.urls import path

from .views import index, about, search_site

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('search/', search_site, name='search')
]
