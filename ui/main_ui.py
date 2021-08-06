import PySimpleGUI as sg

from db_handler.read_write_db import get_books_from_status
from .form import add_book_form

## ----- CONFIGS ----- ##
sg.change_look_and_feel('Dark')
WIN_WIDTH = 40

## ----- WINDOW AND LAYOUT ----- ##
# --- BUTTONS STYLE
bt = {'size': (10,2), 'font': ('Franklin Gothic Book', 16), 
    'button_color': ('black', 'green'), 'pad': (0,0)}

layout = [
    # App title
    [sg.T('Book Record', size=(WIN_WIDTH,1)), sg.Button('Add Book', key='_ADD_')],
    [sg.Button('Reading', **bt, key='_READ_'),sg.Button('Suspended', **bt, key='_SUSPEND_'), 
        sg.Button('Plan to read', **bt, key='_PLAN_'), sg.Button('Finished', **bt, key='_FINISHED_'),],
]

window = sg.Window(
    'Book Record', 
    layout=layout, 
    margins=(0,0),
    finalize=True,
    )

## ----- FUNCTIONS ----- ##

def render_reading() -> None:
    books = get_books_from_status('reading')
    print(books)


def render_suspended() -> None:
    books = get_books_from_status('suspended')
    print(books)


def render_plan_to_read() -> None:
    books = get_books_from_status('plan-to-read')
    print(books)


def render_finished() -> None:
    books = get_books_from_status('finished')
    print(books)


## ----- MAIN EVENT LOOP ----- ##
def main() -> None:
    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, 'Exit'): break
        
        if event == '_ADD_':
            print('Add book')
            add_book_form()
            # layout.append([sg.T('Book')])
        
        if event in ('_READ_', '_PLAN_','_SUSPEND_', '_FINISHED_'):
            print('Change view')
            if event == '_READ_':
                render_reading()
            elif event == '_PLAN_':
                render_plan_to_read()
            elif event == '_SUSPEND_':
                render_suspended()
            else:
                render_finished()

if __name__ == '__main__':
    pass