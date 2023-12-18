import os
import time
import sys
import math
import numpy as np
import PySimpleGUI as sg


print ("Machine Learning Lab1")
time.sleep(1)
os.system('clear')

one_d_arr = np.array([10,12])
print(one_d_arr)

m1=np.array([1,2,3,4,5])
print(m1)

m2=np.arange(10)
print(m2)

m3=np.arange(5,10,5)
print(m3)

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Some text on Row 1')],
            [sg.Text('Enter something on Row 2'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()

