from typing import Any, Union, List, Tuple

from datetime import datetime
from .db_conf import ConnectDB, TABLE_NAME

def insert_book(book_info: Union[List[str], Tuple[str]]) -> None:
    """insert a book to the database (title, isbn, tuple)"""
    with ConnectDB() as (conn, cur):
        cur.execute(f"""
            INSERT INTO {TABLE_NAME} 
            VALUES (?, ?, ?, "{datetime.now().strftime('%c')}")
        """, book_info)
        conn.commit()


def get_all_books(cols: Union[List[str], Tuple[str]] = []) -> List[Tuple[Any]]:
    """get all books"""
    books = None
    cols = 'rowid, *' if not cols else ' '.join(cols) # defualt select all
    with ConnectDB() as (conn, cur):
        query = f'SELECT {cols} FROM  {TABLE_NAME}'    
        cur.execute(query)
        books = cur.fetchall()
    return books


def get_book_status(id: int) -> Tuple[str]:
    """get all books"""
    status = None
    with ConnectDB() as (conn, cur):
        query = f'SELECT {cols} FROM  {TABLE_NAME}'    
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


def get_book_from_title(title: str) -> Tuple[Any]:
    books = None
    with ConnectDB() as (conn, cur):
        query = f'SELECT rowid, * FROM  {TABLE_NAME} WHERE title="{title}"'
        cur.execute(query)
        books = cur.fetchone()
    return books


def delete_book(id: int) -> None:
    with ConnectDB() as (conn, cur):
        query = f'DELETE FROM {TABLE_NAME} WHERE rowid={id}'
        cur.execute(query)
        conn.commit()



def update_book(id: int, title: str, status: str, isbn: str) -> None:
    """Update book status"""
    with ConnectDB() as (conn, cur):
        query = f"""
            UPDATE {TABLE_NAME}
            SET 
                title="{title}",
                status="{status}", 
                isbn="{isbn}", 
                updated_at="{datetime.now().strftime('%c')}"
            WHERE rowid={id}
        """
        cur.execute(query)
        conn.commit()