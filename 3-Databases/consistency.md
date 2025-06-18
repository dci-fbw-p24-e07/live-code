# Consistency 

## 12.06.25 - DB Consistency and ACID principles

- What is DB Consistency?
- What are ACID principles?
- ACID vs BASE principles
- Example application ACID principles

### What is DB Consistency?

- The state of data in which all copies or instances are the same across all systems and databases.
- Helps to ensure that the data is accurate, up-to-date and coherent across database systems, applications and platforms.
- It ensures that the users of data can trust the information they are accessing.
- Implementing data validation rules, data standardization techniques and data synchronization processes are a few ways we can ensure data consistency
- We employ ACID principles to ensure the data consistency

### ACID principles

![ACID Principles](example_imgs/ACID.png)

1. **Atomicity**:

    - A transaction is treated as a single, indivisible unit.
    - All operations in a transaction must be completed fully or not at all. 
    - If any part of the transaction fails, the system should rollback the entire transaction

2. **Consistency**:

    - Ensures that a transaction brings the database from one valid state to another valid state while adhering to predefined rules and constraints.
    - After completing a transaction, the data must meet all the database integrity rules.

3. **Isolation**:

    - Prevents transactions from interfering with each other. 
    - When multiple transactions are executed simultaneously, isolation ensures they don't affect each other's outcomes.
    - Each transaction must be isolated to avoid conflicts - especially in high-concurrency environments.

4. **Durability**:

    - Guarantees that once a transaction is completed, its changes are permanently stored in the database. 
    - This ensures that data remains intact and accessible after failures.

#### ACID principles in a Relational Database

```sql
-- Transaction 1
INSERT INTO menu_a(food_a)
VALUES 
    ('Grapefruit'),
    ('Mango');

-- Transaction 2
INSERT INTO menu_b(food_b)
VALUES 
    ('Grapefruit'),
    ('Mango');
```

1. Beginning a transaction:

    ```sql
    BEGIN TRANSACTION;

    -- OR
    BEGIN WORK;

    -- OR
    BEGIN;
    ```

    **Example:**

    ```sql
    BEGIN TRANSACTION;

    INSERT INTO menu_a(food_a)
    VALUES 
        ('Grapefruit'),
        ('Mango');

    INSERT INTO menu_b(food_b)
    VALUES 
        ('Grapefruit'),
        ('Mango');
    ```

2. Committing a transaction:

    - Applies the changes to the database.

    ```sql
    COMMIT TRANSACTION;

    -- OR 
    COMMIT WORK;

    -- OR
    COMMIT;
    ```

    **Example:**

    ```sql
    BEGIN TRANSACTION;

    INSERT INTO menu_a(food_a)
    VALUES 
        ('Grapefruit'),
        ('Mango');

    INSERT INTO menu_b(food_b)
    VALUES 
        ('Grapefruit'),
        ('Mango');

    COMMIT;
    ```

3. Rolling back a transaction:

    - Undoes any changes that were made within the transaction

    ```sql
    ROLLBACK TRANSACTION;

    -- OR
    ROLLBACK WORK;

    -- OR 
    ROLLBACK;
    ```

    **Example:**

    ```sql
    BEGIN TRANSACTION;

    INSERT INTO menu_a(food_a)
    VALUES 
        ('Grapefruit'),
        ('Mango');

    INSERT INTO menu_b(food_b)
    VALUES 
        ('Grapefruit'),
        ('Mango');

    ROLLBACK;
    ```

**Sample  transaction script:**

```sql
BEGIN;

-- Step1: Debit 500 from account 1
UPDATE accounts 
SET balance = balance - 500
WHERE account_id = 1;

-- Step 2: Credit 500 to Account 3
UPDATE accounts 
SET balance = balance + 500
WHERE account_id = 3;

-- Step 3: Record transaction
INSERT INTO transactions (account_id, transaction_type, amount, description) VALUES (1, 'Transfer', 500.00, 'School fees');

-- Commit the transaction if both steps succeed
COMMIT;

-- Rollback if any error occurs
ROLLBACK;
```

### ACID vs BASE principles in NoSQL DB's

- BASE is an acronym for Basically Available, Soft state, Eventual consistency.
- Focuses on availability and flexibility over strict consistency.

- Basically available: The system guarantees availability, meaning it will respond to requests even if some parts of the system are down or unreachable.
- Soft state: Due to asynchronous updates, the system's state may change over time, even without input.
- Eventual consistency: Data will eventually become consistent, but there may be periods when it is temporarily inconsistent.


