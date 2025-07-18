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

## Step 4: Templates, static files and URL configuration

### Templates

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

4. Create the `base.html` at the root of the `templates` directory:

    ```shell
    cd templates
    touch base.html
    ```

    ```html
    {% load static %}
    <!DOCTYPE html>
    <html>
    <head>
    <title>{% block title %} Car Rental {% endblock %}</title>
        <link rel="stylesheet" href="{% static 'css/main.css' %}">
    </head>
    <body>
    <header>
        <h1>🚗 Car Rental Booking System</h1>
        <nav>
        <a href="/">Home</a>
        <a href="/cars/">Cars</a>
        <a href="/bookings/">Bookings</a>
        </nav>
    </header>
    <div class="container">
        {% block content %}
        {% endblock %}
    </div>
    </body>
    </html>
    ```

### Static files

- Static files refers to JavaScript, CSS, Images, Videos, Fonts, etc.
- Any files to be used that will not be dynamically generated or altered by the application.
- 

1. Create the `static` folder at the root of the project:

    ```shell
    mkdir static
    ```

2. Create separate folders within the `static` directory to hold the different static files:

    ```shell
    cd static

    mkdir css
    mkdir js
    mkdir img
    ```

3. Update the `settings.py` file with the static files settings:

    ```python
    STATICFILES_DIRS = [BASE_DIR/"static"]
    ```

4. Update the html files to load any static files:

    - Django Template Language provides a special template tag that allows to load static files into your template
    - The `{% load static %}` tag is supposed at the top of your HTML file
    - It allows you enter a path to your desired static file

        ```html
        <link rel="stylesheet" href="{% static 'css/main.css' %}">
        <img src="{% static 'img/hello.png' %}">
        <script src="{% static 'js/script.js' %}"></script>
        ```

### URL's

- In order to avoid path collision you should a separate `urls.py` file in each Django app then include those urls into the `config/urls.py` file
- Ensure to use URL namespacing to create an extra level of specificity
- This will allow you to call URL's via the format `<namespace>:<path-name>` e.g `redirect("core:home")`

1. Create urls.py files in each app and give each of them a unique `app_name` variable

    ```python
    from django.urls import path
    from . import views

    app_name = "<app-name>"

    urlpatterns = [

    ]
    ```

2. Include those file in the main `urls.py` file ensuring to give the matching namespace attribute for each one

    ```python
    from django.urls import path, include

    urlpatterns = [
        # .... 
        path("bookings/", include("bookings.urls", namespace="bookings")),
        path("cars/", include("cars.urls", namespace="cars")),
        path("payments/", include("payments.urls", namespace="payments")),
        path("users/", include("users.urls", namespace="users")),
        path("", include("core.urls", namespace="core")),
    ]
    ```

## Step 5: Models and Database setup

### PostgreSQL DB Setup

1. Create a database in PostgreSQL

    ```shell
    # Login in to psql
    sudo -u postgres psql

    # Create database 
    CREATE DATABASE car_rental;
    ```

2. Create a user for the car rental and give them permissions to the DB:

    ```sql
    -- Create the user
    CREATE ROLE rental_admin WITH LOGIN PASSWORD 'rental_admin123';

    -- Grant user all privileges to the database
    GRANT ALL PRIVILEGES ON DATABASE car_rental TO rental_admin;

    GRANT ALL PRIVILEGES ON SCHEMA public TO rental_admin;
    ```

3. Change database settings:

    1. Install `psycopg2` and `python-dotenv`:

        ```shell
        pip install psycopg2 python-dotenv
        ```

        - do a `pip freeze`

    2. Create the `.env` file at the root of the project and add the following:

        ```env
        DB_NAME=<your-database-name>
        DB_USER=<your-database_user>
        DB_PASSWORD=<your-database-password>
        DB_HOST=<your-database=host>
        DB_PORT=<your-db-port>
        ```

    3. Add the `.env` file to `.gitignore`

    4. Update the database settings in the `settings.py` file:

        ```python
        import os
        from dotenv import load_dotenv

        load_dotenv()

        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': os.getenv('DB_NAME'),
                'USER': os.getenv('DB_USER'),
                'PASSWORD': os.getenv('DB_PASSWORD'),
                'HOST': os.getenv('DB_HOST'),
                'PORT': os.getenv('DB_PORT'),
            }
        }
        ```

