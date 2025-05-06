"""
URL Configuration for Blogs app
"""
from django.urls import path
from . import views


urlpatterns = [
    path('', views.blog_index, name='blog-home'),
    path('new/', views.blog_new, name='blog-new'),
    path('post/<slug:slug>/', views.blog_detail, name='blog-post'),
    path('update/', views.blog_update, name='blog-update'),
    path('delete/', views.blog_delete, name='blog-delete'),
    path('approve/', views.blog_approve, name='blog-approve'),
    path('approvelist/', views.blog_approve_list, name='blog-approve-list'),
    path('myblogs/', views.blog_my, name='blog-my'),
    path('commadd/', views.comment_add, name='comment-add'),
    path('commdel/', views.comment_delete, name='comment-delete'),
    path('commappr/', views.comment_approve, name='comment-approve'),
]
