import psycopg2


def connect():
    """ 
    Connect to PostgreSQL Database Server
    """
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="suppliers",
            user="supplier_admin",
            password="supply123",
            port=5432
        )
        return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


def create_tables():
    commands = (
        """ 
        CREATE TABLE vendors (
            vendor_id SERIAL PRIMARY KEY,
            vendor_name VARCHAR(255) NOT NULL
        );
        """,
        """
        CREATE TABLE parts (
            part_id SERIAL PRIMARY KEY,
            part_name VARCHAR(255) NOT NULL
        );
        """,
        """ 
        CREATE TABLE part_drawings (
            part_id INTEGER PRIMARY KEY,
            file_extension VARCHAR(5) NOT NULL,
            drawing_data BYTEA NOT NULL,
            FOREIGN KEY (part_id)
            REFERENCES parts (part_id)
            ON UPDATE CASCADE 
            ON DELETE CASCADE
        );
        """,
        """ 
        CREATE TABLE vendor_parts (
            vendor_id INTEGER NOT NULL,
            part_id INTEGER NOT NULL,
            PRIMARY KEY (vendor_id , part_id),
            FOREIGN KEY (vendor_id)
                REFERENCES vendors (vendor_id)
                ON UPDATE CASCADE ON DELETE CASCADE,
            FOREIGN KEY (part_id)
                REFERENCES parts (part_id)
                ON UPDATE CASCADE ON DELETE CASCADE
        );
        """
    )
    
    try: 
        # Establish connection
        conn = connect()
        
        with conn.cursor() as cur:
            # Execute sql commands
            for command in commands:
                cur.execute(command)
            # Commit the changes through connection
            conn.commit()
        conn.close()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


def insert_vendor(vendor_name):
    """ 
    Insert a new vendor into the vendors table
    """

    sql = """ INSERT INTO vendors(vendor_name)
        VALUES(%s) RETURNING vendor_id;
        """
        
    try:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute(sql, (vendor_name,))
            
            # get the generated id back
            rows = cur.fetchone()
            if rows:
                vendor_id = rows[0]
            
            conn.commit()
        conn.close()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


def insert_many_vendors(vendor_list: list):
    """ 
    Insert a list of vendors into the vendors table
    """
    
    sql = """ INSERT INTO vendors(vendor_name)
        VALUES(%s) RETURNING *;
        """
    try:
        conn = connect()
        with conn.cursor() as cur:
            cur.executemany(sql, vendor_list)
            conn.commit()
        conn.close()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


def get_vendors():
    """ Retrieve data from the vendors table
    """
    conn = connect()
    with conn.cursor() as cur:
        # Execute the SELECT statement
        cur.execute("SELECT * FROM vendors ORDER BY vendor_name;")        
        row = cur.fetchone()
        print(row)
    conn.close()


def get_many_vendors(size=10):
    """ 
    Return a set of vendors limited by the size parameter.
    size: default=10
    """
    conn = connect()
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM vendors ORDER BY vendor_name;")
        rows = cur.fetchmany(size=size)
        
        while rows:
            print(rows)
            # Retrieve the next set of results
            rows = rows = cur.fetchmany(size=size)
    conn.close()
        
        
def get_all_parts():
    """ 
    Retrieves all parts from the database
    """
    conn = connect()
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM parts;")
        rows = cur.fetchall()
        print(rows)
    conn.close()
    
