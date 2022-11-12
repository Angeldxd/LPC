import smtplib, ssl
import getpass

from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def Envio_Correo():
    username = input("Ingresa el correo que enviará el mensaje: ")
    password = getpass.getpass("Ingresa la contraseña: ")

    destinatario = input("Ingresa el correo de tu destinatario: ")
    asunto = input("Ingresa el asunto del correo: ")

    mensaje = MIMEMultipart("alternative")
    mensaje["Subject"] = asunto
    mensaje["From"] = username
    mensaje["To"] = destinatario

    html = f"""
    <html>
    <body>
        Hola {destinatario}
        Esta correo que te envío es de prueba
    </body>
    </html>
    """

    parte_html = MIMEText(html, "html")
    text = mensaje.attach(parte_html)


 

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(username, password)
        print("Sesión iniciada")
        server.sendmail(username, destinatario, text)
        print("Mensaje enviado")

Envio_Correo()