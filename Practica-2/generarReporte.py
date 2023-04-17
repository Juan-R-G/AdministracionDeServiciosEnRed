from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
from report_lab import *


class Report:
    def __init__(self):
        self.menu = Tk()
        self.menu.title("Generar Reporte")
        self.menu.resizable(False, False)
        self.frm = ttk.Frame(self.menu, padding=15)
        self.frm.grid()
        self.lbl1 = ttk.Label()
        self.flag = False
        self.devices = []
        if os.path.exists(os.path.join(os.getcwd(), "Dispositivos")):
            for root, dirs, files in os.walk(os.path.join(os.getcwd(), "Dispositivos")):
                for name in files:
                    self.devices.append(name.replace(".txt", ""))
            if len(self.devices) > 0:
                self.flag = True
        if self.flag:
            self.lbl1 = ttk.Label(self.frm, text="Seleccione un Dispositivo:")
        self.lbl1.grid(columnspan=3, row=0)
        self.eleccion = StringVar()
        self.radioButtons = []
        self.c = 0
        if self.flag:
            for name in self.devices:
                self.radioButtons.append(ttk.Radiobutton(self.frm, text=name, value=name, variable=self.eleccion, command=lambda: self.dispositivo()))
                self.c += 1
                self.radioButtons[self.c-1].grid(columnspan=3, row=self.c)
        # Seleccionar Reporte
        self.btn1 = ttk.Button()
        if self.flag:
            self.btn1 = ttk.Button(self.frm, text="Generar", command=lambda: self.generar(), state=DISABLED)
        else:
            self.btn1 = ttk.Button(self.frm, text="Continuar", command=lambda: self.menu.destroy())
        self.btn1.grid(columnspan=3, row=self.c+1)
        self.menu.mainloop()

    def dispositivo(self):
        pass

    def generar(self):
        pass
