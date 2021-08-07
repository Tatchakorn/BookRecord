from typing import Any, List, Tuple
import PySimpleGUI as sg

from db_handler.read_write_db import get_books_from_status
from .form import add_book_form

## ----- CONFIGS ----- ##
sg.change_look_and_feel('Dark')
WIN_WIDTH = 60
WIN_HEIGHT = 100
BTN_FONT_SIZE = 16
LIST_BOX_W = WIN_WIDTH + 20
LIST_BOX_H = 10

bt = {'size': (WIN_WIDTH//4,2), 'font': ('Franklin Gothic Book', BTN_FONT_SIZE), 
    'button_color': ('black', 'green'), 'pad': (0,0)}

listbox_default_conf = {'values': [], 'enable_events': True, 
    'size': (LIST_BOX_W, LIST_BOX_H), 'visible': False}
## ----- WINDOW AND LAYOUT ----- ##

layout = [
    # App title
    [sg.Text('Book Record', size=(WIN_WIDTH,1)), sg.VSeparator(), sg.Button('Add Book', key='_ADD_')],
    [sg.Button('Reading', **bt, key='_READ_'), sg.Button('Suspended', **bt, key='_SUSPEND_'), 
        sg.Button('Plan to read', **bt, key='_PLAN_'), sg.Button('Finished', **bt, key='_FINISHED_'),],
    [sg.HSeparator()],
    [   
        sg.Listbox(**listbox_default_conf, key='_READ-LIST_'),
        sg.Listbox(**listbox_default_conf, key='_SUSPEND-LIST_'),
        sg.Listbox(**listbox_default_conf, key='_PLAN-LIST_'),
        sg.Listbox(**listbox_default_conf, key='_FINISH-LIST_'),
    ],
]

window = sg.Window(
    'Book Record', 
    layout=layout, 
    margins=(0,0),
    finalize=True,
    )

## ----- HELPER FUNCTIONS ----- ##

def format_book_text(books: List[Tuple[Any]]) -> List[str]:
    return (
        f'{book[1]}' 
        for book in books
    )


def hide_all_lists() -> None:
    window['_READ-LIST_'].update(visible=False)
    window['_SUSPEND-LIST_'].update(visible=False)
    window['_PLAN-LIST_'].update(visible=False)
    window['_FINISH-LIST_'].update(visible=False)

## ----- RENDER LIST ----- ##
st_elem = {
    'reading': '_READ-LIST_',
    'suspended': '_SUSPEND-LIST_',
    'plan-to-read': '_PLAN-LIST_',
    'finished': '_FINISH-LIST_',
}


def render(status: str) -> None:
    books = get_books_from_status(status)
    books = format_book_text(books)
    window[st_elem[status]].update(values=books, visible=True)


## ----- MAIN EVENT LOOP ----- ##
STARTUP = True
def main() -> None:
    while True:
        global STARTUP
        if STARTUP: # No fetch startup
            window['_READ-LIST_'].update(visible=True)
            STARTUP = False
        
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, 'Exit'): break
        if event == '_ADD_':
            add_book_form()
        if event in ('_READ_', '_PLAN_','_SUSPEND_', '_FINISHED_'):
            hide_all_lists() # only show the selected one
            print('Change view')
            if event == '_READ_':
                render('reading')
            elif event == '_PLAN_':
                render('plan-to-read')
            elif event == '_SUSPEND_':
                render('suspended')
            else:
                render('finished')

if __name__ == '__main__':
    pass