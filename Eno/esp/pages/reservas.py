import reflex as rx
from Eno.esp.views.navbar import navbar
from Eno.components.contact import contact_and_title
from Eno.components.formulario import contact_form
from Eno.components.wine_line import wine_line
from Eno.esp.views.footer import footer_desktop, footer_mobile

@rx.page(
    route="/reservas", 
    title="Reserva con Nosotros | Enotopía",
    description="Página de \"Reservas\" de Enotopía"
)
def reservas() -> rx.Component:
    return rx.box(
        navbar(),
        # contact_and_title(), # Puedes habilitar esta línea si es necesario
        contact_form(),  # Asegúrate de que contact_form() es una función que devuelve un componente
        wine_line(),
        footer_desktop(),
        footer_mobile()
    )
