"""
Book Record
Author: Tatchakorn Saibunjom
Email: saitako@outlook.com

Schema Diagram: https://drawsql.app/
"""

import os

from db_handler.create_db import create_db
from db_handler.get_update import insert_book
from db_handler.db_conf import DB_PATH
from ui import main_ui

# if database is not exist
if not os.path.isfile(DB_PATH):
    create_db()

if __name__ == '__main__':
    test_insert_value = ('book a', '978-3-16-148410-0', 'reading', 'Fri Aug  6 13:45:20 2021')
    insert_book(test_insert_value)

    # main_ui.main()