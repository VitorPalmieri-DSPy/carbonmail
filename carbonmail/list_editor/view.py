# É onde fica o código para a Interfacwe Gráfica;
# Tudo que existir de VISUAL vai ficar aqui;
# É principalmente aqui que usaremos o PySimpleGUI.

import PySimpleGUI as sg

def get_layout():
    return [
        [sg.Text("Olá")],
    ]

def get_window():
    return sg.Window("Editor de Lista", get_layout())