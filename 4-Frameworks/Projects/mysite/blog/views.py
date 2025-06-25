from django.shortcuts import render
from django.http import HttpResponse


def blog_list(request):
    return HttpResponse("<h2>All Blog Posts</h2>")