| Feature | **ACID** | **BASE** |
|---------|----------|----------|
| Full Form | Atomicity, Consistency, Isolation, Durability | Basically Available, Soft state, Eventually consistent |
| Core principle | Ensure reliable and consistent transactions | Prioritizes availability and performance over strict consistency |
| Data integrity | High - Guarantees data integrity at all times | Lower - Allows temporary inconsistencies |
Transaction handling | Transactions must complete fully or not at all | Best-effort transactions - may be incomplete or inconsistent temporarily |
| Scalability | Limited - works best with monolithic or traditional relational databases | High - Designed for distributed, scalable systems |
| Latency | Higher - Due to strict consistency requirements | Lower - Allows for faster response times |
| Use cases | Financial transactions, inventory management, order processing | Social media platforms, real-time analytics, content delivery network |

## 13.06.25 - Locks & Stored procedures

- What are database Locks?
- Types of locks available
- Implementing the locking mechanisms that PostgreSQL provides
- What are stored procedures?
- How to implement a stored procedure

### What are database locks?

- A mechanism to control access to database objects such as tables, rows, or entire database files. 
- It prevents conflicts by ensuring each transaction can safely modify or access data without interference. 
- This helps achieve data integrity in high-concurrency environments.
- Locks are essential for managing concurrent data access, ensuring data consistency, and preventing conflicts. 
- It restricts simultaneous access to a database object, avoiding conflicts by ensuring each transaction’s data access remains consistent and isolated. 
- They are categorized into different levels of restriction, from preventing all access to allowing read-only access.

**Types of Locks in PostgreSQL**

1. Access Exclusive (AEX) Locks
    - Purpose: Prevent any other transactions from accessing or modifying the locked object.
    - Usage: Typically used for destructive operations like dropping or truncating a table.

2. Exclusive (EX) Locks
    - Purpose: Prevent other transactions from modifying the locked object but allow them to read it.
    - Usage: Commonly used when performing updates that modify the structure of an object, such as adding or removing columns from a table.

3. Share (SH) Locks
    - Purpose: Allow multiple transactions to read the same object concurrently but prevent modifications.
    - Usage: Used during read-only operations like SELECT queries.

4. Row Share (RS) and Row Exclusive (RX) Locks
    - Row Share (RS) Locks: Allow multiple transactions to read the same row concurrently but prevent modifications.
    - Row Exclusive (RX) Locks: Allow a transaction to modify a row but prevent other transactions from reading or modifying it.

**How Locks Work in PostgreSQL**

- In PostgreSQL, locks are acquired automatically by the database system whenever a transaction accesses or modifies a database object. 
- The database system uses a lock manager to keep track of which locks are held by which transactions, and it uses a lock escalation mechanism to avoid having too many locks in memory.

- When a transaction attempts to access an object that is already locked by another transaction, it will either wait for the lock to be released (if the lock mode is compatible), or it will be aborted with an error (if the lock mode is incompatible). This ensures that transactions are executed in a consistent and serializable manner.

### Implementing Lock in PostgreSQL

**Syntax:**

```sql
LOCK TABLE [ONLY] <table-name>
IN [lock-mode] [NOWAIT]
```

- table-name − The name of the existing table to lock, possibly qualified by its schema. Only that table is locked if ONLY is entered before the table name. The table and any possible descendant tables are locked if ONLY is not specified.
- lock-mode − Which locks this lock conflicts with is specified by the lock mode. The most restrictive lock mode, ACCESS EXCLUSIVE, is utilized if no lock mode is specified.
- [NOWAIT] simply tells not to wait for any lock to be released from the table, according to the current definition. If the lock is not gained, PostgreSQL will abort the transaction immediately.

> Note: The lock is held for the duration of the current transaction after it has been achieved. Locks are always released after a transaction; there is no UNLOCK TABLE command.

1. Access Share
    - These locks are acquired on a specific table via the PostgreSQL SELECT command. 
    - After acquiring these locks on the table, we are only able to read data from it and not able to edit it. 
    - Access exclusive is the only locking mode that conflicts with this PostgreSQL lock mechanism.

    **Syntax:**

    ```sql
    BEGIN;
    LOCK TABLE Email IN ACCESS SHARE MODE;
    SELECT * FROM Email;
    ```

2. Row Share
    - The SELECT will acquire this PostgreSQL Lock on the table FOR SHARE & SELECT FOR UPDATE statements. 
    - This lock conflicts with Exclusive & Access Exclusive modes of Locking.

    **Syntax:**

    ```sql
    BEGIN;
    LOCK TABLE Email IN ROW SHARE MODE;
    ```

