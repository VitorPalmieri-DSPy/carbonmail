# É onde fica o código para a Interfacwe Gráfica;
# Tudo que existir de VISUAL vai ficar aqui;
# É principalmente aqui que usaremos o PySimpleGUI.

import PySimpleGUI as sg
from carbonmail.utils import inner_element_space

# Window => Janela
# Layout => O que vai ser mostrado na janela
#        ===> Lista de Listas
#             Cada sublista é uma "Linha" da Janela
#             Cada elemento é um componente visual

lista = ["Administradores", "Alunos"]

def get_layout():

    frame_campaign = [
        inner_element_space(600),
        [
            sg.Text("Selecione o Código"),
            sg.In(key="-Code-", size=(30, 1)),
            sg.FileBrowse(
                "Selecionar",
                file_types=(("Códigos Python", "*.py"),),
                size=(15, 1),
            )
        ],
        [
            sg.Text("Selecione a Lista de Destinatários"),
            sg.Combo(
                lista,
                lista[1],
                key="-Lists-",
            )
        ],
        inner_element_space(600),
    ]

    frame_email = [
        inner_element_space(600),
        [
            sg.Text("Insira o título",
            font=("Helvetica 15"),
            ),
            sg.In(
                key="-Title-",
                size=(62, 1),
            )
        ],
        [
            sg.Text(
                "Insira o Conteúdo",
                font=("Helvetica 15"),    
            ),
            sg.MLine(
                key="-Content-",
                size=(60, 10),
            )
        ],
        inner_element_space(600),
    ]

    layout = [
        [
            sg.Frame(
                "Configurações de Campanha",
                frame_campaign,
                element_justification="c",
            )
        ],
        [
            sg.Frame(
                "Configurações do E-mail",
                frame_email,
                element_justification="c",
            )
        ],
        [
            sg.Button(
                "Enviar E-mail",
                key="-Send-",
                size=(15, 1),
                pad=(10, (10, 0)),
            ),
            sg.Button(
                "Gerenciar Listas",
                key="-ListEditor-",
                size=(15, 1),
                pad=(10, (10, 0)),
            )
        ],
        inner_element_space(600),
    ]

    return layout


def get_window():
    sg.theme("DarkBlue14")

    return sg.Window(
        "Enviador de E-mail", 
        get_layout(),
        element_justification="c"
        )
