from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os


class DelDev:
    def __init__(self):
        self.menu = Tk()
        self.menu.title("Eliminar Dispositivo")
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
            if len(self.devices):
                self.flag = True
        if self.flag:
            self.lbl1 = ttk.Label(self.frm, text="Seleccione un Dispositivo:")
        else:
            self.lbl1 = ttk.Label(self.frm, text="No hay dispositivos guardados...")
        self.lbl1.grid(column=0, row=0)
        self.eleccion = StringVar()
        self.radioButtons = []
        self.row = 0
        if self.flag:
            for name in self.devices:
                self.radioButtons.append(ttk.Radiobutton(self.frm, text=name, value=name, variable=self.eleccion, command=lambda: self.btn1.state(["!disabled"])))
                self.row += 1
                self.radioButtons[self.row-1].grid(column=0, row=self.row)
        self.btn1 = ttk.Button()
        if self.flag:
            self.btn1 = ttk.Button(self.frm, text="Eliminar", command=lambda: self.eliminar(), state=DISABLED)
        else:
            self.btn1 = ttk.Button(self.frm, text="Continuar", command=lambda: self.menu.destroy())
        self.btn1.grid(column=0, row=self.row+1)
        self.menu.mainloop()

    def eliminar(self):
        try:
            os.remove(os.path.join(os.getcwd(), "Dispositivos", self.eleccion.get() + ".txt"))
            self.menu.destroy()
            messagebox.showinfo("Eliminar Dispositivo", "Se ha eliminado el dispositivo correctamente!")
        except Exception as e:
            print(e)
            self.menu.destroy()
            messagebox.showerror("Eliminar Dispositivo", "Error al intentar eliminar el dispositivo: " + e.args[0])