### Models setup and migrations

1. Cars model

    ```python
    class Car(models.Model):

        class Type(models.TextChoices):
            SUV = ('SUV', 'Sport Utility Vehicle')
            SEDAN = ('SEDAN', 'Standard Sedan')
            HATCHBACK = ('HATCHBACK', 'Compact Hatchback')
            COUPE = ('COUPE', 'Two-door Coupe')
            CONVERTIBLE = ('CONVERTIBLE', 'Convertible')
            VAN = ('VAN', 'Van')
            MINIVAN = ('MINIVAN', 'Minivan')
            PICKUP_TRUCK = ('PICKUP_TRUCK', 'Pickup Truck')
            MOTORCYCLE = ('MOTORCYCLE', 'Motorcycle')

        name = models.CharField(max_length=100)
        brand = models.CharField(max_length=100)
        year = models.IntegerField()
        reg_number = models.CharField(max_length=20)
        vehicle_type = models.CharField(choices=Type.choices)
        vin_number = models.CharField(max_length=25)
        price = models.DecimalField(max_digits=10, decimal_places=2)
        availability = models.BooleanField(default=True)

        def __str__(self):
            return f"{self.year} {self.brand} {self.name} - {self.reg_number}"
    ```

2. Bookings model

    ```python
    from users.models import CustomUser
    from cars.models import Car


    class Booking(models.Model):
        customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
        car = models.ForeignKey(Car, on_delete=models.CASCADE)
        start_date = models.DateField()
        end_date = models.DateField()
        confirmed = models.BooleanField(default=False)

        def __str__(self):
            return f"{self.customer} - {self.car} - {self.start_date}"

        def total_days(self):
            return (self.end_date - self.start_date).days + 1

        def total_price(self):
            return self.total_days() * self.car.price
    ```

3. Payments model

    ```python
    from bookings.models import Booking

    class Payment(models.Model):

        class Status(models.TextChoices):
            SUCCESS = ('success', 'Success')
            FAILED = ('failed', 'Failed')
            PENDING = ('pending', 'Pending')

        booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
        amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
        payment_date = models.DateTimeField(auto_now_add=True)
        status = models.CharField(choices=Status.choices, default='pending')

        def __str__(self):
            return f"{self.booking} - {self.status}"
    ```

4. Create migration files and apply the migrations:

    ```shell
    python manage.py makemigrations

    python manage.py migrate
    ```

## Step 6: Views and Admin setup

### Admin interface

- Register all models in the admin panel:

1. CustomUser

    - in the `users/admin.py` file:

    ```python
    from .models import CustomUser

    admin.site.register(CustomUser)
    ```

2. Booking

    - In the `bookings/admin.py` file:

    ```python
    from .models import Booking

    admin.site.register(Booking)
    ```

3. Car

    - In the `cars/admin.py` file:

    ```python
    from .models import Car

    admin.site.register(Car)

4. Payment

    - In the `payments/admin.py` file:

    ```python
    from .models import Payment

    admin.site.register(Payment)
    ```

- Create a superuser and login to the admin interface

```shell
python manage.py createsuperuser
```

### Views

1. Home view

    - In the `core/views.py` file

        ```python
        def index(request):
            return render(request, "core/index.html")
        ```

    - Create the `index.html` file in the `templates/core/` directory:

        ```html
        {% extends 'base.html' %}
        {% block content %}
        <h2>Welcome to the Car Rental System</h2>
        <p>Browse and book available cars easily.</p>
        {% endblock %}
        ```

    - Create a URL path for the home page in `core/urls.py` file:

        ```python
        urlpatterns = [
            path("", views.index, name="index"),
        ]
        ```

2. Car list view

    - Create the `car_list` view in the `cars/view.py` file:

        ```python
        from .models import Car

        def car_list(request):
            cars = Car.objects.filter(availability=True)
            return render(request, "cars/list.html", {"cars": cars})
        ```

    - Create the `list.html` template in the `templates/cars` directory:

        ```python
        {% extends 'base.html' %}
        {% block title %} 
        Car Rental - Available Cars
        {% endblock %}
        {% block content %}
        <h2>Available Cars</h2>
        <table>
            <tr>
            <th>Name</th>
            <th>Brand</th>
            <th>Price/Day</th>
            <th>Action</th>
            </tr>
            {% for car in cars %}
            <tr>
            <td>{{ car.name }}</td>
            <td>{{ car.brand }}</td>
            <td>${{ car.price }}</td>
            <td><a href="{% url 'bookings:create' car.id %}"><button>Book Now</button></a></td>
            </tr>
            {% endfor %}
        </table>
        {% endblock %}
        ```

    - Create an apprpriate url path in the `cars/urls.py` file:

        ```python
        urlpatterns = [
            path("", views.car_list, name="list"),
        ]

