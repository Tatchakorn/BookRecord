from sqlite3.dbapi2 import Error
from .db_conf import ConnectDB, TABLE_NAME
from typing import Any, Union, List, Tuple

# Insert many
# VALUES ('John', 'Brown', 'john@elder.com')
# cur.executemany("INSERT INTO customers VALUES (?, ?, ?)", customers)
# conn.commit()

def insert_book(book_info: Union[List[str], Tuple[str]]) -> None:
    """insert a book to the database"""
    with ConnectDB() as (conn, cur):
        cur.execute(f"""
            INSERT INTO {TABLE_NAME} 
            VALUES (?, ?, ?, ?)
        """, book_info)
        conn.commit()


def get_all_books() -> List[Tuple[Any]]:
    """get all books"""
    books = None
    with ConnectDB() as (conn, cur):
        query = f'SELECT rowid, * FROM  {TABLE_NAME}'    
        cur.execute(query)
        books = cur.fetchall()
    return books


def get_books_from_status(status: str) -> List[Tuple[Any]]:
    """get all books from status"""
    books = None
    with ConnectDB() as (conn, cur):
        query = f'SELECT rowid, * FROM  {TABLE_NAME} WHERE status="{status}"' 
        cur.execute(query)
        books = cur.fetchall()
    return books


def update_book_status(title: str, status: str) -> None:
    """Update book status"""
    with ConnectDB() as (conn, cur):
        cur.execute(f"""
            UPDATE {TABLE_NAME}
            SET status="{status}"
            WHERE title="{title}"
        """)
        conn.commit()


def update_book(id: int, key: str, val: str) -> None:
    """
    Update arbitary (key, value) from rowid
    """
    with ConnectDB as (conn, cur):
        cur.execute(f"""
            UPDATE {TABLE_NAME}
            SET {key} = "{val}"
            WHERE rowid={id}
        """)
        conn.commit()
