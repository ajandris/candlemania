"""
    gets the excerpt with given length from HTML formatted text
"""
import re
from django import template
from bs4 import BeautifulSoup

register = template.Library()

@register.filter(name='get_excerpt')
def get_excerpt(html_text, length):
    soup = BeautifulSoup(html_text, features="html.parser")
    clean = re.compile('<.*?>')
    cleaned = clean.sub('', html_text)
    cleaned = cleaned.replace("&lt;", "").replace("&gt;", "")
    return cleaned[:length]
