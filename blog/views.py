from django.shortcuts import render

"""
Blog functions
"""
def blog_index(request):
    return render(request, 'blog/blog-home.html')
