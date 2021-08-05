import sqlite3
from db_conf import *

# Insert many
# VALUES ('John', 'Brown', 'john@elder.com')
# cur.executemany("INSERT INTO customers VALUES (?, ?, ?)", customers)
# conn.commit()

def insert_one():
    with ConnectDB as (conn, cur):
        cur.execute("""
            INSERT INTO customers 
            VALUES ('John', 'Brown', 'john@elder.com')
        """)
        conn.commit()


def update_db():
    with ConnectDB as (conn, cur):
        cur.execute("""
            UPDATE customers
            SET first_name = 'Brian'
            WHERE rowid=6
        """)
        conn.commit()


def query_db():
    with ConnectDB as (conn, cur):
        # rowid is auto-generated
        query = "SELECT rowid, * FROM  customers"
        # query = "SELECT first_name FROM  customers WHERE  last_name='Cartman'"
        # query = "SELECT first_name, last_name FROM  customers WHERE  email LIKE '%cartman%'"
        
        cur.execute(query)
        # cur.fetchone()
        # cur.fetchmany(2)
        # cur.fetchall()
        return cur.fetchall()