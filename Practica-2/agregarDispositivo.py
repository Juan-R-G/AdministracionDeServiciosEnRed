from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
from snmp import consulta


class AddDev:
    def __init__(self):
        self.menu = Tk()
        self.menu.title("Agregar Dispositivo")
        self.menu.resizable(False, False)
        self.frm = ttk.Frame(self.menu, padding=15)
        self.frm.grid()
        self.lbl0 = ttk.Label(self.frm, text="Ingrese los Siguientes Datos:")
        self.lbl0.grid(columnspan=2, row=0)
        self.lbl1 = ttk.Label(self.frm, text="IP/Hostname:")
        self.lbl1.grid(column=0, row=1)
        self.ent1 = ttk.Entry(self.frm, width=25)
        self.ent1.insert(0, "localhost")
        self.ent1.grid(column=1, row=1)
        self.lbl2 = ttk.Label(self.frm, text="Version SNMP:")
        self.lbl2.grid(column=0, row=2)
        self.ent2 = ttk.Entry(self.frm, width=25)
        self.ent2.insert(0, "1")
        self.ent2.grid(column=1, row=2)
        self.lbl3 = ttk.Label(self.frm, text="Comunidad:")
        self.lbl3.grid(column=0, row=3)
        self.ent3 = ttk.Entry(self.frm, width=25)
        self.ent3.insert(0, "")
        self.ent3.grid(column=1, row=3)
        self.lbl1 = ttk.Label(self.frm, text="IP/Hostname:")
        self.lbl1.grid(column=0, row=1)
        self.ent1 = ttk.Entry(self.frm, width=25)
        self.ent1.insert(0, "localhost")
        self.ent1.grid(column=1, row=1)
        self.menu.mainloop()
