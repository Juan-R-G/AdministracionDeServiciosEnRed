from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
from datetime import datetime
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
        self.lbl1.grid(columnspan=6, row=0)
        self.eleccion = StringVar()
        self.radioButtons = []
        self.row = 0
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
        self.lbl3.grid(columnspan=3, row=self.row)
        self.lbl4 = ttk.Label(self.frm, text="Fecha Termino")
        self.lbl4.grid(columnspan=3, row=self.row)
        self.row += 1
        self.lbl5 = ttk.Label(self.frm, text="Dia")
        self.lbl5.grid(column=0, row=self.row)
        self.lbl6 = ttk.Label(self.frm, text="Mes")
        self.lbl6.grid(column=1, row=self.row)
        self.lbl7 = ttk.Label(self.frm, text="Año")
        self.lbl7.grid(column=2, row=self.row)
        self.lbl8 = ttk.Label(self.frm, text="Dia")
        self.lbl8.grid(column=3, row=self.row)
        self.lbl9 = ttk.Label(self.frm, text="Mes")
        self.lbl9.grid(column=4, row=self.row)
        self.lbl10 = ttk.Label(self.frm, text="Año")
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
        self.lbl11 = ttk.Label(self.frm, text="Hora")
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

    def generar(self):
        pass
