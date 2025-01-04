from django.urls import path

from .views import index, about

"""
Main URL patterns
"""
urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
]

