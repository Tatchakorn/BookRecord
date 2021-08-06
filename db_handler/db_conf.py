"""
Configurations & Connection
"""
import os
from sqlite3.dbapi2 import Error
from typing import Tuple
import sqlite3

DB_NAME = 'book.db'
DB_PATH = os.path.join(DB_NAME) # Add additional path later


class ConnectDB:
    def __init__(self) -> None:
        try:
            # create a database connection
            self.conn = sqlite3.connect(DB_PATH)
        except Error as e:
            print('[ERROR] DB not connected', e)
        self.cur = self.conn.cursor()

    def __enter__(self) -> Tuple[object]:
        return (self.conn, self.cur)
    
    def __exit__(self, type, value, traceback) -> bool:
        self.conn.close()
        return True