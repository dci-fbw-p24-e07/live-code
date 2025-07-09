from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.blog_list, name="blog-list"),
    path("books/", views.BooksView.as_view(), name="books-list"),
    path("authors/", views.AuthorView.as_view(), name="author-list"),
    path("<int:blog_id>/", views.blog_detail, name="blog-detail"),
    
]
