"""
Module name: apps.py

Module description: Provides functionality for blog field used with tinyMCE.

"""

from django.apps import AppConfig

class BlogConfig(AppConfig):
    """
    Configuration for model's BlogPost field blog
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
