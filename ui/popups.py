import PySimpleGUI as sg
from db_handler.read_write_db import insert_book, update_book

status_list = ('reading', 'suspended', 'plan-to-read', 'finished')

def add_update_book_form(title: str = '', 
                         isbn: str = '', 
                         status: str = 'reading', 
                         update: bool=False,
                         id: int = None) -> str:
    """Add book form return a string message"""
    layout = [
        [sg.Text('Enter book information')],
        [
            sg.Text('Title', size=(10, 1)), 
            sg.InputText(key='_TITLE_', default_text=title)
        ],
        [
            sg.Text('ISBN', size=(10, 1)), 
            sg.InputText(key='_ISBN_', default_text=isbn)
        ],
        [
            sg.Text('Status', size=(10, 1)), 
            sg.Combo(status_list, key='_STATUS_', default_value=status)
        ],
        [sg.Button('Submit'), sg.Button('Cancel')],
    ]
    window = sg.Window('add book', layout,  default_element_size=(50,50))
    event, values = window.read(close=True)
    
    # database constraints
    ACCEPT_STATUS = ('reading', 'plan-to-read', 'suspended', 'finished')
    if '' in (values['_TITLE_'], values['_STATUS_']) or values['_STATUS_'] not in ACCEPT_STATUS:
        return 'Book was not added'
    
    if event == 'Submit':
        if update:
            update_book(id, values['_TITLE_'], values['_STATUS_'], values['_ISBN_'])
            return 'Book updated'
        else:
            insert_book((values['_TITLE_'], values['_ISBN_'], values['_STATUS_']))
            return 'Book added'
    
    if event == 'Cancel': return 'Cancled'


def popup_no_select(action: str) -> None:
    layout = [
        [sg.Text(f'Select an item you want to {action}!')],
        [sg.Button('close')],
    ]
    window = sg.Window(f'No selection', layout, default_element_size=(50,50))
    event, values = window.read(close=True)


def popup_confirm(action: str) -> bool:
    layout = [
        [sg.Text(f'Are you sure you want to {action} this item?')],
        [sg.Button('Yes'), sg.Button('No')],
    ]
    window = sg.Window(f'{action} book', layout, default_element_size=(50,50))
    event, values = window.read(close=True)
    print(event)
    if event == 'Yes':
        return True
    return False