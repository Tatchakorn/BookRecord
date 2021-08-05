"""
Call once or lose all data !!
"""

from .db_conf import *

# Mysqlite3 has 5 data types
# 1. NULL -> None
# 2. INTEGER -> int
# 3. REAL -> float
# 4. TEXT -> str
# 5. BLOB -> bytes

# Example
# -- projects table
# CREATE TABLE IF NOT EXISTS projects (
# 	id integer PRIMARY KEY,
# 	name text NOT NULL,
# 	begin_date text,
# 	end_date text
# );

# -- tasks table
# CREATE TABLE IF NOT EXISTS tasks (
# 	id integer PRIMARY KEY,
# 	name text NOT NULL,
# 	priority integer,
# 	project_id integer NOT NULL,
# 	status_id integer NOT NULL,
# 	begin_date text NOT NULL,
# 	end_date text NOT NULL,
# 	FOREIGN KEY (project_id) REFERENCES projects (id)
# );

def create_db() -> None:
    """
    Create a Table
    """
    with ConnectDB() as (conn, cur):
        sql_create_table = """ 
            CREATE TABLE customers(
                first_name TEXT,
                last_name TEXT,
                email TEXT)
            """
        cur.execute(sql_create_table)
        # Commit the command
        conn.commit()