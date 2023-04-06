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
        self.ent3.insert(0, "JuanRGomez")
        self.ent3.grid(column=1, row=3)
        self.lbl4 = ttk.Label(self.frm, text="Puerto:")
        self.lbl4.grid(column=0, row=4)
        self.ent4 = ttk.Entry(self.frm, width=25)
        self.ent4.insert(0, "161")
        self.ent4.grid(column=1, row=4)
        self.btn1 = ttk.Button(self.frm, text="Agregar", command=lambda: self.agregar())
        self.btn1.grid(columnspan=2, row=5)
        self.lbl5 = ttk.Label()
        self.menu.mainloop()

    def agregar(self):
        ip = self.ent1.get()
        ver = self.ent2.get()
        comm = self.ent3.get()
        port = self.ent4.get()

        if ip == "" or ver == "" or comm == "" or port == "":
            self.lbl5 = ttk.Label(self.frm, text="Llene todos los campos!", foreground="red")
            self.lbl5.grid(columnspan=2, row=6)
        else:
            self.lbl5.destroy()
            if not os.path.exists(os.path.join(os.getcwd(), "Dispositivos")):
                os.mkdir(os.path.join(os.getcwd(), "Dispositivos"))
            file = open(os.path.join(os.getcwd(), "Dispositivos", ip + ".txt"), "w")
            file.write("ip:" + ip + "-ver:" + ver + "-comm:" + comm + "-port:" + port)
            try:
                t = consulta(comm, ip, port, "1.3.6.1.2.1.1.1.0")  # Sistema Operativo
                if t == "":
                    raise Exception("Error al obtener la descripcion del sistema...")
                if "Linux" in t:
                    t = t.split()
            except Exception as e:
                print(e)
