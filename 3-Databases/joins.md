# Joins

## 03.06.25 - Joins Basics and examples

- What are joins?
- Types of Joins and examples:
    1. Full Join
    2. Inner Join
    3. Left Join
    4. Right Join
    5. Left Outer Join
    6. Right Outer Join
- Common use cases

### What are joins?

- This is a way to combine/merge a two data sets using SQL.
- It is achieved through a `JOIN` SQL statement
- Joins will combine both tables into one complete result

### Types of joins

1. Inner Join:

    - Examine each row in the first table(menu_a). It compares each value in the the specified for first table with the value in the specified column of the second table (menu_b). 
    - If these values are equal they are added to the resulting set - creating a join

        ![Inner Join](example_imgs/PostgreSQL-Join-Inner-Join.png)

        ```sql
        SELECT a_id, food_a, b_id, food_b
        FROM menu_a -- first table(left)
        INNER JOIN menu_b -- second table
        ON food_a = food_b;
        ```

    **Use cases:**
    - Retrieving data from related tables
    - Establishing relationships between tables
    - Normalizing data into multiple tables to avoid redundancy
    - Combining data from different sources


2. Left Join:

    - It selects data from the left table and compares each value with the values from the right table
    - If these values are equal, the left join creates a new row that contains columns from both tables and adds the new row to the result set.
    - In the case that values are not equal, the left join creates a new row that contains columns from both tables. However if fills the columns fo the right table with the value `NULL`.

        ![Left Join](example_imgs/PostgreSQL-Join-Left-Join.png)

        ```sql
        SELECT a_id, food_a, b_id, food_b
        FROM menu_a
        LEFT JOIN menu_b
        ON food_a = food_b;
        ```

        **Use cases:**
        - Handling optional or missing data scenarios
        - Combining data while preserving all records from one table
        - Retrieving all records from the left table and only matching records from the right table

3. Left Outer Join:

    - Achieves the same result as a Left Join but only returns rows do not have a match from the right/second table
    - Uses a `WHERE` clause

        ![Left Outer Join](example_imgs/PostgreSQL-Join-Left-Join-with-Where.png)

        ```sql
        SELECT a_id, food_a, b_id, food_b
        FROM menu_a
        LEFT JOIN menu_b
        ON food_a = food_b
        WHERE b_id IS NULL;
        ```

4. Right Join

    - An inverse or reverse version of the Left Join.
    - If the values in both tabkes match, the right join creates a new row that contains values from both the tables
    - If the values are not equal, the right join creates a new row that contains columns from both tables, but fills the columns in the left table with `NULL`.

        ![Right Join](example_imgs/PostgreSQL-Join-Right-Join.png)

        ```sql
        SELECT a_id, food_a, b_id, food_b
        FROM menu_a
        RIGHT JOIN menu_b
        ON food_a = food_b;
        ```

        **Use cases:**
        - Handling optional or missing data scenarios
        - Combining data while preserving all records from one table
        - Retrieving all records from the right table and only matching records from the left table

5. Right Outer Join:

    - Achieves the same result as the Right Join but only returns rows that do not have a match from the left/first table
    - Uses the `WHERE` clause

        ![Right Outer Join](example_imgs/PostgreSQL-Join-Right-Join-with-Where.png)

        ```sql
        SELECT * 
        FROM menu_a 
        RIGHT JOIN menu_b
        ON food_a = food_b
        WHERE a_id IS NULL;
        ```

6. Full Join:

    - The Full Join contains all rows from both tables, with the matching rows from both sides if available.
    - In case there is no match, the columns will be filled with `NULL`

        ![Full Join](example_imgs/PostgreSQL-Join-Full-Outer-Join.png)

        ```sql 
        SELECT *
        FROM menu_a
        FULL OUTER JOIN menu_b
        ON food_a = food_b;
        ```



