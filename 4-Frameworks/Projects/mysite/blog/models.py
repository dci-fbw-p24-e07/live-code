from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class BlogPosts(models.Model): 
    title = models.CharField(max_length=100) # varchar or char
    body = models.TextField() # text
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="blogs", null=True)
    
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
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books", null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['name'], name="book_name_idx"),
            models.Index(fields=['price'], name="book_price_idx")
        ]
        constraints = [
            models.CheckConstraint(condition=models.Q(pages__gte=50), name="pages_gte_50"),
            # Check that the price is not above 100
            models.CheckConstraint(condition=models.Q(price__lte=100), name="price_lte_100")
        ]
    
    def save(self, **kwargs):
        if "Java".lower() in self.name.lower():
            return "We don't like Java over here"
        else:
            # Call the actual save method
            super().save(**kwargs)
        
    def price_status(self):
        """ 
        Returns the price status of a book
        """
        
        if self.price >= 65:
            return "Expensive"
        elif self.price >= 35 and self.price <= 64:
            return "Affordable"
        elif self.price <= 34:
            return "Cheap"
    

class BookData(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    chapter_name = models.CharField(max_length=250)
    
    class Meta:
        db_table = "_book_data"
    
        