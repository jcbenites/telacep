import PySimpleGUI as sg
from CepBR import CepBr

#sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [
    [sg.Text('Digite o CEP:')],
    [sg.InputText(key='cep')],
    [sg.Button('Ok'), sg.Button('Cancel')],
    [sg.Text("", key='resultado')]
]

# Create the Window
window = sg.Window('Tela buscar informações CepBR', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    if event == "buscar cep":
        cep = values['cep']
        window['resultado'].update(f'O CEP pertence a: {resultado}')


window.close()