"""
URL configuration for candlemania project.

"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from . import settings

# Custom error 404 (Page not found)
handler404 = 'candlemania.errors.custom_404'


"""
Main URL patterns
"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('accounts/', include('allauth.urls')),
    path('blogs/', include('blog.urls')),
    path('', include('main.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATICFILES_DIRS[0])
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
