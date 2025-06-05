# SQL's Data Definition Language

## Description

In this exercise, we will focus on creating and manipulating the structure of databases.

## Tasks

Unless indicated otherwise, you can choose to execute the following tasks using the terminal or using DBeaver (or a combination).

If you use DBeaver, all operations (except connecting to a database) must be done using SQL statements in the **SQL Editor**.

### Task 1

*For this task, execute the file **using the terminal** instead of DBeaver.*

Create a new database called `vehicles` with a table named `car_model`.

This table should have the following fields:

- **name**: The name of the car model (Corolla, Fabia,...)
- **make**: A string (Toyota, Skoda,...).
- **year_of_checkin**: A string representing the year.
- **engine_type**: A string (gas, diesel, electric,...).
- **stock**: An integer representing the amount of cars in stock.

> For the text fields (strings) use any length you consider appropriate.

You must write two SQL statements, one for the database and another one for the table.

Write the two statements on a file named `vehicles.sql`, one after the other and separated by a new line.

> **Hint**: connect to the newly created database before creating the table.

**Your result should look similar to this:**

```
CREATE DATABASE
psql (14.0, server 13.4)
SSL connection (protocol: TLSv1.2, cipher: ECDHE-RSA-AES256-GCM-SHA384, bits: 256, compression: off)
You are now connected to database "vehicles" as user "postgres".
CREATE TABLE
vehicles=#
```

### Task 2

*For this task, execute the file **using the terminal** instead of DBeaver.*

Now, we forgot to tell you another field was required: `engine_type` (a text string). Take the file you created on the previous task, and add this field on the statement that creates the table.

Execute the entire file again (execute the statements to create both the database and table again).

Since the script now produces an error, add another statement at the top to remove the database, so that it can create it again.

**Your result should look similar to this:**

```
DROP DATABASE
CREATE DATABASE
psql (14.0, server 13.4)
SSL connection (protocol: TLSv1.2, cipher: ECDHE-RSA-AES256-GCM-SHA384, bits: 256, compression: off)
You are now connected to database "vehicles" as user "postgres".
CREATE TABLE
vehicles=#
```

Finally, manually delete the database, then execute the script again.

> To manually delete the database, you can simply run the SQL statement or use the DBeaver UI.

**Your result should look like this**

```
psql:vehicles.sql:1: NOTICE:  database "vehicles" does not exist, skipping
DROP DATABASE
CREATE DATABASE
psql (14.0, server 13.4)
SSL connection (protocol: TLSv1.2, cipher: ECDHE-RSA-AES256-GCM-SHA384, bits: 256, compression: off)
You are now connected to database "vehicles" as user "postgres".
CREATE TABLE
vehicles=#
```

### Task 3

Add a new field named `number_of_doors` (of type Integer) to the table `car_model`.

This time, instead of modifying the initial script, removing the database and creating the table again, write an SQL statement that just adds the field to the table already existing in the database.

After that, check the columns of the table to make sure the new field has been added.

**Your result should look like this (or similar, if you use DBeaver):**

```
                         Table "public.car_model"
     Column      |          Type          | Collation | Nullable | Default
-----------------+------------------------+-----------+----------+---------
 name            | character varying(100) |           |          |
 make            | character varying(100) |           |          |
 year_of_checkin | character varying(4)   |           |          |
 engine_type     | character varying(10)  |           |          |
 stock           | integer                |           |          |
 number_of_doors | integer                |           |          |

```

### Task 4

Now, someone realized the field named `year_of_checkin` actually stores the year of manufacture.

Write another SQL statement that changes the name of the field to `year_of_manufacture` without creating the table anew.

Again, check the columns of the table to make sure the field has been renamed.

**Your result should look like this (or similar, if you use DBeaver):**

```
                           Table "public.car_model"
     Column          |          Type          | Collation | Nullable | Default
---------------------+------------------------+-----------+----------+---------
 name                | character varying(100) |           |          |
 make                | character varying(100) |           |          |
 year_of_manufacture | character varying(4)   |           |          |
 engine_type         | character varying(10)  |           |          |
 stock               | integer                |           |          |
 number_of_doors     | integer                |           |          |

```

### Task 5

Seems like the initial definition had a few errors and you realized the values in the field `year_of_manufacture` should be integers and they are now strings.

Change the type of the field to integer.

> **Hint**: You may get an error the first time. Read the error description and the hint provided by the error. Follow its advice.

Again, check the columns of the table to make sure the field type has been changed.

**Your result should look like this (or similar, if you use DBeaver):**

```
                           Table "public.car_model"
     Column          |          Type          | Collation | Nullable | Default
---------------------+------------------------+-----------+----------+---------
 name                | character varying(100) |           |          |
 make                | character varying(100) |           |          |
 year_of_manufacture | integer                |           |          |
 engine_type         | character varying(10)  |           |          |
 stock               | integer                |           |          |
 number_of_doors     | integer                |           |          |

```

### Task 6

You know what? this field is giving you a lot of problems, so just delete it.

> Use an SQL statement, of course.

Again, check the columns of the table to make sure the field has been removed.

**Your result should look like this (or similar, if you use DBeaver):**

```
                           Table "public.car_model"
     Column          |          Type          | Collation | Nullable | Default
---------------------+------------------------+-----------+----------+---------
 name                | character varying(100) |           |          |
 make                | character varying(100) |           |          |
 engine_type         | character varying(10)  |           |          |
 stock               | integer                |           |          |
 number_of_doors     | integer                |           |          |

```
