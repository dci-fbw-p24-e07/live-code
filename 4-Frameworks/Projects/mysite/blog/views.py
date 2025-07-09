from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.http import HttpResponse
from .models import BlogPosts, Book, Author


def blog_list(request):
    # Fetch all blogs and their related authors
    blogs = BlogPosts.objects.select_related('author').all()
    
    return render(request, "blog_list.html", context={"blogs": blogs})


def blog_detail(request, blog_id):
    blog = BlogPosts.objects.get(pk=blog_id)
    content = blog.body
    return HttpResponse(content)
    

class BooksView(View):
    
    def get(self, request):
        books = Book.objects.select_related('author').all()
        return render(request, "books.html", {"books": books})    


class AuthorView(TemplateView):
    template_name = "author_list.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['authors'] = Author.objects.all()
        return context
