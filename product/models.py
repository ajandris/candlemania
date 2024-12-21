import bleach
from bleach.css_sanitizer import CSSSanitizer
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from tinymce.models import HTMLField
from candlemania import settings
from main.utils import unique_slugify


class ProductCategory(models.Model):
    title = models.CharField(max_length=250, unique=True, blank=False, null=False, db_comment="Category title")
    slug = models.SlugField(unique=True, blank=False, null=False, db_comment="Slug")
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_comment="User who created record",
                             related_name="user_pc")
    created_at = models.DateTimeField(auto_now_add=True, db_comment="Creation datetime")
    updated_at = models.DateTimeField(auto_now=True, db_comment="Updated datetime")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slugify(self, slugify(self.title))

    class Meta:
        verbose_name_plural = "ProductCategories"
        db_table = 'product_categories'


class Product(models.Model):
    title = models.CharField(max_length=250, unique=True, blank=False, null=False, db_comment="Product title")
    slug = models.SlugField(unique=True, blank=False, null=False, db_comment="Slug")
    short_description = HTMLField(blank=False, null=False, db_comment="Product short description")
    description = HTMLField(blank=False, null=False, db_comment="Product description")
    tags = models.CharField(blank=True, null=True, db_comment="Tags", max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, db_comment="Product record owner",
                              related_name="product_owner")
    created_at = models.DateTimeField(auto_now_add=True, db_comment="Creation datetime")
    updated_at = models.DateTimeField(auto_now=True, db_comment="Updated datetime")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slugify(self, slugify(self.title))

        allowed_tags = settings.BLEACH_ALLOWED_TAGS
        allowed_attrs = settings.BLEACH_ALLOWED_ATTRIBUTES
        sanitiser = CSSSanitizer(allowed_css_properties=settings.BLEACH_ALLOWED_STYLES)
        self.description = bleach.clean(self.description, tags=allowed_tags, attributes=allowed_attrs,
                                        css_sanitizer=sanitiser)
        self.short_description = bleach.clean(self.short_description, tags=allowed_tags, attributes=allowed_attrs,
                                              css_sanitizer=sanitiser)
        super().save(*args, **kwargs)

    class Meta:
        db_table = "products"

class ProductFeedback(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, db_comment="Feedback Author", related_name="author")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, db_comment="Product", related_name="product_pf")
    rating = models.IntegerField(db_comment="Rating", default=1, null=False, blank=False)
    approved = models.BooleanField(db_comment="Approved", default=False)
    created_at = models.DateTimeField(auto_now_add=True, db_comment="Creation datetime")
    updated_at = models.DateTimeField(auto_now=True, db_comment="Updated datetime")

    class Meta:
        db_table = "product_feedbacks"


class AffiliatedProductSite(models.Model):
    site_name = models.CharField(max_length=100, unique=True, blank=False, null=False, db_comment="Affiliated site name")
    logo = models.ImageField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_comment="User who created the record",
                             related_name="user_aps")
    created_at = models.DateTimeField(auto_now_add=True, db_comment="Creation datetime")
    updated_at = models.DateTimeField(auto_now=True, db_comment="Updated datetime")

    class Meta:
        db_table = "affiliated_product_sites"

class AffiliatedProductLink(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, db_comment="Product", related_name="product_apl")
    affiliated_product_site = models.ForeignKey(AffiliatedProductSite, on_delete=models.CASCADE, )
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_comment="User who created the record",
                             related_name="user_apl")
    created_at = models.DateTimeField(auto_now_add=True, db_comment="Creation datetime")
    updated_at = models.DateTimeField(auto_now=True, db_comment="Updated datetime")

    class Meta:
        db_table = "affiliated_product_links"
