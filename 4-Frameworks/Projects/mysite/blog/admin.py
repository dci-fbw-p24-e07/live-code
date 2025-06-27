from django.contrib import admin

# Import the desired models
from .models import BlogPosts

admin.site.register(BlogPosts)
