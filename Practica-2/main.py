# Roldan-Gomez-Juan
from tkinter import *
from tkinter import ttk
from agregarDispositivo import AddDev
from cambiarInformacion import ChInfo
from eliminarDispositivo import DelDev
from generarReporte import Report


class Main:
    def __init__(self):
        self.menu = Tk()
        self.menu.title("Inicio")
        self.menu.resizable(False, False)
        self.frm = ttk.Frame(self.menu, padding=10)
        self.frm.grid()
        self.info = "Sistema de Administracion de Contabilidad\n\nPractica 2 - Modulo de Administracion de Contabilidad\n\nJuan Roldan Gomez\t\t4CM14\t\t2020630462"
        self.lbl1 = ttk.Label(self.frm, text=self.info, justify=CENTER, padding=6)  # width: anchor:CENTER
        self.lbl1.grid(column=0, row=0)
        self.lbl2 = ttk.Label(self.frm, text="Escoja una opcion:", padding=10)
        self.lbl2.grid(column=0, row=1)
        self.eleccion = IntVar()
        self.opc1 = ttk.Radiobutton(self.frm, text="Agregar Dispositivo", value=1, variable=self.eleccion, command=lambda: self.btn1.state(["!disabled"]))
        self.opc1.grid(column=0, row=2)
        self.opc2 = ttk.Radiobutton(self.frm, text="Cambiar Informacion del Dispositivo", value=2, variable=self.eleccion, command=lambda: self.btn1.state(["!disabled"]))
        self.opc2.grid(column=0, row=3)
        self.opc3 = ttk.Radiobutton(self.frm, text="Eliminar Dispositivo", value=3, variable=self.eleccion, command=lambda: self.btn1.state(["!disabled"]))
        self.opc3.grid(column=0, row=4)
        self.opc4 = ttk.Radiobutton(self.frm, text="Generar Reporte", value=4, variable=self.eleccion, command=lambda: self.btn1.state(["!disabled"]))
        self.opc4.grid(column=0, row=5)
        self.btn1 = ttk.Button(self.frm, text="Seleccionar", command=lambda: self.seleccion(), state=DISABLED)
        self.btn1.grid(column=0, row=6)
        self.menu.mainloop()

    def seleccion(self):
        if self.eleccion.get() == 1:
            self.menu.destroy()
            AddDev()
            Main()
        elif self.eleccion.get() == 2:
            self.menu.destroy()
            ChInfo()
            Main()
        elif self.eleccion.get() == 3:
            self.menu.destroy()
            DelDev()
            Main()
        else:
            self.menu.destroy()
            Report()
            Main()


Main()
