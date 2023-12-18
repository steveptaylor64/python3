#This is my first program usinng VSC

import PySimpleGUI as sg
#import PySimpleGUIQt as sg
#import PySimpleGUIWx as sg
#import PySimpleGUIWeb as sg


sg.set_options(font='Default 18', keep_on_top=True)



#Layout
layout=[
            [sg.Text('Hello World')],
            [sg.Button('OK')],
            [sg.Button('Press To Continue:')],
        ]

#Window
window=sg.Window('Title', layout)



#Event Loop / Handling
event, value= window.read(close=True)



#Close
window.close()

