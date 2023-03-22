from tkinter import *
from tkinter import ttk


class Main:
    def __init__(self):
        self.menu = Tk()
        self.menu.title("Inicio")
        self.menu.geometry("750x440")
        self.menu.resizable(False, False)
        self.frm = ttk.Frame(self.menu, padding=10)
        self.frm.grid()
        self.info = "Sistema de Administracion de Red\nPractica 1 - Adquisicion de Informacion\nJuan Roldan Gomez\t\t4CM14\t\t2020630462"
        self.lbl1 = ttk.Label(self.frm, text=self.info)
        self.lbl1.grid(column=0, row=0)
        self.lbl2 = ttk.Label(self.frm, text="Escoja una opción:")
        self.lbl2.grid(column=0, row=1)
        self.eleccion = IntVar()
        self.opc1 = ttk.Radiobutton(self.frm, text="Agregar Dispositivo", value=1, variable=self.eleccion)
        self.opc1.grid(column=0, row=2)
        self.opc2 = ttk.Radiobutton(self.frm, text="Cambiar Informacion del Dispositivo", value=2, variable=self.eleccion)
        self.opc2.grid(column=0, row=3)
        self.opc3 = ttk.Radiobutton(self.frm, text="Eliminar Dispositivo", value=3, variable=self.eleccion)
        self.opc3.grid(column=0, row=4)
        self.opc4 = ttk.Radiobutton(self.frm, text="Generar Reporte", value=4, variable=self.eleccion)
        self.opc4.grid(column=0, row=5)
        self.menu.mainloop()


main = Main()
"""
def seleccion(sel):
    if sel == 1:
        print("A")
    elif sel == 2:
        print("C")
    elif sel == 3:
        print("E")
    else:
        print("R")

    mmenu.destroy()
    adev.mainloop()
elecButton(frm, text="Continuar", command=lambda: seleccion(eleccion.get())).grid(column=0, row=6)

# Agregar Dispositivo
adev = Tk()
adev.title("Agregar Dispositivo")
adev.geometry("700x450")
adev.resizable(False, False)
frm1 = ttk.Frame(adev, padding=10)


# Default
mmenu.mainloop()"""

