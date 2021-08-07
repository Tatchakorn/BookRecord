from typing import Any, List, Tuple
import PySimpleGUI as sg

from db_handler.read_write_db import (
    get_books_from_status,
    get_book_from_title,
    delete_book,
)
from .popups import (
    add_update_book_form, 
    popup_confirm, 
    popup_no_select,
)

"""
TODO
- Search bar
- popup -> show book info
- optimize render -> Stop hiding all elements!!
"""
## ----- CONFIGS ----- ##
# sg.change_look_and_feel('Dark')
sg.theme('Dark2')
WIN_WIDTH = 60
WIN_HEIGHT = 100
BTN_FONT_SIZE = 16
LIST_BOX_W = WIN_WIDTH + 20
LIST_BOX_H = 10

bt = {'size': (WIN_WIDTH//4,2), 'font': ('Franklin Gothic Book', BTN_FONT_SIZE), 
    'button_color': ('white', 'green'), 'pad': (0,0)}

listbox_default_conf = {'values': [], 'enable_events': True, 
    'size': (LIST_BOX_W, LIST_BOX_H), 'visible': False}
## ----- WINDOW AND LAYOUT ----- ##

layout = [
    # App title
    [sg.Text('Tar\'s Book record', size=(WIN_WIDTH,1))],
    [
        sg.Button('Reading', **bt, key='_READ_'), 
        sg.Button('Suspended', **bt, key='_SUSPEND_'), 
        sg.Button('Plan to read', **bt, key='_PLAN_'), 
        sg.Button('Finished', **bt, key='_FINISHED_'),],
    [sg.HSeparator()],
    [
        sg.Input(do_not_clear=True, size=(20,1),enable_events=True, key='_SEARCH-INPUT_'),
        sg.Button('Add Book', key='_ADD_', button_color=('white', 'green'),),
        sg.Button('Update', key='_UPDATE_', button_color=('white', '#a34c00')),
        sg.Button('Delete', key='_DELETE_', button_color=('white', 'red')),
    ],
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
    return_keyboard_events=True,
    )

## ----- HELPER FUNCTIONS ----- ##

def format_book_text(books: List[Tuple[Any]]) -> List[str]:
    return [
        f'{book[1]}' 
        for book in books
    ]


def hide_all_lists() -> None:
    """Too lazy to implement this properly"""
    window['_READ-LIST_'].update(visible=False)
    window['_SUSPEND-LIST_'].update(visible=False)
    window['_PLAN-LIST_'].update(visible=False)
    window['_FINISH-LIST_'].update(visible=False)

## ----- RENDER LIST ----- ##
stbtn_to_list = { # Maping from (status, button_select_view) -> LIST
    'reading': '_READ-LIST_',
    'suspended': '_SUSPEND-LIST_',
    'plan-to-read': '_PLAN-LIST_',
    'finished': '_FINISH-LIST_',
    '_READ_': '_READ-LIST_',
    '_SUSPEND_': '_SUSPEND-LIST_',
    '_PLAN_': '_PLAN-LIST_',
    '_FINISHED_': '_FINISH-LIST_',
}

btn_to_st = {  # Maping from button -> status
    '_READ_': 'reading',
    '_SUSPEND_': 'suspended',
    '_PLAN_': 'plan-to-read',
    '_FINISHED_': 'finished',
    
}


def render(status: str) -> None:
    hide_all_lists() # only show the selected one
    books = get_books_from_status(status)
    books = format_book_text(books)
    window[stbtn_to_list[status]].update(values=books, visible=True)


## ----- MAIN EVENT LOOP ----- ##
STARTUP = True
def main() -> None:
    while True:
        global STARTUP
        
        if STARTUP: # No fetch startup
            window['_READ-LIST_'].update(visible=True)
            selecting_view = '_READ_'
            STARTUP = False
        
        event, values = window.read()

        print(event)
        print(values)
        
        if event == '\r': # Hit Enter key
            elem = window.FindElementWithFocus()
            if elem is not None:
                try:
                    elem.Click()
                except:
                    print('Cannot click the element')
        
        if event in (sg.WINDOW_CLOSED, 'Exit'): break
        
        if values['_SEARCH-INPUT_'] != '':
            print('Search for something')
            # search = values['_SEARCH-INPUT']
            # new_values = [x for x in names if search in x]  # do the filtering
            # window.Element('_LIST_').Update(new_values)     # display in the listbox
            # render('search')
        
        if event in ('_ADD_', '_DELETE_', '_UPDATE_'):
            if event == '_ADD_':
                print(add_update_book_form())
            elif event == '_UPDATE_':
                selected_book_title = values[stbtn_to_list[selecting_view]]
                if not selected_book_title:                 # Empty list
                    popup_no_select('update')
                else:
                    b_info = get_book_from_title(selected_book_title[0])
                    add_update_book_form(b_info[1], b_info[2], b_info[3], update=True, id=b_info[0])
                    render(btn_to_st[selecting_view])       # Update view
            elif event == '_DELETE_':
                selected_book_title = values[stbtn_to_list[selecting_view]]
                if not selected_book_title:                 # Empty list
                    popup_no_select('delete')
                else:
                    print(f'Deleting {selected_book_title[0]}')
                    if popup_confirm('delete'):
                        b_info = get_book_from_title(selected_book_title[0])
                        print(b_info)
                        delete_book(b_info[0])
                        render(btn_to_st[selecting_view])   # Update view
        if event in ('_READ_', '_PLAN_','_SUSPEND_', '_FINISHED_'):
            if event == '_READ_':
                selecting_view = event
                render('reading')
            elif event == '_PLAN_':
                selecting_view = event
                render('plan-to-read')
            elif event == '_SUSPEND_':
                selecting_view = event
                render('suspended')
            else:
                selecting_view = event
                render('finished')

if __name__ == '__main__':
    pass