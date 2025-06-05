# SQL's Data Manipulation and Query Language

## Description

In this exercise, you will focus on populating, querying and deleting the data in the database.

## Data

Execute the contents of the file [music.sql](music.sql) in the terminal. This file will load a slightly different data set about musicians. It creates a table named `musician` with the following fields:

- **first_name**: string with the first name of the musician.
- **last_name**: string with the last name of the musician.
- **date_of_birth**: a date field with the date of birth of the musician.
- **instrument**: string with the main instrument of the musician.

The table will be created empty.

## Tasks

You can choose to execute the following tasks using the terminal or using DBeaver (or a combination).

In any case, all operations (except connecting to a database) must be done using SQL statements.

### Task 1

Write and execute the SQL statements to add 5 musicians of your choice to the table.

> **Hint**: to insert dates use the `'YYYY-MM-DD'` string format.

Then, select all data from all the musicians and confirm the table now has your 5 musicians.

**Your result should look similar to this:**

```
 first_name | last_name |    date_of_birth    | instrument
------------+-----------+---------------------+------------
 Justin     | Bieber    | 1994-03-01 00:00:00 | Voice
 Lady       | Gaga      | 1986-03-28 00:00:00 | Voice
 Alejandro  | Sanz      | 1968-12-18 00:00:00 | Voice
 Jimmy      | Hendrix   | 1942-11-27 00:00:00 | Guitar
 Charlie    | Parker    | 1920-08-29 00:00:00 | Saxophone
(5 rows)
```

### Task 2

Now, execute the file [data.sql](data.sql) to load the table with additional (fake) musicians.

Use an SQL statement to show a list of 10 musicians.

**Your result should look similar to this:**

```
 first_name | last_name  |    date_of_birth    | instrument
------------+------------+---------------------+------------
 Justin     | Bieber     | 1994-03-01 00:00:00 | Voice
 Lady       | Gaga       | 1986-03-28 00:00:00 | Voice
 Alejandro  | Sanz       | 1968-12-18 00:00:00 | Voice
 Jimmy      | Hendrix    | 1942-11-27 00:00:00 | Guitar
 Charlie    | Parker     | 1920-08-29 00:00:00 | Saxophone
 Arturo     | Schumacher | 1994-09-17 17:45:58 | Trombone
 Chloe      | McDonald   | 1976-04-03 20:20:07 | Voice
 Ella       | Moore      | 1962-02-25 04:30:36 | Saxphone
 Itziar     | McDonald   | 1966-08-11 04:35:48 | Clarinet
 Aaliyah    | Brown      | 1993-08-20 18:26:23 | Clarinet
(10 rows)
```

### Task 3

Show a list of musicians sorted by date of birth.

**Your result should look similar to this:**

```
 first_name |   last_name    |    date_of_birth    |  instrument   
------------+----------------+---------------------+---------------
 Charlie    | Parker         | 1920-08-29 00:00:00 | Saxophone
 Jimmy      | Hendrix        | 1942-11-27 00:00:00 | Guitar
 Grace      | Fiedler        | 1950-01-23 02:46:32 | Keyboard
 Aaliyah    | Black          | 1950-01-24 05:07:44 | Saxphone
 Yussef     | Moore          | 1950-02-24 03:17:43 | Trombone
 Gianna     | Hunter         | 1950-05-18 12:27:04 | Saxphone
 Amelia     | Martí          | 1950-06-02 13:16:53 | Cello
 ...        | ...            | ...                 | ...
```

Now, show the same list but listing the youngest musicians first.

**Your result should look similar to this:**

```
 first_name |   last_name    |    date_of_birth    |  instrument   
------------+----------------+---------------------+---------------
 Keith      | Muller         | 2000-12-21 06:18:54 | Piano
 Arturo     | Johnson        | 2000-10-21 19:42:58 | Piano
 Julia      | Müller         | 2000-05-08 14:04:39 | Electric Bass
 Julia      | Moore          | 2000-05-02 12:26:59 | Flute
 Araceli    | Doe            | 2000-03-01 16:30:34 | Clarinet
 Olivia     | Nguyen         | 2000-01-28 20:06:43 | Violin
 Emma       | Adams          | 1999-11-25 18:51:40 | Violin
 ...        | ...            | ...                 | ...
```

### Task 4

Next, delete the musicians you added.

Then, show the 10 youngest musicians in the database.

**Your result should look like this:**

```
 first_name |   last_name    |    date_of_birth    |  instrument   
------------+----------------+---------------------+---------------
 Keith      | Muller         | 2000-12-21 06:18:54 | Piano
 Arturo     | Johnson        | 2000-10-21 19:42:58 | Piano
 Julia      | Müller         | 2000-05-08 14:04:39 | Electric Bass
 Julia      | Moore          | 2000-05-02 12:26:59 | Flute
 Araceli    | Doe            | 2000-03-01 16:30:34 | Clarinet
 Olivia     | Nguyen         | 2000-01-28 20:06:43 | Violin
 Emma       | Adams          | 1999-11-25 18:51:40 | Violin
 Araceli    | Garcia         | 1999-09-07 22:44:10 | Harp
 Ella       | Miller         | 1999-08-11 09:34:43 | Flute
 Bernhard   | Schwarzenegger | 1999-03-27 01:15:21 | Saxphone
(10 rows)
```

### Task 5

On your last query, you realized the database has a mistake. An instrument named `Saxphone` should actually be `Saxophone`.

