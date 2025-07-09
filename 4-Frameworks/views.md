# Views & Templates

## 08.07.25 - Views Basics

- What are views?
- The `request` object
- Function-based views
- Class-based views

### What are views?

- These are the request handlers of the project
- They essentially act as the middlemen between models and templates
- Since Django views are essentially the controllers they will possess a lot of the business logic
- Each view takes a users, fetches data from its models, applies business logic or processing and then prepares and returns an HTTP response to a template.

**The `request` object:**

- This is an instance of `HttpRequest` and serves as a central component in the request-response cycle. 
- When a client makes a HTTP Request to a Django application Django automatically creates and `HttpRequest` object to encapsulate all the information about that incoming request.
- The request object is then passed as the first argument to the corresponding view function or method.

### Function-based views

- Simple Python functions that that take in a request object and process the request then send out an HTTP Response.

```python
def <view-name>(request):
    # Business logic...
    return [HTTP-Response]
```

```python
def blog_detail(request, blog_id):
    blog = BlogPosts.objects.get(pk=blog_id)
    content = blog.body
    return HttpResponse(content)
```

**Template response:**

1. Create the templates folder in the app folder which you want to create templates for

    ```shell
    # Navigate to app directory
    cd blog

    # Create templates directory
    mkdir templates
    ```

2. Create a view and link it to a template

    ```python
    def blog_list(request):
        # Fetch all blogs and their related authors
        blogs = BlogPosts.objects.select_related('author').all()
        
        return render(request, "blog_list.html", context={"blogs": blogs})
    ```

3. Create the HTML pages for the templates:

    - We can use the Django Template language inside the HTML templates.
    - The Django template language embeds Python into HTML allowing you to perform Pythonic evaluations on the context you send to your templates.
    - It provides template tags, template variables and template filters that help to enrich the HTML

    1. Blog list:

        ```html
        <!DOCTYPE html>
        <html>
            <head>
                <meta charset="utf-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <title></title>
                <meta name="description" content="">
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <link rel="stylesheet" href="">
            </head>
            <body>
            <h2>Checkout Our Blogs</h2>
            <ul>
            {% for blog in blogs %} <!---template tag-->
                <li>{{ blog }} - {{blog.author.first_name}}</li> <!--- template variable --->
            {% endfor %}
            {% if %}
            </ul>
            </body>
        </html>
        ```

### Class-based views

- Django offers the ability to use class-based views as an alternative to function-based views.
- This can be achieved through inheriting one of the many View classes that Django offers:
    1. View (base)
    2. TemplateView
    3. DetailView - Get - Retrieve
    4. ListView - Get - Retrieve
    5. CreateView - Post - Create
    6. UpdateView - Put/Patch - Update

**View:**

- This the base view that django offers
- It allows to customize behaviour by tapping into different http methods
- This is done by defining class methods that have the exact name of the method you wish to customize(e.g `get`, `post`, `delete`, `put`, etc)

```python 
# views.py
from django.views import View

class MySampleView(View):

    def get(self, request):
        return render(request, "sample.html")
```

```python
# urls.py
from . import views

urlpatterns = [
    # existing paths.... 
    path("sample/", views.MySampleView.as_view(), name="sample-view")
]
```

- When calling a class based view in the urls you need to tap into the `as_view()` so that Django can translate it into a view.

- Retrieve all books from the `Book` model then send them to the template as context and display each book with its corresponding author in a list

## 09.07.25 - TemplateView and template tags & filters

- Using the TemplateView
- Utilising template tags and filters
- Using static files (css, javascript, etc)

### TemplateView

- This inherits from the base `View` class
- It allows you to render a template without writing extra lines of code
- In order to send context to the template you will need to overwrite the `get_context_data()` method

```python
from django.views.generic import TemplateView

class ExampleView(TemplateView):
    template_name = "example.html" # Point to the template

    def get_context_data(self, **kwargs):
        # Recreate the context
        context = super().get_context_data(**kwargs) # {}
        # Add new extra context
        context["sample_context"] = Book.objects.all()
        context["blogs"] = BlogPosts.objects.all()
        return context
```

- In the `core` app rewrite all the views to use the `TemplateView` class. They should still display the same information as before
- When \accessing the context from the template you would use the newly created key(in this example `sample_context`)

- Create a class called `AuthorsView` that uses the TemplateView and sends a list of all author to the template `author_list.html` and displays this as an ordered list
