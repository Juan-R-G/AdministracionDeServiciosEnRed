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
        else:
            self.lbl1 = ttk.Label(self.frm, text="No hay dispositivos guardados...")
        self.lbl1.grid(columnspan=3, row=0)
        self.eleccion = StringVar()
        self.radioButtons = []
        self.c = 0
        if self.flag:
            for name in self.devices:
                self.radioButtons.append(ttk.Radiobutton(self.frm, text=name, value=name, variable=self.eleccion, command=lambda: self.dispositivo()))
                self.c += 1
                self.radioButtons[self.c-1].grid(columnspan=3, row=self.c)
        self.lbl2 = ttk.Label()
        self.tipoReporte = IntVar()
        self.radioButtons1 = []
        self.radioButtons1.append(ttk.Radiobutton(self.frm, text="Reporte General", value=1, variable=self.tipoReporte, command=lambda: self.tipo1()))
        self.radioButtons1.append(ttk.Radiobutton(self.frm, text="Reporte de Contabilidad", value=2, variable=self.tipoReporte, command=lambda: self.tipo2()))
        self.btn1 = ttk.Button()
        if self.flag:
            self.btn1 = ttk.Button(self.frm, text="Generar", command=lambda: self.generar(), state=DISABLED)
            self.btn1.grid(columnspan=3, row=self.c+10)
        else:
            self.btn1 = ttk.Button(self.frm, text="Continuar", command=lambda: self.menu.destroy())
            self.btn1.grid(columnspan=3, row=1)
        self.menu.mainloop()

    def dispositivo(self):
        self.lbl2 = ttk.Label(self.frm, text="Seleccione el reporte a generar:")
        self.c = len(self.devices) + 1
        self.lbl2.grid(columnspan=3, row=self.c)
        self.c += 1
        self.radioButtons1[0].grid(columnspan=3, row=self.c)
        self.c += 1
        self.radioButtons1[1].grid(columnspan=3, row=self.c)

    def tipo1(self):
        pass

    def tipo2(self):
        pass

    def generar(self):
        pass
