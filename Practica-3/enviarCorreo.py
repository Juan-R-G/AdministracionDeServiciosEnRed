import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage


def enviar(asunto, mensaje, imagen):
    de = "juan.0403.0112@gmail.com"
    para = "juan.0403.0112@gmail.com"
    mailserver = "smtp.gmail.com: 587"
    contrasena = ""
    try:
        msg = MIMEMultipart()
        msg['Subject'] = asunto
        msg['From'] = de
        msg['To'] = para
        f = open(imagen, "rb")
        img = MIMEImage(f.read())
        f.close()
        msg.attach(img)
        s = smtplib.SMTP(mailserver)
        s.starttls()
        s.login(de, contrasena)
        s.sendmail(de, para, msg.as_string())
        s.quit()

        print("Se envio exitosamente el correo de notificacion!")
    except Exception as e:
        print("Error al enviar el correo: " + e.args[0])
