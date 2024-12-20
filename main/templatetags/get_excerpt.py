"""
    gets the excerpt with given length from HTML formatted text
"""
import re
from django import template

register = template.Library()

@register.filter(name='get_excerpt')
def get_excerpt(html_text, length):
    clean = re.compile('<.*?>')
    cleaned = clean.sub('', html_text)
    cleaned = cleaned.replace("&lt;", "").replace("&gt;", "")
    return cleaned[:length]
