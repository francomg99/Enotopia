import reflex as rx
from Eno.esp.views.navbar import navbar
from Eno.esp.views.quienes_somos.quienes_somos import quienes_somos_desktop, quienes_somos_mobile
from Eno.esp.views.footer import footer_desktop, footer_mobile
from Eno.components.wine_line import wine_line, other_line
from Eno.esp.views.index.valentina import enotopia_desktop, enotopia_mobile

@rx.page(
    route="/quienes_somos", 
    title="¿Quiénes somos? | Enotopía",
    description="Página de \"¿Quiénes somos?\" de Enotopía"
    )

def quienes_somos()->rx.Component:
    return rx.box(
        navbar(),
        quienes_somos_desktop(),
        quienes_somos_mobile(),
        other_line(),
        enotopia_mobile(),
        enotopia_desktop(),
        other_line(),       
        footer_desktop(),
        footer_mobile()
        )