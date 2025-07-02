# Object Relational Mapper

## 26.06.25 - djangoORM basics

- Setup the postgreSQL DB
- Use `python-dotenv` to store environment variables
- Use `sqlmigrate` to check SQL commands being sent to DB
- Use existing database to create models

## Setting up PostgreSQL database in Django

1. Create DB:

    ```sql
    CREATE DATABASE my_site_db;
    ```

2. Create a database user for the Django app and give the user permissions to DB:

    ```sql
    -- Create the user
    CREATE ROLE <username> WITH LOGIN PASSWORD '<password>';

    -- Grant user privileges to DB
    GRANT ALL PRIVILEGES ON DATABASE <database-name> TO <username>;
    ```

3. Change the existing to use the PostgreSQL settings in the `settings.py` file:

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': '<database-name>',
            'USER': '<db-username>',
            'PASSWORD': '<db-user-password>',
            'HOST': '<hostname>',
            'PORT': <db-port>(optional)
        }
    }
    ```

4. Install psycopg2:

    ```shell
    pip install psycopg2
    ```

5. Install `python-dotenv`:

    ```shell 
    pip install python-dotenv
    ```

6. Create the `.env` file in the root folder and add the environment variable to it:

    ```
    DB_NAME=<db-name>
    DB_USER=<username>
    DB_PASSWORD=<password>
    DB_HOST=<hostname>
    DB_PORT=<port>
    ```

7. Load the environment variables into the `settings.py` file:

    ```python
    import os
    from dotenv import load_dotenv

    load_dotenv()
    ```

8. Update the database settings to use dotenv:

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv("DB_NAME"),
            'USER': os.getenv("DB_USER"),
            'PASSWORD': os.getenv("DB_PASSWORD"),
            'HOST': os.getenv("DB_HOST"),
            'PORT': os.getenv("DB_PORT")
        }
    }
    ```

9. Add `.env` to the `.gitignore` file

## using the `sqlmigrate` command

- It is used to check the SQL that will be run when migrations are applied

```shell
python manage.py sqlmigrate <app-name> <migration-filenumber>

python manage.py sqlmigrate blog 0001
```

## Generating models for a legacy db

```shell
python manage.py inspectdb

# Store the output in a file
python manage.py inspectdb > <filename>.py
```

## 27.06.25 - Admin interface and CRUD operations

- Registering models in the admin interface
- Creating a superuser
- The Django Model Manager
- Django Shell
- CRUD operations using the model manager

### The Django Admin Panel/Interface

- This is a built-in browser based interface that allows a user to interact with the models.
- The user has to have staff privileges
- The models have to be registered in ordered to be displayed in the admin interface
- The admin panel is accessed through the `admin/` route that is specified the main URL Config file

**Creating a superuser:**

```shell
python manage.py createsuperuser
```

- It will prompt for a few user details which will be used to login to the admin panel

**Including models in the Admin Interface:**

- Models that you create are not displayed in the admin panel by default, they need to be explicitly included
- To do this you would need to register them through the `admin.py` file of your app

```python
from django.contrib import admin

# Import the desired models
from .models import BlogPosts

admin.site.register(BlogPosts)
```

**Using the Meta class for the model:**

- It allows you to control how data or anything related will be displayed or retrieved
- You can control ordering, Admin panel display name, database table name, create indexes, etc

```python
class BlogPosts(models.Model):
    # fields 

    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"
        ordering = ["created_at"]
```

**Updating the string Representation:**

- The models come with a built in dunder method `__str__()` that controls how an object is represented in string format
- The output value of the dunder method should be of data type `str`

```python
def __str__(self):
    return str(self.title)
```

### The Django Model Manager

- A Django class that acts as a bridge between database queries and Django models.
- It acts as the interface that interacts with the database in Django Models.
- If you want to retrieve data or objects from your database the Manager will create a QuerySet that returns the objects.
- A queryset is a collection of data for the database. It allows to get data easily by allowing us to filter, create, order, etc.
- A queryset is usually a list
- The default name for a models manager is `objects`

**Syntax:**'
```python
model_name.objects.method

# Get all BlogPosts
BlogPosts.objects.all()  # -> QuerySet
```

**Methods of a Manager Class:**

| Method | Description |
|--------|-------------|
| `all()` | returns a queryset containing all objects created on that model |
| `filter()` | returns a queryset with a list of objects that match given arguments |
| `get()` | returns a single object that corresponds to the given argument. |
| `create()` | creates a new object |
| `order_by()` | returns the queryset arranged in a particular order as mentioned in the argument |

