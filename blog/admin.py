"""
Module name: admin.py

Module description: Module provides interface for Candlemania
                    Blog models to be used in the admin interface.

"""
from django.contrib import admin
from blog.models import BlogComment, BlogPost


@admin.register(BlogComment)
class BlogCommentAdmin(admin.ModelAdmin):
    """
    Admin interface for BlogComment model
    """
    list_fields = [field.name for field in BlogComment._meta.get_fields()]


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    """
    Admin interface for BlogPost model
    """
    list_fields = [field.name for field in BlogPost._meta.get_fields()]
