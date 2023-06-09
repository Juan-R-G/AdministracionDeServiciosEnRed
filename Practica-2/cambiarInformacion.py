# Roldan-Gomez-Juan
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
from snmp import consulta


class ChInfo:
    def __init__(self):
        self.menu = Tk()
        self.menu.title("Cambiar Informacion")
        self.menu.resizable(False, False)
        self.frm = ttk.Frame(self.menu, padding=15)
        self.frm.grid()
        self.lbl0 = ttk.Label()
        self.flag = False
        self.devices = []
        if os.path.exists(os.path.join(os.getcwd(), "Dispositivos")):
            for root, dirs, files in os.walk(os.path.join(os.getcwd(), "Dispositivos")):
                for name in files:
                    self.devices.append(name.replace(".txt", ""))
            if len(self.devices):
                self.flag = True
        if self.flag:
            self.lbl0 = ttk.Label(self.frm, text="Seleccione un Dispositivo:")
        else:
            self.lbl0 = ttk.Label(self.frm, text="No hay dispositivos guardados...")
        self.lbl0.grid(columnspan=2, row=0)
        self.eleccion = StringVar()
        self.radioButtons = []
        self.row = 0
        if self.flag:
            for name in self.devices:
                self.radioButtons.append(ttk.Radiobutton(self.frm, text=name, value=name, variable=self.eleccion, command=lambda: self.enable()))
                self.row += 1
                self.radioButtons[self.row-1].grid(columnspan=2, row=self.row)
        self.lbl1 = ttk.Label()
        self.ent1 = ttk.Entry()
        self.lbl2 = ttk.Label()
        self.ent2 = ttk.Entry()
        self.lbl3 = ttk.Label()
        self.ent3 = ttk.Entry()
        self.lbl4 = ttk.Label()
        self.ent4 = ttk.Entry()
        self.btn1 = ttk.Button()
        if self.flag:
            self.btn1 = ttk.Button(self.frm, text="Guardar", command=lambda: self.actualizar(), state=DISABLED)
            self.btn1.grid(columnspan=2, row=self.row+5)
        else:
            self.btn1 = ttk.Button(self.frm, text="Continuar", command=lambda: self.menu.destroy())
            self.btn1.grid(columnspan=2, row=self.row+1)
        self.lbl5 = ttk.Label()
        self.menu.mainloop()

    def enable(self):
        self.btn1.state(["!disabled"])
        file = open(os.path.join(os.getcwd(), "Dispositivos", self.eleccion.get() + ".txt"), "r")
        t = file.readline().replace("\n", "")
        file.close()
        t = t.split('-')
        x = t[0].split(':')
        self.row = len(self.devices) + 1
        self.lbl1 = ttk.Label(self.frm, text="IP/Hostname:")
        self.lbl1.grid(column=0, row=self.row)
        self.ent1 = ttk.Entry(self.frm, width=25)
        self.ent1.insert(0, x[1])
        self.ent1.grid(column=1, row=self.row)
        x = t[1].split(':')
        self.row += 1
        self.lbl2 = ttk.Label(self.frm, text="Version SNMP:")
        self.lbl2.grid(column=0, row=self.row)
        self.ent2 = ttk.Entry(self.frm, width=25)
        self.ent2.insert(0, x[1])
        self.ent2.grid(column=1, row=self.row)
        x = t[2].split(':')
        self.row += 1
        self.lbl3 = ttk.Label(self.frm, text="Comunidad:")
        self.lbl3.grid(column=0, row=self.row)
        self.ent3 = ttk.Entry(self.frm, width=25)
        self.ent3.insert(0, x[1])
        self.ent3.grid(column=1, row=self.row)
        x = t[3].split(':')
        self.row += 1
        self.lbl4 = ttk.Label(self.frm, text="Puerto:")
        self.lbl4.grid(column=0, row=self.row)
        self.ent4 = ttk.Entry(self.frm, width=25)
        self.ent4.insert(0, x[1])
        self.ent4.grid(column=1, row=self.row)

    def actualizar(self):
        ip = self.ent1.get()
        ver = self.ent2.get()
        comm = self.ent3.get()
        port = self.ent4.get()

        if ip == "" or ver == "" or comm == "" or port == "":
            self.lbl5 = ttk.Label(self.frm, text="Llene todos los campos!", foreground="red")
            self.lbl5.grid(columnspan=2, row=self.row+2)
        else:
            self.lbl5.destroy()
            os.remove(os.path.join(os.getcwd(), "Dispositivos", self.eleccion.get() + ".txt"))
            file = open(os.path.join(os.getcwd(), "Dispositivos", ip + ".txt"), "w")
            file.write("ip:" + ip + "-ver:" + ver + "-comm:" + comm + "-port:" + port)
            try:
                t = consulta(comm, ip, port, "1.3.6.1.2.1.1.1.0")  # Sistema Operativo
                if t == "error":
                    file.close()
                    raise Exception("Error al obtener la descripcion del sistema...")
                if "Linux" in t:
                    t = t.split()
                    file.write("\nSistema Operativo:" + t[0])
                    file.write("_Version:" + t[2])
                elif "Windows" in t:
                    t = t.split(" - ")
                    t = t[1].split(":")
                    t = t[1].replace(" Version", "").split()
                    file.write("\nSistema Operativo:" + t[0])
                    file.write("_Version:" + t[1])
                else:
                    t = t.split()
                    file.write("\nSistema Operativo(?):" + t[0])

                t = consulta(comm, ip, port, "1.3.6.1.2.1.1.5.0")  # Nombre del Agente
                if t == "error":
                    file.close()
                    raise Exception("Error al obtener el nombre del agente...")
                file.write("\nDispositivo:" + t)

                t = consulta(comm, ip, port, "1.3.6.1.2.1.1.4.0")  # Contacto del Agente
                if t == "error":
                    file.close()
                    raise Exception("Error al obtener el contacto del agente...")
                file.write("\nContacto:" + t)

                t = consulta(comm, ip, port, "1.3.6.1.2.1.1.6.0")  # Ubicación del Agente
                if t == "error":
                    file.close()
                    raise Exception("Error al obtener la localización del agente...")
                file.write("\nUbicacion:" + t)

                t = consulta(comm, ip, port, "1.3.6.1.2.1.2.1.0")  # Numero de interfaces de red
                if t == "error":
                    file.close()
                    raise Exception("Error al obtener el numero de interfaces de red...")
                file.write("\nInterfaces:" + t)

                first = ''  # Primer Interfaz de Red 'Up'
                file.write("\n¡")
                n = int(t)
                if n < 6:
                    n = range(1, n+1)
                else:
                    n = range(1, 6)
                for x in n:
                    t = consulta(comm, ip, port, "1.3.6.1.2.1.2.2.1.2." + str(x))  # Nombre de una interfaz de red
                    if t == "error":
                        file.close()
                        raise Exception("Error al obtener la descripcion de una interfaz de red...")
                    if "0x" in t:
                        t = t.replace("0x", "").replace("00", "")
                        t = bytes.fromhex(t).decode('utf-8')
                    file.write("/" + t + ":")
                    t = consulta(comm, ip, port, "1.3.6.1.2.1.2.2.1.7." + str(x))  # Estado Administrativo de una interdaz de red
                    if t == "error":
                        file.close()
                        raise Exception("Error al obtener el estado administrativo de una interfaz de red...")
                    file.write(t)

                    if int(t) == 1 and first == '':
                        first = str(x)

                file.write("\n&" + first)
                file.close()
                self.menu.destroy()
                messagebox.showinfo("Cambiar Informacion", "Se han actualizado corrctamente los datos del dispositivo!")
            except Exception as e:
                print(e)
                file.write("\n" + e.args[0])
                file.close()
                self.menu.destroy()
                messagebox.showerror("Cambiar Informacion", "Error: " + e.args[0])

