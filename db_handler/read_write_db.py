from typing import Any, Union, List, Tuple

from datetime import datetime
from .db_conf import ConnectDB, TABLE_NAME

('book b', '978-3-16-148410-1', 'finished')

def insert_book(book_info: Union[List[str], Tuple[str]]) -> None:
    """insert a book to the database (title, isbn, tuple)"""
    with ConnectDB() as (conn, cur):
        cur.execute(f"""
            INSERT INTO {TABLE_NAME} 
            VALUES (?, ?, ?, "{datetime.now().strftime('%c')}")
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


def update_book_isbn(title: str, isbn: str) -> None:
    """
    Update book isbn
    """
    with ConnectDB as (conn, cur):
        cur.execute(f"""
            UPDATE {TABLE_NAME}
            SET isbn="{isbn}"
            WHERE title="{title}"
        """)
        conn.commit()