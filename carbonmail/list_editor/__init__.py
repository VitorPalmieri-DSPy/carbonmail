# Arquivo usado para transformar a Pasta em Pacote;
# Ele é sempre executado ao importar este pacote.

from carbonmail.list_editor import view
import PySimpleGUI as sg
from PySimpleGUI import WIN_CLOSED

class List_Editor:
    def __init__(self, email_sender):
        self.window = None
        self.ems = email_sender

    def instantiate(self):
        if self.window == None:
            self.window = view.get_window()

    def enable_window(self):
        self.instantiate()

        while True:
            event, values = self.window.read()

            if event in (WIN_CLOSED, "-Back-"):
                self.window.close()
                self.ems.unhide_window()
                break

            if event == "-Send-":
                title = values["-Title-"]
                content = values["-Content(Body)-"]

                sg.Popup(
                    f"O Título é: {title}\nO Conteúdo é: {content}",
                    title="E-mail",
                )
    
    def close_window(self):
        if self.window is not None:
            self.window.Close()
        self.window = None

    def hide_window(self):
        if self.window is not None:
            self.window.Hide()
    
    def unhide_window(self):
        if self.window is not None:
            self.window.UnHide()