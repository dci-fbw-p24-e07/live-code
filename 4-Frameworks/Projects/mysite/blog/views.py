from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogPosts, Book


def blog_list(request):
    # Fetch all blogs and their related authors
    blogs = BlogPosts.objects.select_related('author').all()
    
    return render(request, "blog_list.html", context={"blogs": blogs})


def blog_detail(request, blog_id):
    blog = BlogPosts.objects.get(pk=blog_id)
    content = blog.body
    return HttpResponse(content)
    