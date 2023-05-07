from tkinter import *
from tkinter import ttk
import os
import rrdtool
import datetime
from snmp import consulta
from rrdtoolGraph import grafica1, grafica2
from enviarCorreo import enviar
import time


class Supervisor:
    def __init__(self):
        self.menu = Tk()
        self.menu.title("Monitor del Rendimiento de los Agentes Registrados")
        self.menu.resizable(False, False)
        self.frm = ttk.Frame(self.menu, padding=1)
        self.frm.grid()
        self.lbl1 = ttk.Label(self.frm, text="Agentes", padding=10)
        self.lbl1.grid(column=0, row=0)
        self.lbl2 = ttk.Label(self.frm, text="Estado del CPU 1", padding=10)
        self.lbl2.grid(column=1, row=0)
        self.lbl3 = ttk.Label(self.frm, text="Estado de la RAM", padding=10)
        self.lbl3.grid(column=2, row=0)
        self.devices = []
        if os.path.exists(os.path.join(os.getcwd(), "Dispositivos")):
            for root, dirs, files in os.walk(os.path.join(os.getcwd(), "Dispositivos")):
                for name in files:
                    self.devices.append(name.replace(".txt", ""))
        self.lbls = []
        for name in self.devices:
            self.lbls.append([ttk.Label(), ttk.Label(), ttk.Label()])
        self.btn1 = ttk.Button(self.frm, text="Comenzar", command=lambda: self.monitor())
        self.btn1.grid(columnspan=3, row=1)
        self.lbl4 = ttk.Label()
        self.lbl5 = ttk.Label()
        self.CPUu3 = 0
        self.CPUu2 = 0
        self.CPUu1 = 0
        self.RAMu3 = 0
        self.RAMu2 = 0
        self.RAMu1 = 0
        self.menu.mainloop()

    def monitor(self):
        self.btn1.destroy()
        while len(self.devices):
            for i in range(0, len(self.devices)):
                try:
                    last_update = rrdtool.lastupdate(os.path.join(os.getcwd(), "Databases", self.devices[i] + ".rrd"))
                    time_stamp = last_update['date'].timestamp()
                    print(time_stamp)
                    cpu = last_update['ds']['procLoad']
                    ramu = last_update['ds']['ramUsed']
                    cach = last_update['ds']['cachUsed']
                    file = open(os.path.join(os.getcwd(), "Dispositivos", self.devices[i] + ".txt"), "r")
                    t = file.readline().replace("\n", "")
                    file.close()
                    t = t.split('-')
                    tram = int(consulta(t[2].split(':')[1], t[0].split(':')[1], t[3].split(':')[1], "1.3.6.1.2.1.25.2.2.0"))
                    ram = round(((ramu - cach) * 100 / tram), 2)
                    self.lbls[i][0] = ttk.Label(self.frm, text=self.devices[i])
                    self.lbls[i][0].grid(column=0, row=i+1)
                    if cpu > 90:  # Rojo
                        self.lbls[i][1] = ttk.Label(self.frm, text=str(cpu) + " %", foreground="red")
                        self.lbl4 = ttk.Label(self.frm, text="El dispositivo " + self.devices[i] + " ha sobrepasado el tercer umbral respecto al uso del CPU\nSe recomienda ejecutar un plan de accion\nSe ha enviado la notificacion por correo electronico")
                        self.lbl4.grid(columnspan=3, row=len(self.devices)+1)
                        if not self.CPUu3:
                            self.CPUu3 = 3
                            self.CPUu2 = 0
                            self.CPUu1 = 0
                    elif cpu > 75:  # Naranja
                        self.lbls[i][1] = ttk.Label(self.frm, text=str(cpu) + " %", foreground="orange")
                        self.lbl4 = ttk.Label(self.frm, text="El dispositivo " + self.devices[i] + " ha sobrepasado el segundo umbral respecto al uso del CPU\nSe recomienda formular un plan de accion\nSe ha enviado la notificacion por correo electronico")
                        self.lbl4.grid(columnspan=3, row=len(self.devices)+1)
                        if not self.CPUu2:
                            self.CPUu3 = 0
                            self.CPUu2 = 3
                            self.CPUu1 = 0
                    elif cpu > 60:  # Amarillo
                        self.lbls[i][1] = ttk.Label(self.frm, text=str(cpu) + " %", foreground="yellow")
                        self.lbl4 = ttk.Label(self.frm, text="El dispositivo " + self.devices[i] + " ha sobrepasado el primer umbral respecto al uso del CPU\nSe recomienda investigar\nSe ha enviado la notificacion por correo electronico")
                        self.lbl4.grid(columnspan=3, row=len(self.devices)+1)
                        if not self.CPUu1:
                            self.CPUu3 = 0
                            self.CPUu2 = 0
                            self.CPUu1 = 3
                    else:  # Verde
                        self.lbls[i][1] = ttk.Label(self.frm, text=str(cpu) + " %", foreground="green")
                        self.CPUu3 = 0
                        self.CPUu2 = 0
                        self.CPUu1 = 0
                    self.lbls[i][1].grid(column=1, row=i+1)
                    if ram > 90:  # Rojo
                        self.lbls[i][2] = ttk.Label(self.frm, text=str(ram) + " %", foreground="red")
                        self.lbl5 = ttk.Label(self.frm, text="El dispositivo " + self.devices[i] + " ha sobrepasado el tercer umbral respecto al uso de la RAM\nSe recomienda ejecutar un plan de accion\nSe ha enviado la notificacion por correo electronico")
                        self.lbl5.grid(columnspan=3, row=len(self.devices)+2)
                        if not self.RAMu3:
                            self.RAMu3 = 3
                            self.RAMu2 = 0
                            self.RAMu1 = 0
                    elif ram > 75:  # Naranja
                        self.lbls[i][2] = ttk.Label(self.frm, text=str(ram) + " %", foreground="orange")
                        self.lbl5 = ttk.Label(self.frm, text="El dispositivo " + self.devices[i] + " ha sobrepasado el segundo umbral respecto al uso de la RAM\nSe recomienda formular un plan de accion\nSe ha enviado la notificacion por correo electronico")
                        self.lbl5.grid(columnspan=3, row=len(self.devices)+2)
                        if not self.RAMu2:
                            self.RAMu3 = 0
                            self.RAMu2 = 3
                            self.RAMu1 = 0
                    elif ram > 60:  # Amarillo
                        self.lbls[i][2] = ttk.Label(self.frm, text=str(ram) + " %", foreground="yellow")
                        self.lbl5 = ttk.Label(self.frm, text="El dispositivo " + self.devices[i] + " ha sobrepasado el primer umbral respecto al uso de la RAM\nSe recomienda investigar\nSe ha enviado la notificacion por correo electronico")
                        self.lbl5.grid(columnspan=3, row=len(self.devices)+2)
                        if not self.RAMu1:
                            self.RAMu3 = 0
                            self.RAMu2 = 0
                            self.RAMu1 = 3
                    else:  # Verde
                        self.lbls[i][2] = ttk.Label(self.frm, text=str(ram) + " %", foreground="green")
                        self.RAMu3 = 0
                        self.RAMu2 = 0
                        self.RAMu1 = 0
                    self.lbls[i][2].grid(column=2, row=i+1)
                    if self.CPUu3:
                        if self.CPUu3 == 3:
                            image = os.path.join(os.getcwd(), "Images", self.devices[i] + "(procLoad).png")
                            x = grafica1(image, int(time_stamp)-300, int(time_stamp), "(Sobrepaso del umbral 3)", os.path.join(os.getcwd(), "Databases", self.devices[i] + ".rrd"))
                            if x == "OK":
                                enviar("ALERTA: UMBRAL 3 SOBREPASADO!", "El dispositivo " + self.devices[i] + " ha sobrepasado el tercer umbral respecto al uso del CPU 1. Se recomienda ejecutar un plan de accion.", image)
                            else:
                                print("Error al obtener los recursos para enviar al correo: " + x)
                            self.CPUu3 -= 1
                        else:
                            self.CPUu3 -= 1
                    elif self.CPUu2:
                        if self.CPUu2 == 3:
                            image = os.path.join(os.getcwd(), "Images", self.devices[i] + "(procLoad).png")
                            x = grafica1(image, int(time_stamp) - 300, int(time_stamp), "(Sobrepaso del umbral 2)", os.path.join(os.getcwd(), "Databases", self.devices[i] + ".rrd"))
                            if x == "OK":
                                enviar("ALERTA: UMBRAL 2 SOBREPASADO!", "El dispositivo " + self.devices[i] + " ha sobrepasado el segundo umbral respecto al uso del CPU 1. Se recomienda formular un plan de accion.", image)
                            else:
                                print("Error al obtener los recursos para enviar al correo: " + x)
                            self.CPUu2 -= 1
                        else:
                            self.CPUu2 -= 1
                    elif self.CPUu1:
                        if self.CPUu1 == 3:
                            image = os.path.join(os.getcwd(), "Images", self.devices[i] + "(procLoad).png")
                            x = grafica1(image, int(time_stamp) - 300, int(time_stamp), "(Sobrepaso del umbral 1)", os.path.join(os.getcwd(), "Databases", self.devices[i] + ".rrd"))
                            if x == "OK":
                                enviar("ALERTA: UMBRAL 1 SOBREPASADO!", "El dispositivo " + self.devices[i] + " ha sobrepasado el primer umbral respecto al uso del CPU 1. Se recomienda investigar.", image)
                            else:
                                print("Error al obtener los recursos para enviar al correo: " + x)
                            self.CPUu1 -= 1
                        else:
                            self.CPUu1 -= 1
                    if self.RAMu3:
                        if self.RAMu3 == 3:
                            image = os.path.join(os.getcwd(), "Images", self.devices[i] + "(ramUsed).png")
                            x = grafica2(image, int(time_stamp) - 300, int(time_stamp), "(Sobrepaso del umbral 3)", os.path.join(os.getcwd(), "Databases", self.devices[i] + ".rrd"), tram)
                            if x == "OK":
                                enviar("ALERTA: UMBRAL 3 SOBREPASADO!", "El dispositivo " + self.devices[i] + " ha sobrepasado el primer umbral respecto al uso de la RAM. Se recomienda ejecutar un plan de accion.", image)
                            else:
                                print("Error al obtener los recursos para enviar al correo: " + x)
                            self.RAMu3 -= 1
                        else:
                            self.RAMu3 -= 1
                    elif self.RAMu2:
                        if self.RAMu2 == 3:
                            image = os.path.join(os.getcwd(), "Images", self.devices[i] + "(ramUsed).png")
                            x = grafica2(image, int(time_stamp) - 300, int(time_stamp), "(Sobrepaso del umbral 2)", os.path.join(os.getcwd(), "Databases", self.devices[i] + ".rrd"), tram)
                            if x == "OK":
                                enviar("ALERTA: UMBRAL 2 SOBREPASADO!", "El dispositivo " + self.devices[i] + " ha sobrepasado el primer umbral respecto al uso de la RAM. Se recomienda formular un plan de accion.", image)
                            else:
                                print("Error al obtener los recursos para enviar al correo: " + x)
                            self.RAMu2 -= 1
                        else:
                            self.RAMu2 -= 1
                    elif self.RAMu1:
                        if self.RAMu1 == 3:
                            image = os.path.join(os.getcwd(), "Images", self.devices[i] + "(ramUsed).png")
                            x = grafica2(image, int(time_stamp) - 300, int(time_stamp), "(Sobrepaso del umbral 1)", os.path.join(os.getcwd(), "Databases", self.devices[i] + ".rrd"), tram)
                            if x == "OK":
                                enviar("ALERTA: UMBRAL 1 SOBREPASADO!", "El dispositivo " + self.devices[i] + " ha sobrepasado el primer umbral respecto al uso de la RAM. Se recomienda investigar.", image)
                            else:
                                print("Error al obtener los recursos para enviar al correo: " + x)
                            self.RAMu1 -= 1
                        else:
                            self.RAMu1 -= 1
                except Exception as e:
                    print("Error al monitorizar el dispositivo " + self.devices[i] + ": " + e.args[0])
                    self.labels()
                    del self.lbls[i]
                    del self.devices[i]
                    break
            self.menu.update()
            time.sleep(10)
            self.labels()

    def labels(self):
        for lbl in self.lbls:
            lbl[0].destroy()
            lbl[1].destroy()
            lbl[2].destroy()
        self.lbl4.destroy()
        self.lbl5.destroy()


Supervisor()
