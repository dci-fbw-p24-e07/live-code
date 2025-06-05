# Subqueries

## 05.06.25 - Subquery basics

- What are subqueries?
- How to structure a subquery
- Subqueries in CRUD statements

### What are subqueries?

- A subquery/inner query/nested query is query within another query and embedded within the `WHERE` clause.
- It is used to return data that will be used in the main query as a condition to further restrict the data to be retrieved,
- Subqueries can be used with the `SELECT`, `INSERT`, `UPDATE` and `DELETE` statements along with operators like `=`, `<`, `>`, `>=`, `IN`, etc.
- Rules for creating subqueries:
    1. Subqueries must be enclosed in parentheses.
    2. A subquery can have only one column in the SELECT clause, unless multiple column are in the main query for the subquery to compare its selected columns.
    3. AN `ORDER BY` cannot be used in a subquery, although the main query can use an `ORDER BY`. The `GROUP BY` can be used to perform the same function as the `ORDER BY` in a subquery.
    4. Subqueries that return more than one row can only be used with multiple value operators, such as `IN`, `EXISTS`, `NOT IN`, `ANY`, `SOME`, `ALL`.
    5. The `BETWEEN` operator cannot be used with a subquery, however the `BETWEEN` operator can be used within the subquery.

**Structure of a subquery:**

```sql
-- Main query
SELECT <column-name(s)>
FROM <table(s)>
WHERE <column-name> <OPERATOR>
    -- Subquery
    (
        SELECT <column-name>
        FROM <table(s)>
        [WHERE]
    );
```

### Subqueries on CRUD operations

#### SELECT

- Subqueries are most frequently used with the `SELECT` statement.

```sql
SELECT *
FROM company
WHERE id IN (
    SELECT id 
    FROM company
    WHERE salary > 45000
    );
```

#### INSERT

- The `INSERT` uses the data returned from the subquery to insert data into another table.
- The selected data in the subquery can be modified using any of the character, date or number functions

```sql
INSERT INTO company_bkp
SELECT * FROM company
WHERE id IN (
    SELECT id 
    FROM company
);
```

#### UPDATE

- Either single or multiple columns can be updated in a table using the subquery on an `UPDATE` statement.

```sql
UPDATE company
SET salary = salary * 0.5
WHERE age IN (
    SELECT age 
    FROM company
    WHERE age >= 27
);
```

#### DELETE

```sql
DELETE FROM company
WHERE age IN (
    SELECT age
    FROM company_bkp
    WHERE age BETWEEN 22 AND 25
);
```

### Use cases

- Filtering data based on a condition derived from another query
- Comparing values between tables
- Simplifying complex queries by breaking them down into smaller parts
- Performing aggregation operations within a query