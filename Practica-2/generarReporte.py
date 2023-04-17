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
        self.lbl1.grid(column=0, row=0)
        self.menu.mainloop()
