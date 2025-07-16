from django.shortcuts import render, redirect
from .forms import RegisterForm


def register(request):
    # Check if the form has been submitted
    if request.method == "POST":
        # inputting submitted info to the form
        form = RegisterForm(request.POST)
        # Check if the form is valid
        if form.is_valid():
            form.save()
            # Redirect to home page
            return redirect("core:home")
    else:
        form = RegisterForm()
        return render(request, "users/register.html", {"form": form})
