import bleach
from bleach.css_sanitizer import CSSSanitizer
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from tinymce.models import HTMLField
from candlemania import settings
from main.utils import unique_slugify

"""
Blog Post
"""
class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts', db_comment="Author")
    title = models.CharField(max_length=250, blank=False, null=False, db_comment="Blog title")
    content = HTMLField(blank=False, null=False, db_comment="Blog post")
    slug = models.SlugField(max_length=255, blank=False, null=False, unique=True, db_comment="Blog post slug")
    approved = models.BooleanField(default=False, db_comment="Blog Approval status")
    created_at = models.DateTimeField(auto_now_add=True, db_comment="Created at")
    updated_at = models.DateTimeField(auto_now=True, db_comment="Updated at")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slugify(self, slugify(self.title))

        allowed_tags = settings.BLEACH_ALLOWED_TAGS
        allowed_attrs = settings.BLEACH_ALLOWED_ATTRIBUTES
        sanitiser = CSSSanitizer(allowed_css_properties=settings.BLEACH_ALLOWED_STYLES)
        self.content = bleach.clean(self.content, tags=allowed_tags, attributes=allowed_attrs, css_sanitizer=sanitiser)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'blog_posts'
        db_table_comment = 'Blogs Posts'


"""
Blog Post Comments
"""
class BlogComment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Comments', db_comment="Comment author")
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='Blog_comments', db_comment="Blog Post")
    content = models.TextField(blank=False, null=False, db_comment="Comment")
    approved = models.BooleanField(default=False, db_comment="Comment Approval status")
    created_at = models.DateTimeField(auto_now_add=True, db_comment="Created at")
    updated_at = models.DateTimeField(auto_now=True, db_comment="Updated at")

    def __str__(self):
        return self.content[:20]

    class Meta:
        db_table = 'blog_comments'
        db_table_comment = 'Blogs Post Comments'
