from django.contrib import admin
from blog.models import BlogComment, BlogPost


@admin.register(BlogComment)
class BlogCommentAdmin(admin.ModelAdmin):
    pass

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    pass