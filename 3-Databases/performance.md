# Database Performance

## 17.06.25 - Indexing and analyzing queries

- Causes of performance issues
- What is a dB Index?
- Different types of indexes
- Benefits of Database indexing
- Using the `EXPLAIN` command
- Creating a DB Index

### Causes of performance issues

1. Lack of indexes
2. Inefficient Querying
3. Improper Data Types
4. Lack of Maintenance
5. Hardware Limitations

### What is database index?

- Is a data structure that improves the speed of data retrieval operations on a database table at the cost of additional writes and storage space to maintain the index structure.
- Indexes are used to quickly locate data without having to search every row in a database every time the table is accessed, significantly enhancing the query performance and data access efficiency.

- Indexes can be created using one or more columns of a database table, providing the basis for both rapid random lookups and efficient access of ordered records.
- An index is a copy of the selected columns of data from the table, designed to enable a very efficient search. It normally includes a "key" or direct link to the original row of data from which it was copied, to allow the complete row to be retrieved efficiently.

**Benefits of Data Indexing:**

1. Improved Query Performance
2. Efficient Data Access
3. Optimized Dat Sorting
4. Consistent Data Performance

### Types of indexes

1. **Clustered Indexes**:

    - Reorder the table to match the index, which means the table itself will be sorted according to the index.
    - This type of indexing is beneficial for range queries

        - Clustered indexes are unique to each table, meaning a table can have only one clustered index.
        - They provide faster data retrieval for queries that involve sorting or range-based searches
        - They can slow down data modification operations like inserts updates and deletes.

2. **Non-Clustered Indexes**:

    - These are maintained separately for the table data.
    - They store a sorted list of values along with pointers to the corresponding rows in a the table, allowing for efficient data retrieval without altering the physical order of the table.

        - Can be created on multiple columns, providing flexibility for various query patterns.
        - They are useful for queries that require searching, filtering or joining tables
        - They require additional storage space and can impact write performance

3. **Composite Indexes**:

    - Include multiple columns to optimize queries with multiple conditions. 
    - They are particularly useful for complex queries that involve filtering or sorting based on multiple columns.

        - Can significantly enhance query query performance by reducing the number of scanned rows.
        - they are beneficial for queries with multiple `WHERE` clause conditions.
        - The require careful planning to ensure the correct columns are included in the index.

4. Partial Indexes:

    - Partial indexes are created on a subset of data to optimize the performance for specific queries. 
    - They are useful when only a portion of the tables data is being queried frequently

        - Reduce storage overheads compared to full-table indexes
        - They improve query performance for specific data subsets, such as active records or recent transactions.
        - Require a careful analysis to identify the appropriate subset of data for indexing

### `EXPLAIN` command

- accepts statements such as `SELECT`, `UPDATE`, `DELETE`, etc
- executes the statement
- Provides a query plan detailing the approach the planner took to executing the statement provided, instead of returning the data

**Syntax:**

```sql 
EXPLAIN [ANALYZE]
SELECT *
FROM <table_name>
[filtering commands]
```

```sql
EXPLAIN ANALYZE 
SELECT * 
FROM accounts 
WHERE customer_id = 3 AND account_type = 'Checking' 
ORDER BY created_at;
```

```shell
                                                QUERY PLAN                                                
----------------------------------------------------------------------------------------------------------
 Sort  (cost=19.76..19.77 rows=1 width=30) (actual time=0.015..0.015 rows=1 loops=1)
   Sort Key: created_at
   Sort Method: quicksort  Memory: 25kB
   ->  Seq Scan on accounts  (cost=0.00..19.75 rows=1 width=30) (actual time=0.009..0.010 rows=1 loops=1)
         Filter: ((customer_id = 3) AND ((account_type)::text = 'Checking'::text))
         Rows Removed by Filter: 4
 Planning Time: 0.058 ms
 Execution Time: 0.030 ms
(8 rows)
```

### Creating an index in PostgreSQL

```sql
CREATE INDEX [IF NOT EXISTS] <index-name>
ON <table-name>(<column-1>, <column-2>, <column-3>, ...);
```

- By default this command uses the B-tree index, which is appropriate for most cases

