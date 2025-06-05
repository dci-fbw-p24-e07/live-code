# Advanced SQL - Data types II

## Description

In this exercise, we will practice extensively with the more complex and versatile types.

## Data

This exercise uses data from the previous unit (Advanced SQL - Data Types I). You can use your own data from that exercise or you can create a new database and load the [initial content](src/data/initial.sql).

The initial content for this exercise includes:

- Table **site_user**
  - Field **id**: `integer`, `PRIMARY KEY`
  - Field **name**: `varchar(25)`
  - Field **uuid**: `uuid`
  - Field **avatar**: `bytea`
  - Field **role**: `role_type` AS `ENUM`
  - Field **birthdate**: `date`
  - Field **siblings**: `text[]`
  - Field **availability**: `time[][]`
  - Field **site_settings**: `json`
  - Field **created_on**: `timestamp`
  - Field **active_for**: `interval`

##

## Tasks

###

### Task 1

Produce a list of users who have more than one child.

Your query should return only one user: Miriam.

### Task 2

Good news! Luoise Clark just gave birth to Jordi, so you've been tasked with adding him to her siblings field.

Then, execute again the statement of the previous task to confirm it works and now returns Miriam and Louise.

### Task 3

Louise will be on a temporary leave, but between 9 and 10 in the morning she can check emails and be contacted at home if something urgent arises, so you've been tasked with setting her availability accordingly.

> You may replace the availability array with a new one.

### Task 4

Louise's site notifications should be turned off as well.

> You may **not** replace the site_settings field this time.

### Task 5

Also, the system is left without moderator for a while, so it has been decided to promote someone to the role Moderator.

First, write an SQL statement to find everyone who has a role below Moderator, so that it can be decided who to promote.

You will find out there is only one, Johann, so your task now will be to promote him to Moderator.

### Task 6

Produce a list showing which users have their notifications turned off.

The answer should be: Miriam & Louise.

### Task 7

Produce a list showing which users don't have any custom background color for the site.

The answer should be: Louise and Johann.
