# Django Many-to-Many Relationships

## Description

In this exercise, you will practice the definition and usage of Many-To-Many relationships with the Django ORM.

## Data and initial files

You can find the [initial files](app) for this exercise in the `app` directory.

The models are the same ones produced in the last task of the exercise on [One-to-One relationships](https://github.com/dci-python-course/Python-databases-orm-one-to-one/tree/solution_task2/app).

## Tasks

### Task 1

The previous design has a few flaws. One of them is that a musician can only be part of a single band (`author`).

Now, we want to be able to relate the same musician with more than one band.

Additionally, we want to store the year the musician started with that band and the year the musician stopped playing with that band. The starting year must be a required field named `start` and the year they stopped will be stored in a non-required field named `end`. If this field is `NULL`, it will mean the musician is currently a member.

Similarly, in our current implementation a song can only by authored by a band or a single musician, but in some occasions more than one band can be co-authoring the same song.

Change the models to meet the new requirements. Then make and run the migrations and finally run the tests located at `music.tests.task1`.

**Your result should look like this:**

```
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
..
----------------------------------------------------------------------
Ran 3 tests in 0.025s

OK
Destroying test database for alias 'default'...
```

### Task 2

Now, open the Django shell and type the ORM queries to:

1. Assign the song with id 15 to the authors with ids 30 and 40.

    Then execute this query:

    ```
    Song.objects.get(pk=15).authors.all()
    ```

    **Your result should look like this:**

    ```
    <QuerySet [<Author: Author object (30)>, <Author: Author object (40)>]>
    ```

1. Assign the songs with ids 10, 20, 30 1nd 40 to the author with id 50.

    Then execute this query:

    ```
    Author.objects.get(pk=15).song_set.all()
    ```

    **Your result should look like this:**

    ```
    <QuerySet [<Song: Song object (10)>, <Song: Song object (20)>, <Song: Song object (30)>, <Song: Song object (40)>]>
    ```

1. Assign the musicians with ids 10, 20, 30 and 40 to the author with id 100.

    Then execute this query:

    ```
    Author.objects.get(pk=100).members.all()
    ```

    > If you don't have the members `related_name`, use `musician_set` instead or the `related_name` you wrote.

    **Your result should look like this:**

    ```
    <QuerySet [<Musician: Musician object (10)>, <Musician: Musician object (20)>, <Musician: Musician object (30)>, <Musician: Musician object (40)>]>
    ```

1. Get the name and instrument of each member (musician) of the band (author) with id 100.

    **Your result should look like this:**

    ```
    <QuerySet [{'name': 'Noah Garcia', 'instrument': 'clarinet'}, {'name': 'Loretta Schumacher', 'instrument': 'eguitar'}, {'name': 'Liam Perez', 'instrument': 'piano'}, {'name': 'Arnold Hutticher', 'instrument': 'trombone'}]>
    ```
