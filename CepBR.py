import requests
import PySimpleGUI as sg

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

#cep = int(input())

objeto_cep = CepBr(cep)
objeto_cep_api = objeto_cep.api_via_cep()

print(objeto_cep_api)


class CepBr:

    def __init__(self, cep):
        cep = str(cep)
        if self.valida_cep(cep):
            self.cep = cep
        else:
            raise ValueError("CEP inválido!")

    def __str__(self):
        return self.format_cep()

    def valida_cep(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def format_cep(self):
        return '{}-{}'.format(self.cep[:5], self.cep[5:])

    def api_via_cep(self):
        url = f"https://viacep.com.br/ws/{self.cep}/json/"
        r = requests.get(url)
        dados_cep = r.json()
        return (
            dados_cep['cep'],
            dados_cep['logradouro'],
            dados_cep['bairro'],
            dados_cep['localidade'],
            dados_cep['uf']
        )


