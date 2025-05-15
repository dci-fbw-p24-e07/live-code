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

