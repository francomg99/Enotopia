import reflex as rx
from reflex.state import State
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class ContactFormState(State):
    name: str = ""
    email: str = ""
    message: str = ""
    message_status: str = ""

    def set_name(self, value: str):
        print(f"Setting name: {value}")
        self.name = value

    def set_email(self, value: str):
        print(f"Setting email: {value}")
        self.email = value

    def set_message(self, value: str):
        print(f"Setting message: {value}")
        self.message = value

    def submit_form(self):
        print("Submitting form with the following data:")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Message: {self.message}")
        send_email(self.name, self.email, self.message)
        self.message_status = "Correo enviado exitosamente."
        print(f"Message status: {self.message_status}")

def send_email(name, email, message):
    smtp_server = 'smtp.gmail.com'  # Cambia esto si usas otro servidor SMTP
    smtp_port = 587  # Puerto estándar para TLS
    smtp_user = 'fralco000@gmail.com'  # Tu correo electrónico
    smtp_password = '2023'  # Tu contraseña o contraseña de aplicación

    msg = MIMEMultipart()
    msg['From'] = smtp_user
    msg['To'] = email
    msg['Subject'] = 'Nuevo mensaje del formulario de contacto'

    body = f"Nombre: {name}\nCorreo: {email}\nMensaje: {message}"
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.sendmail(smtp_user, email, msg.as_string())
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        ContactFormState.message_status = f"Error al enviar el correo: {e}"
        print(f"Failed to send email: {e}")

def contact_form():
    return rx.fragment(
        rx.input(value=ContactFormState.name, placeholder='Nombre', on_change=lambda e: ContactFormState.set_name(e)),
        rx.input(value=ContactFormState.email, placeholder='Correo', on_change=lambda e: ContactFormState.set_email(e)),
        rx.text_area(value=ContactFormState.message, placeholder='Mensaje', on_change=lambda e: ContactFormState.set_message(e)),
        rx.button("Enviar", on_click=ContactFormState.submit_form),
        rx.box(ContactFormState.message_status)  # Confirmación visual del estado del mensaje
    )
