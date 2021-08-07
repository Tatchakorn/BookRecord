from typing import Any, List, Tuple
import PySimpleGUI as sg

from db_handler.read_write_db import (
    get_all_books,
    get_books_from_status,
    get_book_from_title,
    delete_book,
)


from ui.popups import (
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
    'size': (LIST_BOX_W, LIST_BOX_H), 'visible': True}
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
    [sg.Listbox(**listbox_default_conf, key='_BOOK-LIST_'),],
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
        f'{book[1]} [{book[4]}]' 
        for book in books
    ]

def extract_book_title(text: str) -> str:
    """Extract title from format_book_text maipulation"""
    return text.split('[')[0][:-1]

## ----- RENDER LIST ----- ##
btn_to_st = {  # Maping from button -> status
        '_READ_': 'reading',
        '_SUSPEND_': 'suspended',
        '_PLAN_': 'plan-to-read',
        '_FINISHED_': 'finished',
    }

def render(status: str, key: str = '') -> None:
    if status == 'search':
        books = format_book_text(get_all_books())
        s_books = [book for book in books if key in book.lower()]  # do the filtering (case insensitive)
        window['_BOOK-LIST_'].update(values=s_books) # display in the listbox
    else:
        books = get_books_from_status(status)
        books = format_book_text(books)
        window['_BOOK-LIST_'].update(values=books)


## ----- MAIN EVENT LOOP ----- ##

key_search = ''
selecting_view = ''
def main() -> None:
    while True:
        global key_search, selecting_view
        
        event, values = window.read()

        print(event)
        print(values)
        
        if event in (sg.WINDOW_CLOSED, 'Exit'): break
        
        if values['_SEARCH-INPUT_'] != '' and event != '_BOOK-LIST_':
            selecting_view = 'search'
            key_search = values['_SEARCH-INPUT_'].lower()
            render('search', key_search)
        
        if event in ('_ADD_', '_DELETE_', '_UPDATE_'):
            if event == '_ADD_':
                add_update_book_form()
                render(btn_to_st.get(selecting_view, 'search'), key_search)       # Update view
            elif event == '_UPDATE_':
                selected_book_title = values['_BOOK-LIST_']
                if not selected_book_title:                 # Empty list
                    popup_no_select('update')
                else:
                    book_title = extract_book_title(selected_book_title[0])
                    b_info = get_book_from_title(book_title)
                    add_update_book_form(b_info[1], b_info[2], b_info[3], update=True, id=b_info[0])
                    render(btn_to_st.get(selecting_view, 'search'), key_search)       # Update view
            elif event == '_DELETE_':
                selected_book_title = values['_BOOK-LIST_']
                print(selected_book_title)
                if not selected_book_title:                 # Empty list
                    popup_no_select('delete')
                else:
                    if popup_confirm('delete'):
                        book_title = extract_book_title(selected_book_title[0])
                        b_info = get_book_from_title(book_title)
                        print(b_info)
                        delete_book(b_info[0])
                        render(btn_to_st.get(selecting_view, 'search'), key_search)       # Update view
        
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