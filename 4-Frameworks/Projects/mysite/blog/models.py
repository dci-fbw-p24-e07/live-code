from django.db import models


class BlogPosts(models.Model): 
    title = models.CharField(max_length=100) # varchar or char
    body = models.TextField() # text
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"
        ordering = ["created_at"]
        
    def __str__(self):
        return str(self.title)
    

class Book(models.Model):
    name = models.CharField(max_length=350)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    

class BookData(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    chapter_name = models.CharField(max_length=250)
