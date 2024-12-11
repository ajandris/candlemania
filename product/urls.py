from django.urls import path, include
from django.shortcuts import render

from . import views

"""
Main URL patterns
"""
urlpatterns = [
    path('', views.product_index, name='product-home'),
]

