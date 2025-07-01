# Django Models & Fields

## Description

In this exercise, you will practice the definition of models and fields and the use of QuerySets.

## Data and initial files

The `app` directory holds the code for a Django web application that will store information related to music.

The Django project already has a Django app named `music` and the project main files (settings and urls) are located in the directory `project`.

Move into the `app` directory and create a virtual environment. Activate it and install the project dependencies.

## Tasks

### Task 1

Modify the settings to be able to use models on the music app and use PostgreSQL as the database engine. Besides defining Django's settings, you will have to manually create an empty database.

Then, create a new model named `Song` in the `music` app. This model should have the following fields:

- **audio**

    A file with the audio of the song. This field will be required. The files should be uploaded into a directory named `audio` in the media directory.

    > The project settings and urls must be configured to manage media files in development.

- **title**

    It will be required and will hold a string of maximum 250 characters.
- **author**

    The author or band. It will not be required and will hold a string of maximum 50 characters. An index will be created for this field.
- **author_website**

    Not required. It will store a link to the website of the author.
- **album**

    The name of the album the song belongs to. It will not be required and it will have a limit of 250 characters.
- **duration**

    It will be required and will hold a duration object.
- **style**

    It will not be required and will hold a string of maximum 20 characters. This field will have some predefined options to choose from (rock, pop, indie, funky, classic, reggaeton,...).

    > You can define your own list of styles.
- **playbacks**

    An integer representing the amount of times the song has been reproduced in our app. Negative integers should not be allowed. It should be able to store a NULL state.
- **price**

    A decimal representing the price in euros of purchasing this song in our app. It should never accept values above 4.99 and it can never be NULL. If there is no price, the price is 0.00€.
- **deal_of_the_day**

    A boolean indicating if the song is currently on a special discount. It will not be required.
- **notes**

    Used to store some general notes. Not required. It will be a text field with no character length limitation.
- **created**

    Date and time the record was added to the database. Should be automatically populated by Django when saving a new object.
- **last_modified**

    Date and time of the last time the record was updated. Should be automatically populated by Django every time an object is updated.

A unique constraint should be defined on the combination of the fields title, author, album and duration.

All field validations must be ran every time a song is saved.

Once you have the model, create the initial migration file.

**Your result should look like this:**

```
Migrations for 'music':
  music/migrations/0001_initial.py
    - Create model Song
```

Then, run the migration.

**Your result should look like this:**

```
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, music, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying music.0001_initial... OK
  Applying sessions.0001_initial... OK
```

Finally, run the unit tests that you will find in the file `music/tests/task1.py`.

**Your result should look like this:**

```
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
......
----------------------------------------------------------------------
Ran 6 tests in 1.059s

OK
Destroying test database for alias 'default'...
```

Compare your solution with [the solution provided](https://github.com/dci-python-course/Python-databases-orm-models-fields/commits/solution_task1).

### Task 2

The `Song` model will be fitting our needs of storing and retrieving songs from various artists and styles.

But now, the website should also be able to accommodate other types of audio files (podcasts and special effects) and we want to use the same model to manage all types.

To do so, you will have to change some things in the current `Song` model:

- **Model name**

    The name `Song` is not representative of the objects that the model holds. Instead, the name `Audio` seems more general and fitting.

    Rename the model.

- **Type**

    A new field named `type` should be added to identify if the audio is a `song`, a `podcast` or an `effect`.

- **Style**

    The `style` field should only apply to audios of the `song` type. To make sure this remains consistent, validate the values every time the model is saved, so that it only allows a `style` if the type is `song`.

    To make it more verbose and less confusing, rename also the field to `song_style`.

    > To pass the unit tests at the end, make sure you have a style named `Funky`.

- **Price**

    Now, the validation of the `price` field needs to work differently. The 4.99€ limitation only applies to songs. For podcasts, the price limit will be 3.99€ and for effects the limit will be 94.99€.

- **Notes**

    After some discussion with other team members, it has been noted that this field is not going to be used, as the current model will be used only in the public site and any information used only for administration purposes will be placed in a different model.

    Remove this field.

Once you have done all the changes, create the migration file.

**Your result should look similar to this:**

```
Migrations for 'music':
  music/migrations/0002_auto_20211125_1152.py
    - Create model Audio
    - Delete model Song
    - Create constraint unique_song on model audio
```

Then, review the migration file and run it.

**Your result should look similar to this:**

```
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, music, sessions
Running migrations:
  Applying music.0002_auto_20211125_1152... OK
```

Finally, start a Django shell with the `shell` command and run the following lines of code:

Finally, run the unit tests that you will find in the file `music/tests/task1.py`.

**Your result should look like this:**

```
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.........
----------------------------------------------------------------------
Ran 9 tests in 1.083s

OK
Destroying test database for alias 'default'...
```

Compare your solution with [the solution provided](https://github.com/dci-python-course/Python-databases-orm-models-fields/commits/solution_task2).

### Task 3

Now, load the fixture found in the file `music/fixtures/audio.json` into the database.

Then, open Django's shell and type the following ORM queries:

> To test your queries, assign them to a variable and inspect the `query` property. You can also use `connection.queries` to see the number of queries done on the session.

1. Create a QuerySet with all songs (alone).

    **Your result should look like this:**

    ```
    <QuerySet [<Audio: Audio object (2)>, <Audio: Audio object (3)>, <Audio: Audio object (5)>, <Audio: Audio object (6)>, <Audio: Audio object (7)>, <Audio: Audio object (9)>, <Audio: Audio object (17)>, <Audio: Audio object (18)>, <Audio: Audio object (19)>, <Audio: Audio object (26)>, <Audio: Audio object (27)>, <Audio: Audio object (29)>, <Audio: Audio object (38)>, <Audio: Audio object (39)>, <Audio: Audio object (45)>, <Audio: Audio object (53)>, <Audio: Audio object (54)>, <Audio: Audio object (59)>, <Audio: Audio object (64)>, <Audio: Audio object (66)>, '...(remaining elements truncated)...']>
    ```
1. Count the number of podcasts.

    **Your result should look like this:**

    ```
    36
    ```

1. Count the number of audios that are not songs.

    **Your result should look like this:**

    ```
    68
    ```
1. Get the 10 shortest songs.

    **Your result should look like this:**

    ```
    <QuerySet [<Audio: Audio object (54)>, <Audio: Audio object (68)>, <Audio: Audio object (80)>, <Audio: Audio object (69)>, <Audio: Audio object (7)>, <Audio: Audio object (9)>, <Audio: Audio object (64)>, <Audio: Audio object (98)>, <Audio: Audio object (5)>, <Audio: Audio object (45)>]>
    ```
1. Get the second most expensive audio effect.

    **Your result should look like this:**

    ```
    <Audio: Audio object (75)>
    ```
1. Get all songs lasting between 2 and 3 minutes. Then, count them.

    **Your result should look like this:**

    ```
    6
    ```
1. Now, count how many songs are there that last between 2 and 3 minutes or have a price higher than 2 euros.

    **Your result should look like this:**

    ```
    20
    ```
1. Set the price of all podcasts of more than 30 minutes long to 3.99€.

    **Your result should look like this:**

    ```
    14
    ```
Compare your solutions with [the solutions provided](https://github.com/dci-python-course/Python-databases-orm-models-fields/commits/solution_task3).
