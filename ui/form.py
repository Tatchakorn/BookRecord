from tkinter.constants import N
import PySimpleGUI as sg
from db_handler.read_write_db import insert_book

status_list = ('reading', 'suspended', 'plan-to-read', 'finished')

def add_book_form() -> str:
    """Add book form return a string message"""
    layout = [[sg.Text('Enter book information')],
            [sg.Text('Title', size=(10, 1)), sg.InputText(key='_TITLE_')],
            [sg.Text('ISBN', size=(10, 1)), sg.InputText(key='_ISBN_')],
            [sg.Text('Status', size=(10, 1)), sg.Combo(status_list,key='_STATUS_')],
            [sg.Button('Submit'), sg.Button('Cancel')]]
    window = sg.Window('Simple Data Entry Window', layout,  default_element_size=(50,50))
    event, values = window.read(close=True)
    if event == 'Submit'and not None in (values['_TITLE_'], values['_STATUS_']):
        insert_book((values['_TITLE_'], values['_ISBN_'], values['_STATUS_']))
        return 'Book added'
    
    if event == 'Cancel': return 'Cancled'
    
    return 'Book was not added'