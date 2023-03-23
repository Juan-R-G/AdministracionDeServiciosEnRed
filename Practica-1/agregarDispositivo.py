from tkinter import *
from tkinter import ttk


class AddDev:
    def __init__(self):
        self.menu = Tk()
        self.menu.title("Agregar Dispositivo")
        self.menu.geometry("750x440")
        self.menu.resizable(False, False)
        self.frm = ttk.Frame(self.menu, padding=10)
        self.frm.grid()
        self.menu.mainloop()
