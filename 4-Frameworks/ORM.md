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
