# Car Rental System

- A project that manages rentals, users and payments for a car rental company.

## Step 1: Setup

1. Create the Project Folder

    ```shell
    mkdir car_rental
    cd car_rental
    ```

2. Create and activate the virtual environment:

    ```shell
    python3 -m venv .venv --prompt=car-rental-env

    # Linux
    source .venv/bin/activate

    # Windows 
    .venv\Scripts\activate
    ```

3. Install Django

    ```shell
    pip install Django
    ```

    - Use `pip freeze > requirements.txt` to track the installed packages

## Step 2: Project Structure

- Define the project and app folders that align with the requirements of the system

    ```shell
    # Create project
    django-admin startproject config .

    # Create the apps
    django-admin startapp core  # Houses common functionality and pages
    django-admin startapp users #  Manages user accounts
    django-admin startapp cars # Manages the car inventory
    django-admin startapp bookings # Manages the rental bookings
    django-admin startapp payments # Manages payment confirmation and history
    ```

    - Register the new apps in the `INSTALLED_APPS` setting

        ```python
        INSTALLED_APPS = [
            # other apps... 
            "core.apps.CoreConfig",
            "users",
            "cars",
            "bookings",
            "payments",
        ]
        ```

## Step 3: User Authentication

- Django uses a built-in authentication system, that is also customizable
- In order to allow for easy easy customization or future modification you must create a Custom User model that inherits from the `AbstractUser` class
- This will ensure that the built-in user managers and any other functionality tied to authentication is brought in to your custom model.

1. Create a custom user model:

    ```python
    from django.contrib.auth.models import AbstractUser
    from django.db import models

    class CustomUser(AbstractUser):
        pass
    ```

2. Update the `settings.py`:

    - Indicate which model to use for the authentication system

    ```python
    AUTH_USER_MODEL = "users.CustomUser"
    ```

3. Create the registration and login views:

    1. Registration:

        1. Create a user registration form:

            - Create the file `forms.py` in the `users` app

                ```python
                from django import forms
                from django.contrib.auth.forms import UserCreationForm
                from .models import CustomUser

                class RegisterForm(UserCreationForm):
                    # Using the built-in form field to add validation
                    email = forms.EmailField()

                    class Meta:
                        model = CustomUser
                        fields = ["first_name", "last_name", "username", "email", "password1", "password2"]
                ```
        
        2. Create the registration view in `users.views.py`:

            ```python
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
            ```
    
    2. Login:

        - Django has built-in authentication urls. In order to utilize these you just need to include them in your `urls.py` file
        - These urls are tied to built-in authentication views that look for templates inside a folder called `registration`

        ```python
        # users/urls.py 

        from django.urls import path, include

        app_name = "users"

        urlpatterns = [
            # ... 
            path("", include("django.contrib.auth.urls"))
        ]
        ```

## Step 4: Templates and URLs configuration

1. Create the templates folder in the root directory:

    ```shell
    mkdir templates
    ```

2. Setup folders for each app inside the templates directory:

    ```shell
    cd templates
    mkdir users
    mkdir bookings
    mkdir cars
    mkdir core
    mkdir payments
    mkdir registration # for the built-in authentication urls
    ```

3. Change the `TEMPLATES` setting to point to the new `templates folder:

    ```python
    TEMPLATES = {
        # Other settings
        "DIRS": [BASE_DIR/"templates"],
        # .... 
    }

