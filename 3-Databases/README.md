# Intro to Databases

## 15.05.25 - Basics

- What is a database?
- Database Management Systems (DBMS)
- Types of DBMS's
- DBMS vs RDBMS
- Characteristics of Relation Data and its structure

### What is a database?

- Is an organized collection of data.
- This collection can be easily accessed, updated and managed
- It is designed, built to be populated with data for a specific purpose
- The structure of a database consists of 2 main parts:

    1. Data - the actual information to be stored in the database
    2. Metadata - The structural description of data in the database. It describes the names of fields used to store data, the length of those fields(where applicable) and their data types. It gives structure and organization to raw data.

### Database Management System (DBMS)

- Is a program that enables users to create, maintain and control access to databases.
- The main goal is to provide a safe, convenient and efficient environment for users to retrieve and store information
- A DBMS can hold more than one databases
- The DBMS is what would be used to interact with the databases by other programs or by the code.
- It allows you to manipulate, maintain, report and relate data within
- Examples of DBMS's include:

    - MySQL
    - PostgreSQL
    - Oracle
    - Microsoft SQL Server
    - SQLite
    - Firebase
    - Redis
    - Mongo

### Types of DBMS's

1. Relational Databases

    - Most commonly used databases
    - Data is stored in tables(relations)
    - These tables have columns(fields) and rows(records)
    - Each row has a unique key or field used as an identifier
    - Most relational databases use SQL(Structured Query Language)

2. Non-relational / NoSQL 

    - These are databases that don't use a relational model
    - They are favoured for their quick read-write operations
    - They allow you store data in unstructured or semi-structured setups
    - Each record can have varying data points from the others
    - There are 4 different types of Non-relational databases:

        1. Key-Value:
            - These are the simplest NoSQL databases
            - Every record is stored as a pair consisting of an attribute/key and a value
            - The structure is similar to a relational database except there two columns: Key and Value
            - These are typically used to store information temporarily eg. shopping carts, caching, user preferences, etc.

        2. Document:
            - These store data in JSON(JavaScript Object Notation), BSON(Binary-encoded JSON) or XML(Extensible Markup Language)
            - They make it easier to access and use your documents across different applications
            - In traditional SQL, data must often be assembled and disassembled when moving from one application to the other
            - They are very popular because the document structures can be reworked very easily to suit whatever application they're using

        3. Graph
            - These focus on the relationship between different data elements.
            - Each element is a node and the connections between elements are links or relationships
            - They can store data in a structured document similar to JSON, in a key-value format or as nodes to represent objects and edges to describe the relationship between them
            - Typically used for social networks and fraud detection

        4. Column-oriented:
            - These are organized and read as a column as opposed reading row by row in relational databases.
            - Typically used for analytics as columns are of the same type
            - Makes it easier to read data faster and aggregate a given column

### Characteristics and structure of relational data

- Relational data is organized using 3 features:

    1. Tables(relations): Represent a specific entity, object or concept. A database can have as many tables as possible
    2. Rows(Records): Each row in a table represents a single record. Tables can have as many records as possible
    3. Columns(Fields/Attributes): Each column represent a data field or attribute associated with the entity/object. These fields also determine the data type of the attribute.

- In order to separate records each row has a unique identifier known as a Primary Key
- We can link one table to the other(creating relationships) through Foreign Keys.
- Relational databases need to have ACID properties:

    1. Atomicity:
        - This enforces that data should always be accurate.
        - Data should always be compliant with the rules, regulations and policies of the business.
        - It also requires that all tasks succeed, or the transaction will rollback

    2. Consistency:
        - The state of the database must remain consistent throughout a transaction.
        - Defines rules for maintaining data points to ensure that the database remains in a correct state after transaction.
        - If the database has copies those copies also need to have consistency within them

    3. Isolation:
        - Each transaction is separate and not dependent on others
        - It keeps the effect of a transaction invisible until it is committed.

    4. Durability:
        - You can recover data from a failed transaction
        - Ensures that data changes are permanent

## 16.05.25 - Relational Modeling

- What is a relational model?
- Key Terms in Relational Models
- Examples of Models
- Primary Keys
- Foreign Keys
- Constraints
- Referential Integrity

### What is a relational model?

