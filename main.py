"""
Book Record
Author: Tatchakorn Saibunjom
Email: saitako@outlook.com

Schema Diagram: https://drawsql.app/
"""

import os

from db_handler.create_db import create_db
from db_handler.db_conf import DB_PATH
from ui import main_ui

# if database is not exist
if not os.path.isfile(DB_PATH):
    create_db()

if __name__ == '__main__':
    main_ui.main()