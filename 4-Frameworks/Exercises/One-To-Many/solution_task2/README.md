# Django One-to-Many Relationships

## Description

In this exercise, you will practice the definition and usage of one-to-many relationships with Django's ORM.

## Data and initial files

You can find the [initial files]((https://github.com/dci-python-course/Python-databases-orm-one-to-many/tree/main/app) for this exercise in the `app` directory.

In this exercise we will manage data related to songs only, but we will extend it with data about albums, authors and musicians.

## Tasks

### Task 1

Your first task is to improve the `Song` model. One of the improvements that is immediately apparent is to change how the data about the author and album is stored.

Both may require storing additional information that we don't want to be repeated many times in the `music_song` table.

In the file [app/music/models.py](app/music/models.py) you will find an initial model similar to the one used in the Models & Fields exercise.

Take this file and add new models named `Author`, `Musician` and `Album`.

An `Author` is the individual or band performing the song. Because it can be a group of people, an additional model named `Musician` will be created to store every single member of each author.

If an author is a band, it will have many musicians associated to it. If not, it will only have 1 musician. But a musician will always be associated to an author, even if she/he is the only member and the name is repeated.

For the `Author` we want to store the following information:

- **name**

    The full name of an author. It can be the name of the band or the name of the musician. This field is required and its length will be limited to 255 characters.

- **website**

    The website of the band or musician. This field is not required.

- **first_appearance**

    The year of first appearance of the band or musician. This field is not required, but if a value is provided, it will validate that it is an integer lower or equal to the current's year and not below 1000.

    The field should render on a form as **Year of first appearance**.

- **last_appearance**

    The year of last appearance will be similar to the year of first appearance. It will not be required and should be lower or equal to current's year and not below 1000.

    The field should render on a form as **Year of last appearance**.

    Both fields should be validated together, so that the `first_appearance` is not greater than the `last_appearance` and raise an error if it is.

For the `Musician`, we want to store the following information:

- **name**

    The full name of the musician. It will be a required string of a maximum of 150 characters.

- **nationality**

    A required [two character identifier](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements) of the country of origin of the musician.

- **instrument**

    A required string with the choices of instruments. Use the following list of instruments as valid choices.

    ```
  (
      ("piano", "Piano"),
      ("eguitar", "Electric Guitar"),
      ("cguitar", "Classical Guitar"),
      ("aguitar", "Acoustic Guitar"),
      ("ebass", "Electric Bass"),
      ("bass", "Bass"),
      ("drums", "Drums"),
      ("voice", "Voice"),
      ("violin", "Violin"),
      ("harp", "Harp"),
      ("handpan", "Handpan"),
      ("tambourine", "Tambourine"),
      ("sax", "Saxophone"),
      ("trumpet", "Trumpet"),
      ("trombone", "Trombone"),
      ("flute", "Flute"),
      ("clarinet", "Clarinet"),
      ("ukulele", "Ukulele"),
  )
    ```

For the `Album`, we want to store the following information:

- **title**

    A string containing the title of the album. It will be limited to 255 characters and will be required.

- **year_of_release**

    A required integer field that follows the same criteria as the `first_appearance` and `last_appearance` fields in the `Author` model (not in the future and above 1000).

- **produced_by**

    A non-required text field limited to 255 characters. It will store the name of the producer of this album.


> An album may contain songs from different authors, so the author should be associated directly to the song and not the album.
>
> If an album is deleted, all the songs in the album should also be deleted.
>
> If an author is deleted, its members (musicians) should also be deleted, but the songs should remain in the database.
>
> For the unit tests to work and to be able to load the data in the next task, name the fields as they appear in the description above.
>
> When defining foreign keys, use the same name of the model it refers to in lowercase (ex: Song.author references Author).

Create the three models and set the proper relationship between them. Then, synchronize your model with the database.

**The makemigrations command should return something similar to this:**

```
Migrations for 'music':
  music/migrations/0002_auto_20211128_2130.py
    - Create model Album
    - Create model Author
    - Remove field author_website from song
    - Create model Musician
    - Alter field album on song
    - Alter field author on song
```

Once you are done, run the unit tests found in the file [app/music/tests/task1.py](app/music/tests/task1.py).

**Your result should look like this:**

```
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.......
----------------------------------------------------------------------
Ran 7 tests in 0.040s

OK
Destroying test database for alias 'default'...
```

### Task 2

Load into the database the fixtures found in the file [app/music/fixtures/music.json](app/music/fixtures/music.json).

Once loaded, open a Django shell and type the following queries:

> All ORM queries should evaluate as single SQL transactions.
>
> Use the `django.db.connection.queries` property to make sure your ORM query does not produce more than one SQL transaction.


1. Show a list of all musicians playing in the song with id `46`.

    **Your result should look like this:**

    ```
    <QuerySet [<Musician: Musician object (31)>, <Musician: Musician object (30)>, <Musician: Musician object (29)>, <Musician: Musician object (28)>, <Musician: Musician object (27)>, <Musician: Musician object (26)>, <Musician: Musician object (25)>]>
    ```

1. Get the producer of the song with id `13`.

    **Your result should look like this:**

    ```
    'Hutticher'
    ```

1. Show the id, title and album title of all `pop` songs having a Saxophone.

    **Your result should look like this:**

    ```
    QuerySet [{'pk': 158, 'title': 'Audio number 15', 'album__title': 'Album 20'}, {'pk': 199, 'title': 'Audio number 7', 'album__title': 'Album 25'}, {'pk': 204, 'title': 'Audio number 12', 'album__title': 'Album 25'}, {'pk': 205, 'title': 'Audio number 13', 'album__title': 'Album 25'}, {'pk': 221, 'title': 'Audio number 4', 'album__title': 'Album 29'}, {'pk': 222, 'title': 'Audio number 5', 'album__title': 'Album 29'}, {'pk': 237, 'title': 'Audio number 3', 'album__title': 'Album 31'}, {'pk': 373, 'title': 'Audio number 15', 'album__title': 'Album 44'}, {'pk': 388, 'title': 'Audio number 7', 'album__title': 'Album 46'}, {'pk': 395, 'title': 'Audio number 14', 'album__title': 'Album 46'}, {'pk': 399, 'title': 'Audio number 3', 'album__title': 'Album 47'}, {'pk': 403, 'title': 'Audio number 7', 'album__title': 'Album 47'}, {'pk': 407, 'title': 'Audio number 11', 'album__title': 'Album 47'}, {'pk': 408, 'title': 'Audio number 12', 'album__title': 'Album 47'}, {'pk': 411, 'title': 'Audio number 15', 'album__title': 'Album 47'}, {'pk': 524, 'title': 'Audio number 7', 'album__title': 'Album 62'}, {'pk': 544, 'title': 'Audio number 12', 'album__title': 'Album 65'}, {'pk': 606, 'title': 'Audio number 6', 'album__title': 'Album 75'}, {'pk': 691, 'title': 'Audio number 10', 'album__title': 'Album 89'}]>
    ```
    **If you count them you should get the following result:**

    ```
    19
    ```

1. Show the id, title and album title of all songs produced by `Clark` and having a Saxophone.

    **Your result should look like this:**

    ```
    <QuerySet [{'id': 398, 'title': 'Audio number 2', 'album__title': 'Album 47'}, {'id': 399, 'title': 'Audio number 3', 'album__title': 'Album 47'}, {'id': 400, 'title': 'Audio number 4', 'album__title': 'Album 47'}, {'id': 401, 'title': 'Audio number 5', 'album__title': 'Album 47'}, {'id': 402, 'title': 'Audio number 6', 'album__title': 'Album 47'}, {'id': 403, 'title': 'Audio number 7', 'album__title': 'Album 47'}, {'id': 404, 'title': 'Audio number 8', 'album__title': 'Album 47'}, {'id': 405, 'title': 'Audio number 9', 'album__title': 'Album 47'}, {'id': 406, 'title': 'Audio number 10', 'album__title': 'Album 47'}, {'id': 407, 'title': 'Audio number 11', 'album__title': 'Album 47'}, {'id': 408, 'title': 'Audio number 12', 'album__title': 'Album 47'}, {'id': 409, 'title': 'Audio number 13', 'album__title': 'Album 47'}, {'id': 410, 'title': 'Audio number 14', 'album__title': 'Album 47'}, {'id': 411, 'title': 'Audio number 15', 'album__title': 'Album 47'}, {'id': 412, 'title': 'Audio number 16', 'album__title': 'Album 47'}]>
    ```

    **If you count them you should get the following result:**

    ```
    15
    ```

1. Show all producers of bands that first appeared in the last hundred years (today's year - 100 years).

    **Your result should look like this:**

    ```
    <QuerySet [{'produced_by': 'Adams'}, {'produced_by': 'Ahmas'}, {'produced_by': 'Clark'}, {'produced_by': 'Fiedler'}, {'produced_by': 'Hill'}, {'produced_by': 'Lewis'}, {'produced_by': 'Miller'}, {'produced_by': 'Sanchez'}, {'produced_by': 'White'}, {'produced_by': 'Wright'}]>
    ```

    **If you count them you should get the following result:**

    ```
    10
    ```
