"""
Module: errors.py
Description: custom error page handling
"""
from django.shortcuts import render


def custom_404(request, exception):
    """
    Custom 404 error page
    """
    return render(request, 'error/404.html', status=404)
