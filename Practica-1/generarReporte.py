from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os


class Report:
    def __init__(self):
        self.menu = Tk()
        self.menu.title("Generar Reporte")
        # self.menu.geometry("750x440")
        self.menu.resizable(False, False)
        self.frm = ttk.Frame(self.menu, padding=10)
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
        self.lbl1.grid(column=0, row=0)
        self.eleccion = StringVar()
        self.radioButtons = []
        self.c = 0
        if self.flag:
            for name in self.devices:
                self.radioButtons.append(ttk.Radiobutton(self.frm, text=name, value=name, variable=self.eleccion, command=lambda: self.btn1.state(["!disabled"])))
                self.c += 1
                self.radioButtons[self.c-1].grid(column=0, row=self.c)
        self.btn1 = ttk.Button()
        if self.flag:
            self.btn1 = ttk.Button(self.frm, text="Generar", command=lambda: self.generar(), state=DISABLED)
            self.btn1.grid(column=0, row=self.c+1)
        else:
            self.btn1 = ttk.Button(self.frm, text="Continuar", command=lambda: self.menu.destroy())
            self.btn1.grid(column=0, row=1)
        self.menu.mainloop()

    def generar(self):
        file = open(os.path.join(os.getcwd(), "Dispositivos", self.eleccion.get() + ".txt"), "r")
        content = [f.replace("\n", "") for f in file]
        file.close()
        title = "Administración de Servicios en Red\nPráctica 1\nJuan Roldán Gómez\t\t4CM14"
        info = []
        t = content[0].split("-")
        x = t[0].split(":")
        info.append("IP: " + x[1])
        x = t[2].split(":")
        info.append("Comunidad: " + x[1])
        t = content[1].split("_")
        for v in t:
            x = v.split(":")
            info.append(x[0] + ": " + x[1])
        t = content[2].split(":")
        info.append(t[0] + ": " + t[1])
        t = content[3].split(":")
        info.append(t[0] + ": " + t[1])
        t = content[4].split(":")
        info.append(t[0] + ": " + t[1])
        t = content[5].split(":")
        info.append("\n" + t[0] + "(" + t[1] + "):")
        image = ""
        if "Windows" in content[1]:
            image = os.path.join(os.getcwd(), "Images", "windows.png")
        else:
            image = os.path.join(os.getcwd(), "Images", "linux.png")
        table = [["Interfaz", "Estado Administrativo"]]
        t = content[6].split("-")
        for v in t:
            if '¡' in v:
                continue
            x = v.split(":")
            if int(x[1]) == 1:
                table.append([x[0], "Up"])
            elif int(x[1]) == 2:
                table.append([x[0], "Down"])
            else:
                table.append([x[0], "Testing"])
