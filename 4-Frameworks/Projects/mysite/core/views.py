from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("Welcome to the Homepage")

def about(request):
    return HttpResponse("<h3>This is the about page</h3>")

# contact
def contact(request):
    return HttpResponse("Contact Page")

# faq
def faq(request):
    return HttpResponse("Frequently Asked Questions")
