import reflex as rx
from Eno.esp.views.navbar import navbar
from Eno.components.contact import contact_and_title
from Eno.components.wine_line import footer_line, other_line
from Eno.esp.views.footer import footer_desktop, footer_mobile

@rx.page(
    route="/reservas", 
    title="Reserva con Nosotros | Enotopía",
    description="Página de \"Reservas\" de Enotopía"
)
def reservas() -> rx.Component:
    return rx.box(
        navbar(),
        contact_and_title(), # Puedes habilitar esta línea si es necesario
        other_line(),
        footer_desktop(),
        footer_mobile(),
        footer_line(),
    )