### The Django Shell

- It allows you to write Python statements from the command line as though they are being executed from within the Django Web Framework
- It is an interactive CLI shell environment that combines the Django Framework functionality with the regular Python
- It can load project specific parameters and settings that only work within the project
- One of the main functionalities that it provides is easy access to the ORM allowing you to directly interact with the database
- If you make any changes to your models you should restart your Django andf re import any dependencies so it picks up the changes

```shell
python manage.py shell
```

- In order to use models within the you need to import them

```python
from blog.models import BlogPosts
```

- To check the SQL query that will be run

    ```python
    print(<queryset>.query)
    ```

### CRUD operations using the ORM

#### Inserting data

1. Single insert

    1. Use the `objects` Manager

        ```python
        blog_1 = BlogPosts.objects.create(title="My First Shell Interaction", body="This shell is really easy to use and makes this fast")
        ```

    2. Use the `save()` method

        ```python
        # 1. Initialize object
        blog_2 = BlogPosts(title="My second interaction", body="We are getting the hang of this")

        # 2. Commit changes to database
        blog_2.save()
        ```

2. Bulk insert

    - The Django model manager provides a `bulk_create` that takes in a list of objects for that specific model.

    ```python
    BlogPosts.objects.bulk_create([BlogPosts(title="Using the bulk create", body="This makes things a lot easier and faster"), BlogPosts(title="Django is fun", body="We will use Django to the fullest")])
    ```

#### Reading Data

1. Get a single object

    ```python
    blog = BlogPosts.objects.get(id=3)
    ```

2. Get all objects

    ```python
    all_blogs = BlogPosts.objects.all()
    ```

3. Filter for objects of a specific criteria

    ```python
    published_posts = BlogPosts.objects.filter(published=True)
    ```

- The Django ORM provides a `.values()` method that returns the actual values of each object
- In order to use this it needs to be attached to a queryset through method chaining

```python
BlogPosts.objects.filter(published=True).values()
```

- The Django ORM also allows to get the actual of a specific field on an object

```python
my_blog = BlogPosts.objects.get(id=7)
my_blog.published
```


#### Update Data

- In order to change the value of field on an object you first need to retrieve that object

```python
blog = BlogPosts.objects.get(id=3)
```

- You can tap into the desired field by using dot-notation to specify the field

```python
# Change the value of the field
blog.title="This should change"

# Save changes to database
blog.save()
```

#### Deleting Data

- In order delete you need to first retrieve the object then you can call the `delete()` method on that object.

```python
# Retrieve object
blog = BlogPosts.objects.get(id=3)

# Delete object
blog.delete()
```

## 01.07.25 - Field lookups, Aggregation and Chaining

- What are field lookups?
- Using lookup fields
- Aggregation and annotation using DjangoORM
- Chaining querysets

### Field lookups

- Field lookups are key to creating SQL `WHERE` clauses.
- These are used in methods like `filter()`, `exclude()`, and `get()`
- They are used as parameters tied together with a specific field in the model

```python
<model-name>.objects.<model-method>(<field>__<lookup>=<value-to-compare>)

Employee.objects.filter(dob__gte="1986-07-10")

Employee.objects.filter(first_name__icontains="X%")
```

