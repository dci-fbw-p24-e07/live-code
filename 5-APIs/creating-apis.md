# Creating REST API's

## Introduction

- What is Django Rest Framework?
- Setting up a DRF project
- Serializers and their role:
    - Serialization vs Deserialization
    - Data validation

### What is Django Rest Framework?

- It is a powerful and flexible toolkit for building Web APIs in Django. 
- It simplifies the process of creating robust and scalable APIs by providing reusable components and patterns.
- **Origins:** It was created in 2011 by Tom Christie as an open-source project to address the growing need to creat REST APis using Django.
- It has become the standard for API development using Django and is widely used in production environments
- There is a large ecosystem of third party packages created to enhance the development of APIs usig DRF

- At its core DRF integrates with Django's core features - models, views, and URLs -- making it simple and seamless to create a RESTful API.
- DRF is composed of the following components:
    1. **Serializers:**
        - These are used to convert Django Querysets and model instances to(serialization) and from(deserialization) JSON, XML, YAML, etc.
    2. **Views:**
        - These are similar to traditional Django views but handle RESTful HTTP request and responses.
        - The view itsefl will use serializers to validate incoming payloads and contains the necessary logic  to return a response
        - Views a coupled with routers, which map the views back to exposed URLs.

[Django REST Framework](https://www.django-rest-framework.org/)

### Setting up Django REST Framework

#### Step 1: Setting up the Python environment

1. Create the project folder:
    ```shell
    mkdir <project-name>
    cd <project-name>
    ```

2. Setup the virtual environment:
    ```shell
    python3 -m venv .venv --prompt=<project-name>
    ```

    - Activate the virtual environment:
        ```shell
        # Linux
        source .venv/bin/activate

        # Windows 
        .venv\Scripts\activate
        ```

3. Install Django and DRF:

    ```shell
    # Install Django
    pip install Django

    # Install Django Rest Framework
    pip install djangorestframework
    ```

    - Create a requirements file to store the currently installed packages
        ```shell 
        pip freeze > requirements.txt
        ```

#### Step 2: Create a Django project:

1. Create a new Django project:

    ```shell
    django-admin startproject config .
    ```

2. Activate the `rest_framework` app:

    - This is done by adding `rest_framework` to the the `INSTALLED_APPS` setting in the `settings.py` file:

        ```python
        INSTALLED_APPS = [
            # ...
            "rest_framework",
        ]
        ```

#### Step 3: Create a Django app

1. Create a new app:

    ```shell 
    django-admin startapp blog
    ```

2. Activate the app in `settings.py`:
    ```python
    INSTALLED_APPS = [
        # ....
        'blog'
    ]
    ```

#### Step 4: Model the data

1. Define the models:
    - In the `blog/models.py` file, create the `BlogPost` model:
        ```python
        class BlogPost(models.Model):
            title = models.CharField(max_length=200)
            content = models.TextField()
            publish_date = models.DateTimeField(auto_now_add=True)
        ```

2. Run the initial migrations:
    ```shell
    # Create the migration files
    python manage.py makemigrations

    # Apply the migrations
    python manage.py migrate
    ```

#### Step 5: Creating a serializer

1. Create a `serializers.py` file in your app:

2. Create a new serializer:

    ```python
    from rest_framework import serializers
    from .models import BlogPost

    # Directly link the serializer to a model
    class BlogPostSerializer(serializers.ModelSerializer):
        class Meta:
            model = BlogPost
            fields = ['id', 'title', 'content', 'published_date']

    # Create a basic serializer
    class BlogPostSerializer(serializers.Serializer):
        title = serializers.CharField()
        content = serializers.TextField()
        published_date = serializers.DateTimeField()
    ```

## Views and URL routing

- APIViews vs Viewsets
- Mapping View to URLs
- Sanitization
- Validation
- Authentication in DRF

### APIViews

- DRF provides an `APIView` class, which subclasses Django's `View` class
- Requests passed tpo the handler methods will be REST Frameworks `Request` instances instead of Django's `HttpRequest` instances. And likewise for returning responses, i.e it uses DRF's `Response` instead of Django's `HttpResponse`
- Incoming requests are dispatched to the appropriate handler method.
- APIView's have the following handler methods:
    1. `.get()`
    2. `.post()`
    3. `.put()`
    4. `.patch()`
    5. `.delete()`

**Usage:**

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import BlogPost
from .serializers import BlogPostSerializer

# Name the class according to what it's supposed to do
class BlogPostListCreate(APIView):

    # List all Blog Posts
    def get(self, request):
        # Retrieve all posts
        blog_posts = BlogPost.objects.all()

        # Use the serialzer to convert the data to JSON
        serializer = BlogPostSerializer(blog_posts, many=True)

        # Return a response
        return Response(serializer.data)  # JSON
        

    def post(self, request):
        # Deserialize the incoming data
        serializer = BlogPostSerializer(data=request.data)

        # Validate the data
        if serializer.is_valid():

            # Save the new post
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        else:
            
            # return validation errors
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

- Creating the URL routes

```python 
# blog/urls.py
from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.BlogPostListCreate.as_view()),
]
```

- In the `config/urls.py`
  
```python
from django.urls import path, include

urlpatterns = [
    path("api/blogs/", include("blogs.urls", namespace="blog"))
]
```

### Viewsets
- Instead of having method handlers like `.get()` and `.post()`, it provides actions, like `.list()` and `.create()`
- The URL construction is handled automatically using the router class
- There are 4 types of ViewSets:
    1. ViewSet
    2. GenericViewSet
    3. ReadOnlyModelViewSet
    4. ModelViewSet

| Method | ViewSet Action | Description |
|--------|----------------|-------------|
| `POST` | `create` | Create a new resource |
| `GET` | `list` | Returns all objects/resources |
| `GET` | `retrieve` (`pk` needed)| Returns a single object/resource |
| `PUT` | `update` (`pk` needed)| Updates all fields on a particular resource |
| `PATCH` | `partial_update` (`pk` needed)| Updates only the specified fields on a particular resource |
| `DELETE` | `destroy` (`pk` needed)| Delete a single resource | 

**Implement a ViewSet Class:**

- Create a new model:

```python
# blog/models.py
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    updated_date = models.DateTimeField(auto_now=True)
```

- Create a serializer for the model:

```python
# blog/serializers.py
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'completed', 'updated_date']
```

- Creating the `ViewSet` class:

```python
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import status 
from .serializers import TaskSerializer
from .models import Task


# Name the class according to the model its working with
class TaskViewSet(ViewSet):

    # Declare the queryset as a class attribute
    queryset = Task.objects.all()

    # Gets the full list of tasks
    def list(self, request):
        # Serialize the objects
        serializer = TaskSerializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Retrieves a single object
    def retrieve(self, request, pk=None):
        task = get_object_or_404(self.queryset, pk=pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)
```

- Creating the url routes:

```python
# blog/urls.py

from rest_framework import routers
from . import views

app_name = "blog"

# Initialize the router object
router = routers.SimpleRouter()

# Register the endpoints and Views
router.register(r'tasks/', views.TaskViewSet, basename="tasks")

# Add routers to urlpatterns
urlpatterns = [
    # ....
    path("", include(router.urls)),
] 
```

- In the main `urls.py`:

```python
from django.shortcuts import include, path

urlpatterns = [
    # ...
    path('api/blogs/', include("blog.urls", namespace="blog"), name="blog"),
]
```

### Authentication

- Authentication is the mechanism used to associate a request with a set credentials.
- It helps to determine whether a user has authorization to access the requested resource
- Django REST Framework provides  a few built-in authentication classes:
    1. `BasicAuthentication`
    2. `TokenAuthentication`
    3. `SessionAuthentication`
    4. `RemoteUserAuthentication`

- Authentication can be determined by either setting the Global authentication scheme or  in the settings or by defining it in the view.
- Authentication is usually accompanied by permisssions
- the Permissions are there to determine whether you are supposed to have access and what kind of access you are supposed to have
- The permissions can also be defined at global level or at a view level


#### Basic Authentication

- This makes use of the HTTP Basic Authentication
- It is generally appropriate for testing
- It utilizes the username and password to authenticate a user

**Setting basic auth at a global level:**

- To alter the `DEFAULT_AUTHENTICATION_CLASSES` setting in `settings.py`:

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}
```

**Setting auth on a Class-based View:**

```python
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class ClassBasedView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
```

#### Token Authentication

1. Add the `rest_framework.authtoken` app to the `INSTALLED_APPS` setting:

    ```python
    INSTALLED_APPS = [
        # ....
        'rest_framework.authtoken',
    ]
    ```

    - Run migrations to create the database tables for the `authtoken` app
        ```shell
        python manage.py migrate
        ```

2. Add the url to generate an auth token in the `config/urls.py`:

    ```python
    from rest_framework.authtoken import views

    urlpatterns = [
        # ...
        path("api-auth-token/", views.obtain_auth_token),
    ]
    ```

    - Clients will send their username and password via a `POST` request to this endpoint to receive an auth token

3. Add authentication to your desired view:

    ```python
    from rest_framework.authentication import TokenAuthentication
    from rest_framework.permissions import IsAuthenticatedOrReadOnly

    class ProtectedView(APIView):
        authentication_classes = [TokenAuthentication]
        permission_classes = [IsAuthenticatedOrReadOnly]

        # methods....
    ```

- When making requests to endpoints that use Token Authentication, clients must include the obtained token in the `Authorization` header prefixed with the word `Token`

    ```http
    Authorization: Token <your token>
    ```
