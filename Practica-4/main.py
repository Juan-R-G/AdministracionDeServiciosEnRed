from tkinter import *
from tkinter import ttk
import platform
import os


class Main:
    def __init__(self):
        self.menu = Tk()
        self.menu.title("Practica 4")
        self.menu.resizable(False, False)
        self.frm = ttk.Frame(self.menu, padding=3)
        self.frm.grid()
        self.lbl0 = ttk.Label(self.frm, text="Modulo de Administración de Configuración")
        self.lbl0.grid(columnspan=2, row=0)
        self.eleccion =StringVar()
        self.opc1 = ttk.Radiobutton(self.frm, text="RCPlive-1", value="192.168.1.1", variable=self.eleccion, command=lambda: self.habilitar())
        self.opc1.grid(column=0, row=1)
        self.opc2 = ttk.Radiobutton(self.frm, text="RCPlive-3", value="30.30.30.1", variable=self.eleccion, command=lambda: self.habilitar())
        self.opc2.grid(column=1, row=1)
        self.btn1 = ttk.Button(self.frm, text="Ping", command=lambda: self.ping(), state=DISABLED)
        self.btn1.grid(columnspan=2, row=2)
        self.btn2 = ttk.Button(self.frm, text="Generar la Configuracion", command=lambda: self.generar(), state=DISABLED)
        self.btn2.grid(columnspan=2, row=3)
        self.btn3 = ttk.Button(self.frm, text="Extraer la Configuracion", command=lambda: self.extraer(), state=DISABLED)
        self.btn3.grid(columnspan=2, row=4)
        self.btn4 = ttk.Button(self.frm, text="Importar la Configuracion", command=lambda: self.importar(), state=DISABLED)
        self.btn4.grid(columnspan=2, row=5)
        self.menu.mainloop()

    def habilitar(self):
        self.btn1.state(["!disabled"])
        self.btn2.state(["!disabled"])
        self.btn3.state(["!disabled"])
        self.btn4.state(["!disabled"])

    def ping(self):
        pingw = Toplevel()
        pingw.title("Ping")
        pingw.resizable(False, False)
        label1 = ttk.Label(pingw, text="Comprobando el estado de la red " + self.eleccion.get())
        label1.grid(column=0, row=0)
        comando = ""
        if platform.system().lower() == "windows":
            comando = "ping -n 1 -w 3 " + self.eleccion.get()
        else:
            comando = "ping -c 1 -w 3 www.google.com"
        labels = []
        r = 1

        for i in range(0, 5):
            labels.append(ttk.Label(pingw, text="Realizando el ping " + str(i+1) + "..."))
            labels[r-1].grid(column=0, row=r)
            self.menu.update()
            r += 1
            t = os.system(comando)
            if t:
                labels.append(ttk.Label(pingw, text="Ping Fallido.", foreground="red"))
            else:
                labels.append(ttk.Label(pingw, text="Ping Exitoso!", foreground="green"))
            labels[r - 1].grid(column=0, row=r)
            r += 1

    def generar(self):
        generarw = Toplevel()
        generarw.title("Generar la Configuracion")
        generarw.resizable(False, False)

    def extraer(self):
        pass

    def importar(self):
        pass


Main()
