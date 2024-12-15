from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, reverse, get_object_or_404, redirect
from .forms import BlogPostForm
from .models import BlogPost


"""
Blog functions
"""
def blog_index(request):
    blogs = BlogPost.objects.all().filter(approved=True).order_by('-updated_at')

    paginator = Paginator(blogs, 4)
    page = request.GET.get('page')
    try:
        pages = paginator.page(page)
    except PageNotAnInteger:
        pages = paginator.page(1)  # If page is not an integer, deliver the first page.
    except EmptyPage:
        pages = paginator.page(paginator.num_pages)  # If page is out of range, deliver the last page of results.

    context = {
        "active_menu": "blog",
        "blogs": pages,
        "pages": pages
    }
    return render(request, 'blog/blog-home.html', context=context)

def blog_new(request):

    if request.method == 'GET':
        form = BlogPostForm(label_suffix="")
        context = {
            "active_menu": "blog",
            "form": form,
            "action_url": reverse("blog-new")
        }
        return render(request, 'blog/blog-new.html', context=context)
    elif request.method == 'POST':
        form = BlogPostForm(request.POST, label_suffix="")
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.save()
            messages.success(request, 'Your data has been saved successfully!')
        else:
            messages.error(request, 'There was an error saving your data.')
            context = {
                "active_menu": "blog",
                "form": form,
            }
            return render(request, 'blog/blog-new.html', context=context)

    return redirect('blog-home')


def blog_update(request, blog_slug):
    pass

def blog_delete(request, blog_slug):
    pass

def blog_approve(request, blog_slug):
    pass

def blog_my(request, blog_slug):
    pass


