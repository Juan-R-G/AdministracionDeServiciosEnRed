from tkinter import *
from tkinter import ttk
import os


class ChInfo:
    def __init__(self):
        self.menu = Tk()
        self.menu.title("Cambiar Informacion")
        # self.menu.geometry("750x440")
        self.menu.resizable(False, False)
        self.frm = ttk.Frame(self.menu, padding=10)
        self.frm.grid()
        self.lbl0 = ttk.Label()
        self.flag = False
        self.devices = []
        if os.path.exists(os.path.join(os.getcwd(), "Dispositivos")):
            for root, dirs, files in os.walk(os.path.join(os.getcwd(), "Dispositivos")):
                for name in files:
                    self.devices.append(name.replace(".txt", ""))
            if len(self.devices) > 0:
                self.flag = True
        if self.flag:
            self.lbl0 = ttk.Label(self.frm, text="Seleccione un Dispositivo")
        else:
            self.lbl0 = ttk.Label(self.frm, text="No hay dispositivos guardados...")
        self.lbl0.grid(columnspan=2, row=0)
        self.eleccion = StringVar()
        self.radioButtons = []
        self.c = 0
        if self.flag:
            for name in self.devices:
                self.radioButtons.append(ttk.Radiobutton(self.frm, text=name, value=name, variable=self.eleccion, command=lambda: self.enable()))
                self.c += 1
                self.radioButtons[self.c-1].grid(columnspan=2, row=self.c)
        self.lbl1 = ttk.Label()
        self.ent1 = ttk.Entry()
        self.lbl2 = ttk.Label()
        self.ent2 = ttk.Entry()
        self.lbl3 = ttk.Label()
        self.ent3 = ttk.Entry()
        self.lbl4 = ttk.Label()
        self.ent4 = ttk.Entry
        self.btn1 = ttk.Button()
        if self.flag:
            self.btn1 = ttk.Button(self.frm, text="Guardar", state=DISABLED)
            self.btn1.grid(columnspan=2, row=self.c+5)
        else:
            self.btn1 = ttk.Button(self.frm, text="Continuar")
            self.btn1.grid(column=0, row=1)
        self.menu.mainloop()

    def enable(self):
        self.btn1.state(["!disabled"])
        file = open(os.path.join(os.getcwd(), "Dispositivos", self.eleccion.get() + ".txt"), "r")
        t = file.readline()
        file.close()
        t = t.split("-")
        x = t[0].split(":")
        self.c += 1
        self.lbl1 = ttk.Label(self.frm, text="IP/Hostname:")
        self.lbl1.grid(column=0, row=self.c)
        self.ent1 = ttk.Entry(self.frm, width=30)
        self.ent1.insert(0, x[1])
        self.ent1.grid(column=1, row=self.c)
        x = t[1].split(":")
        self.c += 1
        self.lbl2 = ttk.Label(self.frm, text="Version SNMP:")
        self.lbl2.grid(column=0, row=self.c)
        self.ent2 = ttk.Entry(self.frm, width=30)
        self.ent2.insert(0, x[1])
        self.ent2.grid(column=1, row=self.c)
        x = t[2].split(":")
        self.c += 1
        self.lbl3 = ttk.Label(self.frm, text="Comunidad:")
        self.lbl3.grid(column=0, row=self.c)
        self.ent3 = ttk.Entry(self.frm, width=30)
        self.ent3.insert(0, x[1])
        self.ent3.grid(column=1, row=self.c)
        x = t[3].split(":")
        self.c += 1
        self.lbl4 = ttk.Label(self.frm, text="Puerto:")
        self.lbl4.grid(column=0, row=self.c)
        self.ent4 = ttk.Entry(self.frm, width=30)
        self.ent4.insert(0, x[1])
        self.ent4.grid(column=1, row=self.c)


ChInfo()
