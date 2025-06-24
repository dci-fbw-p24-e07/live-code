# Frameworks - Django

## 24.06.25 - Intro to Django

- What is a Framework?
- What is Django?
- MVC(Model-View-Controller) vs MTV(Model-Template-View) architectures
- Installing Django
- Boilerplate files

### What is a framework?

- Is like a foundation for building software.
- It provides the structure and tools to develop your projects
- Frameworks have a set way of doing things, which can make development faster and more organised

### What is Django?

[Django Docs](https://docs.djangoproject.com/en/5.2/)

- A Python Web Development Framework
- It take care of all the complex and allows you to concentrate on building your application
- It emphasizes the use of the DRY principle as it comes out-of-box with features like authentication, database connection and CRUD operations.
- Django utilizes its own version of the MVC pattern/architecture

![MTV](example_imgs/MTV.png)

![Apps vs Project](example_imgs/apps_vs_project.png)

### Installing Django

1. Create a project directory:

    ```shell
    mkdir <project-name>

    cd <project-name>
    ```

2. Create and activate the virtual environment:

    ```shell
    # Create virtual environment
    python3 -m venv .venv --prompt=<project-name>

    # Activate
    source .venv/bin/activate
    ```

3. Install Django:

    ```shell
    pip install Django

    # Check installation 
    django-admin help
    ```

4. Create a django project:

    ```shell
    django-admin startproject <name-of-project> .
    ```

5. Test django project creation(Running the development server):

    ```shell
    python manage.py runserver
    ```

6. Create a django app:

    ```shell
    django-admin startapp core
    ```
