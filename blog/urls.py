from django.urls import path, include
from django.shortcuts import render

from . import views

"""
Main URL patterns
"""
urlpatterns = [
    path('', views.blog_index, name='blog-home'),
    path('new/', views.blog_new, name='blog-new'),
    path('update/', views.blog_update, name='blog-update'),
    path('delete/', views.blog_delete, name='blog-delete'),
    path('approve/', views.blog_approve, name='blog-approve'),
    path('myblogs/', views.blog_my, name='blog-my'),
]