Change all the records of saxophone players, so that the name of the instrument is properly written.

Then, to make sure it worked, show all musicians playing the saxophone.

**Your result should look like this:**

```
 first_name |   last_name    |    date_of_birth    | instrument
------------+----------------+---------------------+------------
 Ella       | Moore          | 1962-02-25 04:30:36 | Saxophone
 Bernhard   | Hunter         | 1994-03-20 07:46:53 | Saxophone
 Olivia     | Hutticher      | 1969-12-02 08:52:37 | Saxophone
 Grace      | Jones          | 1959-04-15 20:19:27 | Saxophone
 Grace      | Blanc          | 1991-08-18 13:24:56 | Saxophone
 William    | Adams          | 1980-07-03 11:25:22 | Saxophone
 Bernhard   | Schwarzenegger | 1999-03-27 01:15:21 | Saxophone
 ...        | ...            | ...                 | ...
```

### Task 6

And, on the same query, you spotted another mistake. `Bernhard Schwarzenegger` doesn't actually play the `Saxophone`, he plays the `Piano`. Everybody knows that!

Change it, before anyone else notices it.

To confirm the change took effect, write a query that shows  which instrument is `Bernhard Schwarzenegger` playing now.

> Only the instrument should be displayed on the output.

**Your result should look like this:**

```
 instrument
------------
 Piano
(1 row)
```

### Task 7

Produce a list of piano players named `Araceli` (as a first name).

Since all are named Araceli and play the piano, do not show the first name nor the instrument in the output.

**Your result should look like this:**

```
 last_name |    date_of_birth    
-----------+---------------------
 White     | 1971-11-01 15:02:13
 Ali       | 1955-07-13 07:07:38
 Hill      | 1997-07-29 23:38:31
 Doe       | 1980-06-15 07:57:14
(4 rows)
```

### Task 8

Produce a list of first names, last names and instruments of all piano and guitar players sorted by instrument and, if the instrument is the same, then sorted by last name.

**Your result should look like this:**

```
 first_name |   last_name    | instrument
------------+----------------+------------
 Julia      | Adams          | Guitar
 Ahmed      | Anniston       | Guitar
 Abdul      | Clark          | Guitar
 Marc       | Green          | Guitar
 Araceli    | Hutticher      | Guitar
 Benjamin   | Johnson        | Guitar
 Arnold     | Lewis          | Guitar
 ...        | ...            | ...
```

### Task 9

Produce a list with the 3 youngest piano players or guitar players named Araceli.

**Your result should look like this:**

```
 first_name | last_name |    date_of_birth    | instrument
------------+-----------+---------------------+------------
 Araceli    | Hill      | 1997-07-29 23:38:31 | Piano
 Araceli    | Doe       | 1980-06-15 07:57:14 | Piano
 Araceli    | Hutticher | 1978-03-20 08:02:55 | Guitar
(3 rows)
```

### Task 10

Show a list of all the different instruments in the `music` table. Sort the list by the name of the instrument.

**Your result should look like this:**
```
instrument   
---------------
Cello
Clarinet
Drums
Electric Bass
Flute
Guitar
Harp
Keyboard
Piano
Saxophone
Trombone
Trumpet
Violin
Voice
(14 rows)
```

### Task 11

Show only the fourth youngest Harp player whose name starts with the letter M.

Show the first name, last name and date of birth. But this time, print them as `Name`, `Family Name` and `Date of birth`.

**Your result should look like this:**

```
Name | Family name |    Date of birth    
------+-------------+---------------------
Ella | Müller      | 1957-03-08 08:44:10
(1 row)
```

### Task 12

Show a list of musicians whose last name does not start with Y, M, C or A.

Order the list by last name first, and then by first name. Show only rows from 5 to 10.

**Your result should look like this:**

```
first_name | last_name |    date_of_birth    | instrument
------------+-----------+---------------------+------------
Benjamin   | Black     | 1995-08-28 23:25:55 | Keyboard
Evelyn     | Black     | 1951-08-20 00:36:39 | Violin
Naomi      | Black     | 1987-03-16 00:23:44 | Harp
Noah       | Black     | 1959-03-10 00:16:37 | Cello
Olivia     | Black     | 1959-08-19 23:18:49 | Violin
(5 rows)
```

### Task 13

Show a list of musicians playing any of the following instruments:

- Guitar
- Saxophone
- Cello
- Violin
- Harp

> You are not allowed to use the `OR` operator.

**Your result should look like this:**

```
 first_name |   last_name    |    date_of_birth    | instrument
------------+----------------+---------------------+------------
 Aaliyah    | Ahmas          | 1991-02-03 09:47:31 | Harp
 Noah       | Muller         | 1950-09-14 16:59:59 | Cello
 Amelia     | Martí          | 1963-10-15 14:22:20 | Violin
 Chloe      | Nguyen         | 1961-02-25 21:25:29 | Violin
 Julia      | Masferrer      | 1990-06-18 05:20:34 | Harp
 Lucas      | Young          | 1961-01-31 20:00:49 | Violin
 ...        1 ...            1 ...                 | ...
```

### Task 14

Finally, clear the table `musician` of all data.

> You are not allowed to use the command `DELETE FROM`.

Then, select all rows and columns from that table.

**Your result should look like this:**

```
 first_name | last_name | date_of_birth | instrument
------------+-----------+---------------+------------
 (0 rows)
```
