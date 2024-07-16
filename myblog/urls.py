"""myblog URL Configuration"""

from django.contrib import admin
from django.urls import path, include, re_path
from . import views
from django.conf.urls.static import static
from django.views.static import serve
from django.conf import settings
from posts.admin import custom_admin_site

urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path('admin/', custom_admin_site.urls),
    path('', views.homepage, name='home'),
    path("posts/", include('posts.urls')),
    
    
]
