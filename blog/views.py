""""
Module name views.py

Module description: views for the blog app

"""
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import Http404
from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import BlogPostForm
from .models import BlogPost, BlogComment


GRID_ITEMS_PER_PAGE = 8
LIST_ITEMS_PER_PAGE = 10


def blog_index(request):
    """
    Blog home page
    """
    blogs = BlogPost.objects.all().filter(approved=True). \
        order_by('-updated_at')

    paginator = Paginator(blogs, GRID_ITEMS_PER_PAGE)
    page = request.GET.get('page')

    try:
        pages = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page.
        pages = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver the last page of results.
        pages = paginator.page(paginator.num_pages)

    context = {
        "active_menu": "blog",
        "blogs": pages,
        "pages": pages
    }
    return render(request, 'blog/blog-home.html', context=context)


@login_required
def blog_new(request):
    """
    New blog page
    """
    if request.method == 'GET':
        form = BlogPostForm(label_suffix="")
        context = {
            "active_menu": "blog",
            "form": form,
            "action_url": reverse("blog-new")
        }
        return render(request, 'blog/blog-new.html', context=context)
    if request.method == 'POST':
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

    return redirect('blog-my')


def blog_detail(request, slug):
    """
    Blog detail page
    """
    blog = get_object_or_404(BlogPost, slug=slug)
    comments = BlogComment.objects.filter(blog_post=blog). \
        order_by('-created_at')
    public_comments = BlogComment.objects. \
        filter(blog_post=blog, approved=True).order_by('-created_at')
    context = {
        "active_menu": "blog",
        "blog": blog,
        "comments": comments,
        "public_comments": public_comments
    }
    return render(request, 'blog/blog-detail.html', context=context)


@login_required
def blog_update(request):
    """
    Blog edit page
    """
    if request.method == 'POST':
        action = request.POST.get('action') \
         if request.POST.get('action') else ""
        if action == 'to_update':
            # before update
            blog_to_update = get_object_or_404(BlogPost,
                                               slug=request.POST['key'],
                                               author=request.user)
            form = BlogPostForm(instance=blog_to_update, label_suffix="")
            context = {
                "active_menu": "blog",
                "form": form,
                "action": "update",
                "key": blog_to_update.slug
            }
            return render(request, 'blog/blog-update.html', context=context)
        if action == 'update':
            # Update data
            slug = request.POST['key'] if request.POST.get('key') else ""
            old_data = get_object_or_404(BlogPost, slug=slug)
            form = BlogPostForm(request.POST, instance=old_data,
                                label_suffix="")
            if form.is_valid():
                blog_post = form.save(commit=False)
                if form.cleaned_data['title'] != form.initial['title']:
                    blog_post.slug = None
                blog_post.approved = False
                blog_post.save()
                messages.success(request,
                                 'Your data has been saved successfully!')
                return redirect('blog-my')
            messages.error(request, 'There was an error saving your data.')
            context = {
                "active_menu": "blog",
                "form": form,
                "action": "update"
            }
            return render(request, 'blog/blog-update.html', context=context)
        raise Http404("Wrong action")

    raise Http404("Wrong request method")


@login_required
def blog_delete(request):
    """
    Delete blog page
    """
    if request.method == "POST":
        action = request.POST.get("action")
        blog_post = get_object_or_404(BlogPost,
                                      slug=request.POST.get("key"))
        if action == "to_delete":
            context = {
                "active_menu": "blog",
                "blog": blog_post
            }
            return render(request, template_name='blog/blog-delete.html',
                          context=context)
        if action == "delete":
            blog_post.delete()
            messages.success(request, 'Data deleted successfully!')
            return redirect('blog-my')
        # no action or wrong action
        return redirect("blog-home")

    raise Http404("Wrong request method")


@login_required
def blog_approve(request):
    """
    Blog approve page
    """
    if request.method == "POST":
        action = request.POST.get("action")
        blog_post = get_object_or_404(BlogPost, slug=request.POST.get("key"))
        if action == "to_approve":
            context = {
                "active_menu": "blog",
                "blog": blog_post
            }
            return render(request, template_name='blog/blog-approve.html',
                          context=context)
        if action == "approve":
            blog_post.approved = True
            blog_post.save()
            messages.success(request, 'Data saved successfully!')
            return redirect('blog-approve-list')
        # no action or wrong action
        return redirect("blog-home")

    raise Http404("Wrong request method")


@login_required
def blog_my(request):
    """
    Current registered user's blogs
    """
    blogs = BlogPost.objects.all().filter(author=request.user). \
        order_by('-updated_at')
    paginator = Paginator(blogs, GRID_ITEMS_PER_PAGE)
    page = request.GET.get('page')

    try:
        pages = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page.
        pages = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver the last page of results.
        pages = paginator.page(paginator.num_pages)

    context = {
        "active_menu": "blog",
        "blogs": pages,
        "pages": pages
    }
    return render(request, 'blog/blog-my.html', context=context)


@login_required
def blog_approve_list(request):
    """
    Blog to approve list
    """
    blogs = BlogPost.objects.all().filter(approved=False). \
        order_by('-updated_at')
    paginator = Paginator(blogs, GRID_ITEMS_PER_PAGE)
    page = request.GET.get('page')

    try:
        pages = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page.
        pages = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver the last page of results.
        pages = paginator.page(paginator.num_pages)

    context = {
        "active_menu": "blog",
        "blogs": pages,
        "pages": pages
    }
    return render(request, 'blog/blog-approve-list.html', context=context)


@login_required
def comment_add(request):
    """
    New comment page
    """
    if request.method == 'POST':
        blog = get_object_or_404(BlogPost, slug=request.POST['blog_slug'])
        comment_object = BlogComment()
        comment_object.content = request.POST['comment']
        comment_object.blog_post = blog
        comment_object.author = request.user
        comment_object.approved = False
        comment_object.save()

        messages.success(request,
                         'Comment added successfully. Wait for approval.')

        return redirect('blog-post', slug=blog.slug)

    raise Http404("Wrong request method")


@login_required
def comment_delete(request):
    """
    Delete comment page
    """
    if request.method == 'POST':
        comment_object = get_object_or_404(BlogComment,
                                           pk=request.POST['comment_id'])
        comment_object.delete()
        messages.success(request, 'Comment deleted successfully.')
        return redirect('blog-post', slug=comment_object.blog_post.slug)

    raise Http404("Wrong request method")


@login_required
def comment_approve(request):
    """
    Approve comment page
    """
    if request.method == 'POST':
        comment_object = get_object_or_404(BlogComment,
                                           pk=request.POST['comment_id'])
        comment_object.approved = True
        comment_object.save()
        messages.success(request, 'Comment Approved.')
        return redirect('blog-post', slug=comment_object.blog_post.slug)

    raise Http404("Wrong request method")
