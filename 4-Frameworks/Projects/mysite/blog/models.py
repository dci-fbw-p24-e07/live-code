from django.db import models


class BlogPosts(models.Model):
    title = models.CharField(max_length=100) # varchar or char
    body = models.TextField() # text
    created_at = models.DateTimeField(auto_now=True)
    
