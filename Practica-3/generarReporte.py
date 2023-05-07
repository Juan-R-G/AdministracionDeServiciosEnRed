from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
from datetime import datetime
from report_lab import *
from rrdtoolGraph import grafica


class Report:
    def __init__(self):
        self.menu = Tk()
        self.menu.title("Generar Reporte")
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
            if len(self.devices):
                self.flag = True
        if self.flag:
            self.lbl1 = ttk.Label(self.frm, text="Seleccione un Dispositivo:")
        else:
            self.lbl1 = ttk.Label(self.frm, text="No hay dispositivos guardados...")
        self.row = 0
        self.lbl1.grid(columnspan=6, row=self.row)
        self.eleccion = StringVar()
        self.radioButtons = []
        if self.flag:
            for name in self.devices:
                self.radioButtons.append(ttk.Radiobutton(self.frm, text=name, value=name, variable=self.eleccion, command=lambda: self.dispositivo()))
                self.row += 1
                self.radioButtons[self.row-1].grid(columnspan=6, row=self.row)
        self.lbl2 = ttk.Label()
        self.tipoReporte = IntVar()
        self.radioButtons1 = []
        self.radioButtons1.append(ttk.Radiobutton(self.frm, text="Reporte General", value=1, variable=self.tipoReporte, command=lambda: self.tipo1()))
        self.radioButtons1.append(ttk.Radiobutton(self.frm, text="Reporte de Contabilidad", value=2, variable=self.tipoReporte, command=lambda: self.tipo2()))
        self.lbl3 = ttk.Label()
        self.lbl4 = ttk.Label()
        self.lbl5 = ttk.Label()
        self.lbl6 = ttk.Label()
        self.lbl7 = ttk.Label()
        self.lbl8 = ttk.Label()
        self.lbl9 = ttk.Label()
        self.lbl10 = ttk.Label()
        self.spin1 = ttk.Spinbox()
        self.spin2 = ttk.Spinbox()
        self.spin3 = ttk.Spinbox()
        self.spin4 = ttk.Spinbox()
        self.spin5 = ttk.Spinbox()
        self.spin6 = ttk.Spinbox()
        self.lbl11 = ttk.Label()
        self.lbl12 = ttk.Label()
        self.lbl13 = ttk.Label()
        self.lbl14 = ttk.Label()
        self.lbl15 = ttk.Label()
        self.lbl16 = ttk.Label()
        self.spin7 = ttk.Spinbox()
        self.spin8 = ttk.Spinbox()
        self.spin9 = ttk.Spinbox()
        self.spin10 = ttk.Spinbox()
        self.spin11 = ttk.Spinbox()
        self.spin12 = ttk.Spinbox()
        self.btn1 = ttk.Button()
        if self.flag:
            self.btn1 = ttk.Button(self.frm, text="Generar", command=lambda: self.generar(), state=DISABLED)
            self.btn1.grid(columnspan=6, row=self.row+9)
        else:
            self.btn1 = ttk.Button(self.frm, text="Continuar", command=lambda: self.menu.destroy())
            self.btn1.grid(columnspan=6, row=self.row+1)
        self.menu.mainloop()

    def dispositivo(self):
        self.lbl2 = ttk.Label(self.frm, text="Seleccione el reporte a generar:")
        self.row = len(self.devices) + 1
        self.lbl2.grid(columnspan=6, row=self.row)
        self.row += 1
        self.radioButtons1[0].grid(columnspan=6, row=self.row)
        self.row += 1
        self.radioButtons1[1].grid(columnspan=6, row=self.row)

    def tipo1(self):
        self.lbl3.destroy()
        self.lbl4.destroy()
        self.lbl5.destroy()
        self.lbl6.destroy()
        self.lbl7.destroy()
        self.lbl8.destroy()
        self.lbl9.destroy()
        self.lbl10.destroy()
        self.spin1.destroy()
        self.spin2.destroy()
        self.spin3.destroy()
        self.spin4.destroy()
        self.spin5.destroy()
        self.spin6.destroy()
        self.lbl11.destroy()
        self.lbl12.destroy()
        self.lbl13.destroy()
        self.lbl14.destroy()
        self.lbl15.destroy()
        self.lbl16.destroy()
        self.spin7.destroy()
        self.spin8.destroy()
        self.spin9.destroy()
        self.spin10.destroy()
        self.spin11.destroy()
        self.spin12.destroy()
        self.btn1.state(["!disabled"])

    def tipo2(self):
        self.row = len(self.devices) + 4
        self.lbl3 = ttk.Label(self.frm, text="Fecha Inicio")
        self.lbl3.grid(column=0, columnspan=3, row=self.row)
        self.lbl4 = ttk.Label(self.frm, text="Fecha Termino")
        self.lbl4.grid(column=3, columnspan=3, row=self.row)
        self.row += 1
        self.lbl5 = ttk.Label(self.frm, text="Dia:")
        self.lbl5.grid(column=0, row=self.row)
        self.lbl6 = ttk.Label(self.frm, text="Mes:")
        self.lbl6.grid(column=1, row=self.row)
        self.lbl7 = ttk.Label(self.frm, text="Año:")
        self.lbl7.grid(column=2, row=self.row)
        self.lbl8 = ttk.Label(self.frm, text="Dia:")
        self.lbl8.grid(column=3, row=self.row)
        self.lbl9 = ttk.Label(self.frm, text="Mes:")
        self.lbl9.grid(column=4, row=self.row)
        self.lbl10 = ttk.Label(self.frm, text="Año:")
        self.lbl10.grid(column=5, row=self.row)
        self.row += 1
        t = datetime.now()
        self.spin1 = ttk.Spinbox(self.frm, from_=1, to=31, width=5)
        self.spin1.insert(0, str(t.day))
        self.spin1.grid(column=0, row=self.row)
        self.spin2 = ttk.Spinbox(self.frm, from_=1, to=12, width=5)
        self.spin2.insert(0, str(t.month))
        self.spin2.grid(column=1, row=self.row)
        self.spin3 = ttk.Spinbox(self.frm, from_=2022, to=2023, width=5)
        self.spin3.insert(0, str(t.year))
        self.spin3.grid(column=2, row=self.row)
        self.spin4 = ttk.Spinbox(self.frm, from_=1, to=31, width=5)
        self.spin4.insert(0, str(t.day))
        self.spin4.grid(column=3, row=self.row)
        self.spin5 = ttk.Spinbox(self.frm, from_=1, to=12, width=5)
        self.spin5.insert(0, str(t.month))
        self.spin5.grid(column=4, row=self.row)
        self.spin6 = ttk.Spinbox(self.frm, from_=2022, to=2023, width=5)
        self.spin6.insert(0, str(t.year))
        self.spin6.grid(column=5, row=self.row)
        self.row += 1
        self.lbl11 = ttk.Label(self.frm, text="Hora:")
        self.lbl11.grid(column=0, row=self.row)
        self.lbl12 = ttk.Label(self.frm, text="Minutos:")
        self.lbl12.grid(column=1, row=self.row)
        self.lbl13 = ttk.Label(self.frm, text="Segundos:")
        self.lbl13.grid(column=2, row=self.row)
        self.lbl14 = ttk.Label(self.frm, text="Hora:")
        self.lbl14.grid(column=3, row=self.row)
        self.lbl15 = ttk.Label(self.frm, text="Minutos:")
        self.lbl15.grid(column=4, row=self.row)
        self.lbl16 = ttk.Label(self.frm, text="Segundos:")
        self.lbl16.grid(column=5, row=self.row)
        self.row += 1
        self.spin7 = ttk.Spinbox(self.frm, from_=0, to=23, width=5)
        self.spin7.insert(0, "0")
        self.spin7.grid(column=0, row=self.row)
        self.spin8 = ttk.Spinbox(self.frm, from_=0, to=59, width=5)
        self.spin8.insert(0, "0")
        self.spin8.grid(column=1, row=self.row)
        self.spin9 = ttk.Spinbox(self.frm, from_=0, to=59, width=5)
        self.spin9.insert(0, "0")
        self.spin9.grid(column=2, row=self.row)
        self.spin10 = ttk.Spinbox(self.frm, from_=0, to=23, width=5)
        self.spin10.insert(0, str(t.hour))
        self.spin10.grid(column=3, row=self.row)
        self.spin11 = ttk.Spinbox(self.frm, from_=0, to=59, width=5)
        self.spin11.insert(0, str(t.minute))
        self.spin11.grid(column=4, row=self.row)
        self.spin12 = ttk.Spinbox(self.frm, from_=0, to=59, width=5)
        self.spin12.insert(0, str(t.second))
        self.spin12.grid(column=5, row=self.row)
        self.btn1.state(["!disabled"])

    def generar(self):
        try:
            if self.tipoReporte.get() == 1:
                file = open(os.path.join(os.getcwd(), "Dispositivos", self.eleccion.get() + ".txt"), "r")
                content = [f.replace("\n", "") for f in file]
                file.close()
                title = ["Administracion de Servicios en Red", "Practica 1", "Juan Roldan Gomez            4CM14"]
                info = []
                t = content[0].split('-')
                x = t[0].split(':')
                info.append("IP: " + x[1])
                x = t[2].split(':')
                info.append("Comunidad: " + x[1])
                t = content[1].split('_')
                for v in t:
                    x = v.split(':')
                    info.append(x[0] + ": " + x[1])
                t = content[2].split(':')
                info.append(t[0] + ": " + t[1])
                t = content[3].split(':')
                info.append(t[0] + ": " + t[1])
                t = content[4].split(':')
                info.append(t[0] + ": " + t[1])
                t = content[5].split(':')
                info.append(t[0] + "(" + t[1] + "):")
                image = ""
                if "Windows" in content[1]:
                    image = os.path.join(os.getcwd(), "Images", "windows.png")
                else:
                    image = os.path.join(os.getcwd(), "Images", "linux.jpg")
                table = [["Interfaz", "Estado Administrativo"]]
                t = content[6].split('/')
                for v in t:
                    if '¡' in v:
                        continue
                    x = v.split(':')
                    if int(x[1]) == 1:
                        table.append([x[0], "Up"])
                    elif int(x[1]) == 2:
                        table.append([x[0], "Down"])
                    else:
                        table.append([x[0], "Testing"])
                if not os.path.exists(os.path.join(os.getcwd(), "Reportes")):
                    os.mkdir(os.path.join(os.getcwd(), "Reportes"))
                fname = os.path.join(os.getcwd(), "Reportes", self.eleccion.get() + "(Reporte General).pdf")
                msg = reporte1(fname, title, info, image, table)
                if "Error" in msg:
                    raise Exception(msg)
                self.menu.destroy()
                messagebox.showinfo("Generar Reporte", msg)
            elif self.tipoReporte.get() == 2:
                file = open(os.path.join(os.getcwd(), "Dispositivos", self.eleccion.get() + ".txt"), "r")
                content = [f.replace("\n", "") for f in file]
                file.close()
                title = ["Administracion de Servicios en Red", "Practica 2", "Juan Roldan Gomez            4CM14"]
                info = []
                t = content[0].split('-')
                x = t[0].split(':')
                info.append("IP: " + x[1])
                x = t[2].split(':')
                info.append("Comunidad: " + x[1])
                t = content[2].split(':')
                info.append("Dispositivo: " + t[1])
                inicio = self.spin1.get() + "/" + self.spin2.get() + "/" + self.spin3.get() + ", " + self.spin7.get() + ":" + self.spin8.get() + ":" + self.spin9.get()
                fin = self.spin4.get() + "/" + self.spin5.get() + "/" + self.spin6.get() + ", " + self.spin10.get() + ":" + self.spin11.get() + ":" + self.spin12.get()
                info.append("Fecha Inicio: " + inicio)
                info.append("Fecha Termino: " + fin)
                t1 = datetime.strptime(inicio, "%d/%m/%Y, %H:%M:%S")
                t2 = datetime.strptime(fin, "%d/%m/%Y, %H:%M:%S")
                start = int(datetime.timestamp(t1))
                end = int(datetime.timestamp(t2))
                if os.path.exists(os.path.join(os.getcwd(), "Databases", self.eleccion.get() + ".rrd")):
                    modules = []
                    variables = ["ifInUcastPkts", "ipInReceives", "icmpOutEchos", "tcpInSegs", "udpInDatagrams"]
                    titulos = {
                        "ifInUcastPkts": "Paquetes Unicast que ha recibido una interfaz de red",
                        "ipInReceives": "Paquetes recibidos a protocolos IP, incluyendo los errores",
                        "icmpOutEchos": "Mensajes ICMP echo que ha enviado el agente",
                        "tcpInSegs": "Segmentos TCP recibidos, incluyendo los recibidos con errores",
                        "udpInDatagrams": "Datagramas entregados a usuarios UDP"
                    }
                    unidades = {
                        "ifInUcastPkts": "Paquetes",
                        "ipInReceives": "Paquetes",
                        "icmpOutEchos": "Mensajes",
                        "tcpInSegs": "Bytes",
                        "udpInDatagrams": "Datagramas"
                    }
                    nombres = {
                        "ifInUcastPkts": "Paquetes recibidos",
                        "ipInReceives": "Paquetes recibidos",
                        "icmpOutEchos": "Mensajes enviados",
                        "tcpInSegs": "Segmentos recibidos",
                        "udpInDatagrams": "Datagramas entregados"
                    }
                    operacion = {
                        "ifInUcastPkts": "",
                        "ipInReceives": "",
                        "icmpOutEchos": "",
                        "tcpInSegs": ",8,*",
                        "udpInDatagrams": ""
                    }
                    for var in variables:
                        t = os.path.join(os.getcwd(), "Images", self.eleccion.get() + "(" + var + ").png")
                        x = grafica(t, start, end, titulos[var], unidades[var], var, os.path.join(os.getcwd(), "Databases", self.eleccion.get()+".rrd"), operacion[var], nombres[var])
                        if "Error" in x:
                            raise Exception(x)
                        modules.append([titulos[var], t])
                    if not os.path.exists(os.path.join(os.getcwd(), "Reportes")):
                        os.mkdir(os.path.join(os.getcwd(), "Reportes"))
                    fname = os.path.join(os.getcwd(), "Reportes", self.eleccion.get() + "(Reporte de Contabilidad).pdf")
                    msg = reporte2(fname, title, info, modules)
                    if "Error" in msg:
                        raise Exception(msg)
                    self.menu.destroy()
                    messagebox.showinfo("Generar Reporte", msg)
                else:
                    raise Exception("No existe una base de datos para el dispositivo seleccionado")
            else:
                raise Exception("Error al seleccionar un reporte...")
        except Exception as e:
            print(e)
            self.menu.destroy()
            messagebox.showerror("Generar Reporte", "Error: " + e.args[0])