> [Lookup Fields Reference](https://docs.djangoproject.com/en/5.2/ref/models/querysets/#field-lookups)

1. `startswith`

    ```python
    blog_1 = BlogPosts.objects.filter(title__startswith="D")

    # Output: <QuerySet [<BlogPosts: Django is fun>, <BlogPosts: Django is fun for everyone>]>
    ```

2. `in`

    - Check for values that are in the provided list

    ```python
    # <model-name>.objects.<model-method>(<field>__<lookup>=[list-of-values])

    blog_2 = BlogPosts.objects.filter(pk__in=[1, 3, 5])
    ```

3. `year`

    ```python
    blog_3 = BlogPosts.objects.exclude(created_at__year=2025)
    ```

4. `range`

    ```python
    # Get all blogposts that have an id in the range 1 - 5

    blog_4 = BlogPosts.objects.filter(pk__range=(1, 5))
    ```

5. `startswith`

    ```python
    # Get all posts whose title starts with the T
    blog_x = BlogPosts.objects.filter(title__startswith='T').values()
    ```

6. `iendswith`

    ```python
    # Get all posts whose title ends with the letter e
    blog_6 = BlogPosts.objects.filter(title__iendswith="E")
    ```

### Aggregation and annotation with Django ORM

- Aggregation and annotation functions must always be imported separately

```python
from django.db.models import Sum, Max, Min, Count, Avg
```

**Annotation:**

- Creates a summary of each object in a queryset

```python
<annotated-output> = <model-name>.objects.annotate(<variable>=<aggregate-function>(<field-name>))

Employee.objects.annotate(avg_salary=Avg('salary'))

# Count all the chapters of each book
books = Book.objects.annotate(chapter_count=Count('bookdata'))

# Access the chapters variable
books[0].chapter_count
```

**Aggregation:**

- Combines separate elements to form a whole
- Combine records of the fields to get a summary of the query set.

```python
<model-name>.objects.aggregate(<aggregation-func>('<field-name>'))

Employee.objects.aggregate(Sum('salary'))

# Get the total value of all the books
Book.objects.aggregate(Sum('price'))

# Get the average number of pages each book has
Book.objects.aggregate(Avg('pages'))

# Get the maximum number of pages that a book has
Book.objects.aggregate(Max('pages'))
```

## 02.07.25 - Meta class and model methods

- What is the `Meta` class?
- Meta class options
- Using the Meta class to enhance Model functionality
- Overriding Django Model methods

### `Meta` Class

- A special inner class that is used to provide metadata to the model.
- It's not a Django-specific feature it is a Python feature where an inner class called Meta can be used to configure behaviour of a class especially in frameworks.
- It provides a way to customize the behaviour without adding new fields.

**Commonly used options:**

- `db_table` - Override the automatically created table name (`<app-name>_<model-name>`)
- `ordering` - Used to determine the field which should to order a queryset. Default is usually the primary key field
- `unique_together` - Enforces that a combination of fields must be unique at the database level
- `indexes` - list of indexes to speed up database lookups

> You can find all `Meta` options at: [https://docs.djangoproject.com/en/5.2/ref/models/options/](https://docs.djangoproject.com/en/5.2/ref/models/options/)

**Using the `Meta` options:**

1. `indexes`

    - Defines a list of indexes to be used on the database
    - created and managed using the `models.Index` class

    ```python
    class Meta:
        indexes = [
            models.Index(fields=['name'], name="book_name_idx"),
            models.Index(fields=['price'], name="book_price_idx")
        ]
    ```

2. `constraints`

    - Defines a list of database constraints to be enforced when saving data to the database
    - Can be created using the `models.CheckConstraint()` or `models.UniqueConstraint()`

    ```python
    constraints = [
            models.CheckConstraint(condition=models.Q(pages__gte=50), name="pages_gte_50"),
            # Check that the price is not above 100
            models.CheckConstraint(condition=models.Q(price__lte=100), name="price_lte_100")
        ]
    ```

3. `db_table`

    - Defines the table name for the database

    ```python
    db_table = "book_data"
    ```

**Benefits of using the `Meta` class:**

1. It keeps your models clean by separating configuration from fields
2. It lets you customize behaviour without affecting the actual data structure
3. It improves readability, performance and control over how your models work

### Model Methods and overriding

- django model methods provide functionality on a "row-level" basis as opposed to the Model Manager which accesses the full model
- This is valuable for keeping business logic for models in one place.

**Create a custom method:**

- Create a method to determine whether a book is expensive, affordable or cheap. This will be determined by price range:

    - Expensive - 65-100
    - Affordable - 35 - 64
    - Cheap - 34  and below

    ```python
    def price_status(self):
        """ 
        Returns the price status of a book
        """
        
        if self.price >= 65:
            return "Expensive"
        elif self.price >= 35 and self.price <= 64:
            return "Affordable"
        elif self.price <= 34:
            return "Cheap"

    # Using the custom method
    book_1 = Book.objects.get(id=2)
    book_1.price_status() # Output: 'Cheap'
    ```

**Overriding built-in model methods:**

- Django models have a few built-in methods that offer specific functionality e.g. `save()`, `delete()`,` __str__()`, etc.
- These can be overridden to produce some custom functionality
- The `super().save(**kwargs)` should be called within the custom method in order for saving to actually take place

- We don't want to save any books that have the word Java in the name

    ```python
    def save(self, **kwargs):
        if "Java".lower() in self.name.lower():
            return "We don't like Java over here"
        else:
            # Call the actual save method
            super().save(**kwargs)
    ```
