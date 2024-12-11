from django.urls import path

from .views import index

"""
Main URL patterns
"""
urlpatterns = [
    path('', index, name='home'),
]

