from tkinter import *
from tkinter import ttk


def seleccion(sel):
    if sel == 1:
        print("A")
    elif sel == 2:
        print("C")
    elif sel == 3:
        print("E")
    else:
        print("R")


mmenu = Tk()
mmenu.title("Inicio")
mmenu.geometry("700x450")
mmenu.resizable(False, False)
frm = ttk.Frame(mmenu, padding=10)
frm.grid()
info = "Sistema de Administracion de Red\nPractica 1 - Adquisicion de Informacion\nJuan Roldan Gomez 4CM14 2020630462"
ttk.Label(frm, text=info).grid(column=0, row=0)
ttk.Label(frm, text="Escoja una opcion:").grid(column=0, row=1)
eleccion = IntVar()
ttk.Radiobutton(frm, text="Agregar Dispositivo", value=1, variable=eleccion).grid(column=0, row=2)
ttk.Radiobutton(frm, text="Cambiar Informacion del Dispositivo", value=2, variable=eleccion).grid(column=0, row=3)
ttk.Radiobutton(frm, text="Eliminar Dispositivo", value=3, variable=eleccion).grid(column=0, row=4)
ttk.Radiobutton(frm, text="Generar Reporte", value=4, variable=eleccion).grid(column=0, row=5)
ttk.Button(frm, text="Continuar", command=lambda: seleccion(eleccion.get())).grid(column=0, row=6)

mmenu.mainloop()

