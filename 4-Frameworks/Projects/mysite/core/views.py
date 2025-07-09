from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


# def home(request):
#     return HttpResponse("Welcome to the Homepage")

class HomeView(TemplateView):
    template_name = "home.html"

def about(request):
    return HttpResponse("<h3>This is the about page</h3>")

# contact
def contact(request):
    return HttpResponse("Contact Page")

# faq
def faq(request):
    return HttpResponse("Frequently Asked Questions")
