import PySimpleGUI as sg

layout = [  [sg.Text('Button Test')],
            [sg.Button('Button 1', key='_1_')],
            [sg.Button('Button 2', key='_2_')],
            [sg.Button('Button 3', key='_3_')],  ]

window = sg.Window('My new window', layout,
                   return_keyboard_events=True)
while True:             # Event Loop
    event, values = window.Read()
    if event is None:
        break
    if event == '\r':
        elem = window.FindElementWithFocus()
        if elem is not None:
            elem.Click()
    elif event == '_1_':
        print('Button 1 clicked')
    elif event == '_2_':
        print('Button 2 clicked')
    elif event == '_3_':
        print('Button 3 clicked')