from django.contrib import admin
from .models import Post
from django.shortcuts import redirect
from django.contrib.auth import logout as auth_logout

# Register your models here.
admin.site.register(Post)

# chage the admin site title
admin.site.site_header = 'Log In'

# redirect to the home page
class CustomAdminSite(admin.AdminSite):
    def logout(self, request, extra_context=None):
        auth_logout(request)
        return redirect('home')
    
# Create an instance of the custom admin site
custom_admin_site = CustomAdminSite(name='custom_admin')

# Copy registered models from the default admin site
custom_admin_site._registry.update(admin.site._registry)