- Is an approach to logically represent and manage the data stored in a database
- The data is organized into a collection to tow-dimensional inter-related tables, also known as relations.
- Each relation is a collection of columns and rows, where the column represents the attributes of an entity and rows(tuples) represent the records.
- The use tables makes it straightforward, efficient and flexible to store and access structured information.

#### Key Terms in Relational Models

1. Attribute: Are the properties that define an entity.
    - Example: `employee_id`, `email_address`, `dept`, etc

2. Relation Schema: Sometimes known simply a Schema. Defines the structure of the relation and represents the name of the relation with its attributes.
    - Example: `student(student_id, name, address, phone, email, age, class)`

3. Tuple: Represents a row in a relation. Each tuple contains a set of attribute values that describe a particular entity.
    - Example: `(134, "Jason", "49 Waller Avenue", "+12334545232", "jason@school.com", 28, "CS50")`

4. Column: Represents a set of values for a particular attribute(field)
    - Example: When you extract the column `phone` from `student`

5. NULL values: This is a value which is not known or unavailable. It is represented by `NULL`
    - Example: The `age` field of a `student` having `student_id` 176 is `NULL`

6. Relation Instance: The set of tuples of a relation at a particular instance of time. It can change whenever there is an insertion, deletion or update to the database.

7. Degree: The number of attributes in the relation.
    - Example: Table `student` has a degree of 7.

8. Cardinality: The number of tuples in a relation.
    - Example: The `student` table has a cardinality of 35.

### Example Models

- Create a `student` table that has the following attributes/fields:
    1. `student_id`
    2. `name`
    3. `address`
    4. `phone`
    5. `email`
    6. `age`
    7. `class`

    ![Students UML](example_imgs/students_uml.png)

    ![Students Table](example_imgs/students_model.png)

### Keys in Relational Models

1. Primary Key:
    - Identifies each tuple in a relation.
    - It must contain unique values
    - It must not be `NULL`
    - It is usually best to let the database handle generation of Primary Keys when you insert records
    - Example: `student_id` is the primary key in the `student` table.

2. Foreign Key:
    - an attribute in one relation that refers to the primary key of another relation
    - It establishes relationships between tables.
    - Example: `class_id` in the `students`table that link the class table

    ![Foreign Key](example_imgs/foreign_key.png)

### Constraints in Relational Models

- Constraints are conditions that we define when creating the database.
- These conditions need to be upheld when interacting with the database
- They are checked before performing any CRUD(Create, Read, Update, Delete) operation 
- If any constraint is violated the operation will fail

1. Domain Constraints:

    - Ensures that the value of each attribute in a tuple must be an atomic value derived from its specific domain.
    - Domains are defined by the data types associated with attributes/fields
    - Common data types include:
        1. Numeric Types: 
            - Integers(short, regular, long) for whole numbers
            - Real numbers(float, double-precision) for decimal values

        2. Character types:
            - Fixed-length(CHAR)
            - Variable-length (VARCHAR, TEXT) used for storing text data of various sizes

        3. Boolean Values: 
            - Stores True or False
            - Often used for flags or conditional checks

        4. Specialized Types:
            - date(DATE)
            - time(TIME)
            - timestamp(TIMESTAMP)
            - money(MONEY)
            - used for precise handling of time-related and financial data

2. Key Integrity:

    - Every relation in the database should have at least one attribute that defines the tuple uniquely.
    - That attribute is called a key
    - Keys have 2 main constraints:
        1. It should unique for all tuples
        2. It can't have `NULL` values

3. Referential Integrity:

    - When one attribute/field can only take values from another attribute/field, either from the same table or from a different table
    - It dictates that there must be only one primary key value for a foreign key
    - Referential integrity is usually violated when:
        - Primary keys are not properly enforced
        - Foreign keys are not properly enforced
        - Database design is incorrect

    - To ensure referential integrity we must:
        - Create primary and foreign keys for each table
        - Ensure that the data types for the primary and foreign keys are matching
        - Ensure there are no duplicate entries
        - Make sure not to create circular relationships

### Installing PostgreSQL

1. Update the local package index:

    ```shell
    sudo apt update
    ```

2. Install the Postgres package along with the `-contrib` package that adds some extra utilities and functionality:

    ```shell
    sudo apt install postgresql postgresql-contrib
    ```

3. Ensure that the server is running using the `systemctl start` command:

    ```shell
    sudo systemctl start postgresql.service
    ```

4. Check the status of the server:

    ```shell
    sudo systemctl status postgresql.service
    ```












