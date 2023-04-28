from tkinter import *
from tkinter import ttk


class Main:
    def __init__(self):
        self.menu = Tk()
        self.menu.title("Inicio")
        self.menu.resizable(False, False)
        self.frm = ttk.Frame(self.menu, padding=10)
        self.frm.grid()
        self.info = "Sistema de monitorización de rendimiento\n\nPractica 3 - Monitorizar el rendimiento de un agente\n\nJuan Roldan Gomez\t\t4CM14\t\t2020630462"
        self.lbl1 = ttk.Label(self.frm, text=self.info)
        self.lbl1.grid(column=0, row=0)
        self.lbl2 = ttk.Label(self.frm, text="Escoja una opcion")
        self.menu.mainloop()


Main()
