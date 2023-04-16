from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors


def reporte1(path, title, info, image, table):
    try:
        mycanvas = canvas.Canvas(path, pagesize=letter)
        x = 50
        y = 742
        mycanvas.setFont('Helvetica', 18)
        for t in title:
            mycanvas.drawString(x+110, y, t)
            y -= 25
        y -= 40
        mycanvas.setFont('Helvetica', 14)
        mycanvas.drawImage(image, x+290, y-95, width=235, height=137)
        for i in info:
            mycanvas.drawString(x, y, i)
            y -= 23
        y -= 100
        t = Table(table)
        t.setStyle(TableStyle([
            ('ALIGN', (0,0), (-1, -1), 'CENTRE'),
            ('FONT', (0, 0), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 14),
            ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
            ('TEXTCOLOR', (1, 1), (-1, -1), colors.mediumblue),
            ('LINEBELOW', (0, 0), (-1, 0), colors.black),
            ('LINEAFTER', (0, 0), (0, -1), colors.black),
            ('LINEBELOW', (0, 1), (-1, -2), colors.black)
        ]))
        t.wrapOn(mycanvas, 150, 100)
        t.drawOn(mycanvas, x, y)
        mycanvas.save()
        return "Se ha creado el reporte en formato PDF y se ha guardado en la carpeta 'Reportes'!"
    except Exception as e:
        print(e)
        return "Error al generar el reporte: " + e.args[0]


def reporte2(path):
    try:
        mydoc = SimpleDocTemplate(path, pagesize=letter)

        mydoc.build()
    except Exception as e:
        print(e)
        return "Error al generar el reporte: " + e.args[0]
