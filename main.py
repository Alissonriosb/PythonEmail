import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()
def enviar_correo(destinatario, asunto, cuerpo):
    # Configurar los detalles del servidor SMTP
    servidor_smtp = os.getenv('SMTP_SERVER')
    puerto_smtp = 587
    usuario = os.getenv('USER')
    contraseña = os.getenv('PASSWORD')

    # Crear el objeto mensaje
    mensaje = MIMEMultipart()
    mensaje['From'] = usuario
    mensaje['To'] = destinatario
    mensaje['Subject'] = asunto

    # Adjuntar el cuerpo del mensaje
    mensaje.attach(MIMEText(cuerpo, 'plain'))

    # Conectar al servidor SMTP
    servidor = smtplib.SMTP(servidor_smtp, puerto_smtp)
    servidor.starttls()  # Habilitar el cifrado TLS

    # Iniciar sesión en el servidor SMTP
    servidor.login(usuario, contraseña)

    # Enviar el correo electrónico
    servidor.send_message(mensaje)

    # Cerrar la conexión al servidor SMTP
    servidor.quit()


destinatario = 'correodestino@gmail.com'
asunto = 'Prueba'
cuerpo = 'Este es un correo electrónico automatizado enviado desde Python.'
enviar_correo(destinatario, asunto, cuerpo)
