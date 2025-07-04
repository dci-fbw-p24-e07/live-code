from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.blog_list, name="blog-list"),
    path("<blog_id>/", views.blog_detail, name="blog-detail"),
]
