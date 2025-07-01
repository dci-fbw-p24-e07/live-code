from django.contrib import admin

# Import the desired models
from .models import BlogPosts, Book, BookData

admin.site.register(BlogPosts)
admin.site.register(Book)
admin.site.register(BookData)
