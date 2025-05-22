# PostgreSQL Basic Usage

## Run PostgreSQL from the terminal

1. Switch user before accessing postgresql prompt
    
    - Switch to the postgres superuser

        ```shell
        sudo su postgres
        ```

    - Login to the PostgreSQL Command Line

        ```shell
        psql
        ```

2. Access prompt and switch user at the same time

    ```shell
    sudo -u postgres psql
    ```

**Changing superuser password:**

```sql
ALTER USER postgres PASSWORD '<new-password>';
```

**Run an existing sql script:**

```sql
\i '<path-to-sql-script>'
```

