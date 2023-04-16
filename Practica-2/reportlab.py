from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors


def reporte1(path, title, info, image, table):
    try:
        mycanvas = canvas.Canvas(path, pagesize=letter)
        mycanvas.save()
        return "Se ha creado el reporte en formato PDF y se ha guardado en la carpeta 'Reportes'!"
    except Exception as e:
        print(e)
        return "Error al generar el reporte: " + e.args[0]