3. Booking view - with a form

    - Create a `BookingForm` in the `bookings/forms.py`:

        ```python
        from django import forms
        from .models import Booking

        class BookingForm(forms.Form):
            start_date = forms.DateField(widget=forms.DateInput(attrs={
                "type": "date"}))
            end_date = forms.DateField(widget=forms.DateInput(attrs={
                "type": "date"}))

        # OR

        class BookingForm(forms.ModelForm):

            class Meta:
                model = Booking
                fields = ["start_date", "end_date"]
        ```

    - Create the `create_booking` view in the `bookings/views.py` file:

        ```python
        from django.shortcuts import render, redirect, get_object_or_404
        from .models import Booking
        from .forms import BookingForm
        from cars.models import Car

        def create_booking(request, car_id):
            # Retrieve the car
            car = get_object_or_404(Car, id=car_id)
            if request.method == "POST":
                form = BookingForm(request.POST)
                if form.is_valid():
                    # Get the date values
                    start_date = form.cleaned_data["start_date"]
                    end_date = form.cleaned_data["end_date"]

                    # Create the booking
                    booking = Booking.objects.create(
                        customer=request.user,
                        car=car,
                        start_date=start_date,
                        end_date=end_date,
                        confirmed=False
                    )
                    return redirect("payments:pay", booking.id)
            form = BookingForm()
            return render(request, "bookings/book.html", {
                "car": car, "form": form
            })
        ```

    - Create the `booking.html` template in the `templates/bookings/` directory:

        ```html
        {% extends 'base.html' %}

        {% block title %}
        Create Booking - {{ car }}
        {% endblock title %}

        {% block content %}
        <h2>Book Car: {{ car }}</h2>
        <form method="post">
            {% csrf_token %}
            <label>{{ form.start_date.label }}</label><br>
            {{ form.start_date }}
            <label>{{ form.end_date.label }}:</label><br>
            {{ form.end_date }}
            <button type="submit">Proceed to Payment</button>
        </form>
        {% endblock %}
        ```

    - Create an appropriate URL path:

        ```python
        urlpatterns = [
            path("create/<int:car_id>/", views.create_booking, name="create"),
        ]

4. Mock payment

    - In the `payments/views.py` create they `pay` view:

        ```python
        from django.shortcuts import render, redirect, get_object_or_404
        from bookings.models import Booking
        from payments.models import Payment

        def pay(request, booking_id):
            booking = get_object_or_404(Booking, id=booking_id)
            if request.method == "POST":
                Payment.objects.create(
                    booking=booking,
                    amount_paid=booking.total_price(),
                    status="success",
                )
                booking.confirmed = True
                booking.save()
                booking.car.availability = False
                return redirect("payments:success")
            return render(request, "payments/confirm_payment.html", {"booking": booking})
        ```

    - Create the file `confirm_payment.html` in the `templates/payments/` directory:

        ```html
        {% extends 'base.html' %}

        {% block title %}
        Car Rental - Confirm Payment
        {% endblock %}

        {% block content %}
        <h2>Confirm Payment</h2>
        <p>Car: {{ booking.car.name }}</p>
        <p>Total Days: {{ booking.total_days }}</p>
        <p>Total Amount: ${{ booking.total_price }}</p>
        <form method="post">
            {% csrf_token %}
            <button type="submit">Pay Now</button>
        </form>
        {% endblock %}
        ```

    - Create an appropriate URL in the `payments/urls.py` file:

        ```python
        urlpatterns = [
            path("confirm/<int:booking_id>/", views.pay, name="pay"),
        ]
        

5. Payment success
