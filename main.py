"""
Book Record
Author: Tatchakorn Saibunjom
Email: saitako@outlook.com

Schema Diagram: https://drawsql.app/
"""

import os
from datetime import datetime

from db_handler.create_db import create_db
from db_handler.get_update import (
    insert_book,
    get_all_books,
    get_books_from_status,
    update_book_status,
)
from db_handler.db_conf import DB_PATH

# from ui import main_ui

# if database is not exist
if not os.path.isfile(DB_PATH):
    create_db()

if __name__ == '__main__':
    test_insert_value = ('book a', '978-3-16-148410-0', 'reading', 'Fri Aug  6 13:45:20 2021')
    insert_book(test_insert_value)
    print(get_all_books())

    print(get_books_from_status('reading'))
    update_book_status('book a', 'suspended')
    print(get_books_from_status('suspended'))
    # datetime.now().strftime('%c')
    