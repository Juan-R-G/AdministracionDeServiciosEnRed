from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter


def pdf(path, title, info, image, table):
    try:
        mycanvas = canvas.Canvas(path, pagesize=letter)
        x = 50
        y = 762
        mycanvas.setFont('Helvetica', 18)
        for t in title:
            mycanvas.drawString(x, y, t)
            y -= 20
        y -= 40
        mycanvas.setFont('Helvetica', 14)
        mycanvas.drawImage(image, x+300, y-70, width=235, height=137)
        for i in info:
            mycanvas.drawString(x, y, i)
            y -= 20
        y -= 30
        mycanvas.save()
        return "Se ha creado el reporte en formato PDF y se ha guardado en la carpeta 'Reportes'"
    except:
        return "Ha ocurrido un error al generar o guardar el reporte..."
