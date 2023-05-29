from tkinter import *
from tkinter import ttk
import platform
import os


class Main:
    def __init__(self):
        self.menu = Tk()
        self.menu.title("Practica 4")
        self.menu.resizable(False, False)
        self.frm = ttk.Frame(self.menu, padding=2)
        self.frm.grid()
        self.lbl0 = ttk.Label(self.frm, text="Modulo de Administración de Configuración")
        self.lbl0.grid(columnspan=2, row=0)
        self.eleccion =StringVar()
        self.opc1 = ttk.Radiobutton(self.frm, text="RCPlive-1", value="192.168.1.x", variable=self.eleccion, command=lambda: self.habilitar())
        self.opc1.grid(column=0, row=1)
        self.opc2 = ttk.Radiobutton(self.frm, text="RCPlive-3", value="30.30.30.x", variable=self.eleccion, command=lambda: self.habilitar())
        self.opc2.grid(column=1, row=1)
        self.btn1 = ttk.Button(self.frm, text="Ping", command=lambda: self.ping(), state=DISABLED)
        self.btn1.grid(columnspan=2, row=2)
        self.btn2 = ttk.Button(self.frm, text="Generar la Configuración", command=lambda: self.generar(), state=DISABLED)

        self.menu.mainloop()

    def habilitar(self):
        pass

    def ping(self):
        pass

    def generar(self):
        pass


Main()
if platform.system().lower() == "linux":
    t = os.system("ping -c 1 www.google.com")
    print(t)
