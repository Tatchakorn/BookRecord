"""
Call once or lose all data !!
"""

from .db_conf import ConnectDB, TABLE_NAME
from sqlite3 import Error

# Mysqlite3 has 5 data types
# 1. NULL -> None
# 2. INTEGER -> int
# 3. REAL -> float
# 4. TEXT -> str
# 5. BLOB -> bytes


# Example
# rowid is auto-generated
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
        # example row 
        # status = {'reading', 'plan-to-read', 'suspended', 'finished'}
        # ('book a', '978-3-16-148410-0', 'reading', 'Fri Aug  6 13:45:20 2021')
        sql_create_table = f""" 
            CREATE TABLE {TABLE_NAME}(
                title TEXT UNIQUE NOT NULL,
                isbn TEXT,
                status TEXT NOT NULL,
                updated_at TEXT)
            """
        try:
            cur.execute(sql_create_table)
        except Error as e:
            print('[ERROR] DB not created', e)
        else:
            # Commit the command
                conn.commit()