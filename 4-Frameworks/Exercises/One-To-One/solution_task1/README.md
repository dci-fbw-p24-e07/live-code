# Django One-to-One Relationships

## Description

In this exercise, you will practice the definition and usage of one-to-one relationships with Django's ORM.

## Data and initial files

You can find the [initial files]((https://github.com/dci-python-course/Python-databases-orm-one-to-one/tree/main/app) for this exercise in the `app` directory.

The models are the same ones produced in the last task of the previous exercise ([One-to-Many relationships](https://github.com/dci-python-course/Python-databases-orm-one-to-many/tree/solution_task2/app))

## Tasks

### Task 1

We want to keep track of who created and modified each record in the `music_song` table.

To do so, you will need to add a `created_by` and `last_modified_by` fields to the `Song` model that will both reference the built-in `User` model in the `auth` app. Both fields should allow `NULL`s.

> If a user is deleted, these fields should be set to NULL.
>
> It is best practice to reference the built-in `User` model with `settings.AUTH_USER_MODEL` instead of importing the model directly.

Additionally, we also want to store additional information about each user, such as:

- **daily_start_time**

    The time the user starts working on the database every working day. It will be required and if no value is provided it will use `09:00:00`.

- **daily_finish_time**

    The time the user finishes working on the database every working day. It will also be required and if no value is provided it will use `14:00:00`.

- **preferred_style**

    A required string as a choice of styles (the same ones used for the song model).

- **preferred_song**

    A reference to a song in the database. It will not be required.

You will define all these fields in a new model named `Profile` with a field named `user` referencing the built-in `User` model.

> A user can only have one profile (or none). A profile can only have one user, and it must have one.

Once you have modified the `Song` model and created the `Profile` model, apply the changes to the database.

> If you get some errors, read the associated HINT carefully.

**Your result should look like this:**

```
Migrations for 'music':
  music/migrations/0003_auto_20211129_1402.py
    - Add field created_by to song
    - Add field last_modified_by to song
    - Create model Profile
```
```
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, music, sessions
Running migrations:
  Applying music.0003_auto_20211129_1402... OK
```

Then, run the unit tests found in the file [app/music/tests/task1.py](app/music/tests/task1.py).

**Your result should look like this:**

```
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.....
----------------------------------------------------------------------
Ran 5 tests in 0.021s

OK
Destroying test database for alias 'default'...
```

### Task 2

Now open a Django shell to write the following queries using the ORM:

1. Create 5 users **with profiles**.

    > Check the documentation for information on how to [create users](https://docs.djangoproject.com/en/3.2/topics/auth/default/#creating-users).
    >
    > Create one user with the method `create_superuser` and the rest with the method `create_user`.

    To confirm that the users were created successfully, show the username, preferred style and preferred song of all users in the database.

    **Your result should look similar to this:**

    ```
    <QuerySet [{'username': 'josephine', 'profile__preferred_style': 'Pop', 'profile__preferred_song': 13}, {'username': 'grumilda', 'profile__preferred_style': 'Funky', 'profile__preferred_song': 45}, {'username': 'stanis', 'profile__preferred_style': 'Rock', 'profile__preferred_song': 44}, {'username': 'lucifer', 'profile__preferred_style': 'Indie', 'profile__preferred_song': 2}, {'username': 'superadmin', 'profile__preferred_style': 'Funky', 'profile__preferred_song': 3}]>
    ```

    Once you have created your users, add 5 more by loading the fixture found in [app/music/fixtures/users_and_profiles.json](app/music/fixtures/users_and_profiles.json).

2. Update the entire `music_song` table to set both the `created_by` and `last_modified_by` fields to the user named `superadmin`.

    **Your result should look similar to this:**
    ```
    791
    ```

3. Return all songs having Josephine's preferred style.

    **Your result should look similar to this:**
    ```
    <QuerySet [<Song: Song object (2)>, <Song: Song object (9)>, <Song: Song object (11)>, <Song: Song object (14)>, <Song: Song object (16)>, <Song: Song object (17)>, <Song: Song object (21)>, <Song: Song object (29)>, <Song: Song object (39)>, <Song: Song object (49)>, <Song: Song object (54)>, <Song: Song object (55)>, <Song: Song object (61)>, <Song: Song object (63)>, <Song: Song object (74)>, <Song: Song object (78)>, <Song: Song object (81)>, <Song: Song object (83)>, <Song: Song object (87)>, <Song: Song object (88)>, '...(remaining elements truncated)...']>
    ```

4. Show the preferred styles of the users who created songs having a musician playing the tambourine.

    Before writing the query, run the command `update_songs` to set different users for the fields `created_by` and `last_modified_by`.

    ```
    python manage.py update_songs
    ```

    **Your result should look like this:**
    ```
    <QuerySet [{'created_by__profile__preferred_style': 'Funky'}, {'created_by__profile__preferred_style': 'Indie'}, {'created_by__profile__preferred_style': 'Pop'}, {'created_by__profile__preferred_style': 'Rock'}]>
    ```

5. Show the id and name of the preferred songs of all users who (a) added new songs having a piano from authors that had their first appearance between 1980 and 1989 (both included) or (b) added new songs having an ukulele from authors that had their last appearance between 1910 and 1919.

    **Your result should look like this:**
    ```
    <QuerySet [{'song_id': 2, 'song_title': 'Audio number 3'}, {'song_id': 3, 'song_title': 'Audio number 4'}, {'song_id': 44, 'song_title': 'Audio number 2'}]>
    ```
    **Or like this:**
    ```
    <QuerySet [{'created_by__profile__preferred_song': 2, 'created_by__profile__preferred_song__title': 'Audio number 3'}, {'created_by__profile__preferred_song': 3, 'created_by__profile__preferred_song__title': 'Audio number 4'}, {'created_by__profile__preferred_song': 44, 'created_by__profile__preferred_song__title': 'Audio number 2'}]>
    ```
