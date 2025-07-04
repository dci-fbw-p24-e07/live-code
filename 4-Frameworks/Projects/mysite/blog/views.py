from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogPosts, Book


def blog_list(request):
    # Fetch all blogs and their related authors
    blogs = BlogPosts.objects.select_related('author').all()
    
    context = ""
    
    # Iterate over the blogs
    for blog in blogs:
        
        context += f"<li>{blog.title} - {blog.author.first_name}</li>"  # No additional queries executed
    return HttpResponse(f"<h2>All Blog Posts</h2></br><ul>{context}</ul>")


def blog_detail(request, blog_id):
    blog = BlogPosts.objects.get(pk=blog_id)
    content = blog.body
    return HttpResponse(content)
    