3. Row Exclusive
    - The share row exclusive, share, access exclusive, and exclusive modes of PostgreSQL conflict with this lock. 
    - The locks on the table will be acquired by UPDATE, DELETE & INSERT statements.

    **Syntax:**

    ```sql
    BEGIN;
    LOCK TABLE Email IN ROW EXCLUSIVE MODE;
    ```

4. Share Update Exclusive
    - The share row exclusive, share, access exclusive, share update exclusive, and exclusive lock modes in PostgreSQL are incompatible with this lock. 
    - It will get control over PostgreSQL’s vacuum, index construction, edit table, and validate commands.

    **Syntax:**

    ```sql
    BEGIN;
    LOCK TABLE Email IN SHARE UPDATE EXCLUSIVE MODE;
    ```

5. Share
    - This lock is incompatible with the share row exclusive, share, access exclusive, share update exclusive, share, and exclusive modes. 
    - This lock mode will obtain locks from PostgreSQL’s create index command.

    **Syntax:**

    ```sql
    BEGIN;
    LOCK TABLE Email IN SHARE MODE;
    ```

6. Share Row Exclusive
    - This lock conflicts with the share row exclusive, share, access, share update, and share row exclusive, share, and exclusive modes.

    **Syntax:**

    ```sql
    BEGIN;
    LOCK TABLE Email IN SHARE ROW EXCLUSIVEMODE;
    ```

7. Exclusive
    - The share row exclusive, share, access exclusive, share update exclusive, share row exclusive, share, and exclusive modes of PostgreSQL clash with this lock. By using the refresh materialized view, one can obtain this lock.

    **Syntax:**

    ```sql
    BEGIN;
    LOCK TABLE Email IN EXCLUSIVE MODE;
    ```

8. Access Exclusive
    - The share row exclusive, share, access exclusive, share update exclusive, share row exclusive, share, access exclusive, and exclusive modes of PostgreSQL clash with this lock. 
    - Only the person who applied the lock to the table can access it when utilizing it.

    **Syntax:**

    ```sql
    BEGIN;
    LOCK TABLE Email IN ACCESS EXCLUSIVE MODE;
    ```

> **Note:** PostgreSQL employs multi-version concurrency control (MVCC) to ensure that data is available and consistent in high-concurrency contexts when a query requires modifying or deleting data. Since each transaction uses its copy of the database, neither write nor read operations will obstruct the other.

### What are stored procedures?

- Stored procedures provide a means to execute multiple SQL statements in a structured and reusable way. 
- They introduce advanced control structures and allow us to perform complex calculations, making it easier to build complex applications directly within the database. 
- By default, PostgreSQL supports three main procedural languages: SQL, PL/pgSQL, and C.

### Implementing a stored procedures

**SYNTAX:**

```sql
CREATE [OR REPLACE] PROCEDURE <procedure-name>(<parameter-list>)
LANGUAGE plpgsql
AS $$
DECLARE
-- variable declaration
BEGIN
-- stored procedure body
end; $$
```

- First, specify the name of the stored procedure after the create procedure keywords.
- Second, define parameters for the stored procedure. A stored procedure can accept zero or more parameters.
- Third, specify plpgsql as the procedural language for the stored procedure.

> Note that you can use other procedural languages for the stored procedure such as SQL, C, etc.

- Finally, use the dollar-quoted string constant syntax to define the body of the stored procedure.
- Parameters in stored procedures can have the in and inout modes but cannot have the out mode.

- A stored procedure does not return a value. You cannot use the return statement with a value inside a store procedure like this:

    ```
    return expression;
    ```

- However, you can use the return statement without the expression to stop the stored procedure immediately:

    ```
    return;
    ```

```sql
CREATE OR REPLACE PROCEDURE transfer(
   sender int,
   receiver int,
   amount dec
)
LANGUAGE plpgsql
AS $$
BEGIN
    -- subtracting the amount from the sender's account
    UPDATE accounts
    SET balance = balance - amount
    WHERE id = sender;
    -- adding the amount to the receiver's account
    UPDATE accounts
    SET balance = balance + amount
    WHERE id = receiver;
COMMIT;
END;$$;
```

- To call a stored procedure, you use the CALL statement as follows:

    ```SQL
    call stored_procedure_name(argument_list);
    ```

- For example, this statement invokes the transfer stored procedure to transfer $1,000 from Bob’s account to Alice’s account.

    ```SQL
    call transfer(1,2,1000);
    ```
