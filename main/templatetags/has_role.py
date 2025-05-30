"""
    Checks if the user has specified role on the web page
    Usage: template filter
"""
from django import template

register = template.Library()


@register.filter(name='has_role')
def has_role(user, role_name):
    """
    Returns True if the user has specified role
    """
    return user.groups.filter(name=role_name).exists()
