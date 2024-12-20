from django.urls import path

from . import views

"""
Main URL patterns
"""
urlpatterns = [
    path('', views.blog_index, name='blog-home'),
    path('new/', views.blog_new, name='blog-new'),
    path('post/<slug:slug>/', views.blog_post, name='blog-post'),
    path('update/', views.blog_update, name='blog-update'),
    path('delete/', views.blog_delete, name='blog-delete'),
    path('approve/', views.blog_approve, name='blog-approve'),
    path('approvelist/', views.blog_approve_list, name='blog-approve-list'),
    path('myblogs/', views.blog_my, name='blog-my'),
]
