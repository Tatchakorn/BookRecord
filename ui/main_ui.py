import PySimpleGUI as sg


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

## ----- MAIN EVENT LOOP --- ##
def main() -> None:
    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, 'Quit'): break
        
        if event == '_ADD_':
            # layout.append([sg.T('Nice')])
            print('Add book')
        
        if event in ('_READ_', '_PLAN_','_SUSPEND_', '_FINISHED_'):
            print('Change view')
            if event == '_READ_':
                print('render read')
            elif event == '_PLAN_':
                print('render plan')
            elif event == '_SUSPEND_':
                print('render suspend')
            else:
                print('render finished')

if __name__ == '__main__':
    pass