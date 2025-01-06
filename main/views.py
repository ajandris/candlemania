from django.shortcuts import render
from blog.models import BlogPost, BlogComment

"""
Home page functions
"""
def index(request):
    blogs = BlogPost.objects.filter(approved='True').order_by("-updated_at")[:8]
    comments = BlogComment.objects.filter(approved='True').order_by("-updated_at")[:8]
    context = {
        "active_menu": "home",
        "blogs": blogs,
        "comments": comments
    }
    return render(request, 'main/index.html', context=context)

def about(request):
    context = {
        "active_menu": "about"
    }
    return render(request, 'main/about.html', context=context)


def search_site(request):
    prev_search = "" if not request.GET.get('search_criteria') else request.GET.get('search_criteria')
    context = {
        "active_menu": "home",
        "prev_search_criteria": prev_search
    }
    return render(request, 'main/search.html', context=context)
