from tkinter import *
from tkinter import ttk
import os
from snmp import *


class AddDev:
    def __init__(self):
        self.menu = Tk()
        self.menu.title("Agregar Dispositivo")
        # self.menu.geometry("750x440")
        self.menu.resizable(False, False)
        self.frm = ttk.Frame(self.menu, padding=10)
        self.frm.grid()
        self.lbl1 = ttk.Label(self.frm, text="IP/Hostname:")
        self.lbl1.grid(column=0, row=0)
        self.ent1 = ttk.Entry(self.frm, width=30)
        self.ent1.grid(column=1, row=0)
        self.lbl2 = ttk.Label(self.frm, text="Version SNMP:")
        self.lbl2.grid(column=0, row=1)
        self.ent2 = ttk.Entry(self.frm, width=30)
        self.ent2.grid(column=1, row=1)
        self.lbl3 = ttk.Label(self.frm, text="Comunidad:")
        self.lbl3.grid(column=0, row=2)
        self.ent3 = ttk.Entry(self.frm, width=30)
        self.ent3.grid(column=1, row=2)
        self.lbl4 = ttk.Label(self.frm, text="Puerto")
        self.lbl4.grid(column=0, row=3)
        self.ent4 = ttk.Entry(self.frm, width=30)
        self.ent4.insert(0, "161")
        self.ent4.grid(column=1, row=3)
        self.btn1 = ttk.Button(self.frm, text="Agregar", command=lambda: self.agregar())
        self.btn1.grid(columnspan=2, row=4)
        self.lbl5 = ttk.Label()
        self.menu.mainloop()

    def agregar(self):
        ip = self.ent1.get()
        ver = self.ent2.get()
        comm = self.ent3.get()
        port = self.ent4.get()
        if ip == "" or ver == "" or comm == "" or port == "":
            self.lbl5 = ttk.Label(self.frm, text="Llene todos los campos!")
            self.lbl5.grid(columnspan=2, row=5)
        else:
            self.lbl5.destroy()
            if not os.path.exists(os.path.join(os.getcwd(), "Dispositivos")):
                os.mkdir(os.path.join(os.getcwd(), "Dispositivos"))
            file = open(os.path.join(os.getcwd(), "Dispositivos", ip + ".txt"), "w")
            file.write("ip:" + ip + "\nver:" + ver + "\ncomm:" + comm + "\nport:" + port)
            file.close()
            self.menu.destroy()


# AddDev()
