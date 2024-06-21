import reflex as rx
from Eno.components.maridacion import maridar
from Eno.esp.views.navbar import navbar
from Eno.components.carrusel_blog import carousel_title
from Eno.esp.views.footer import footer_desktop, footer_mobile

@rx.page(
    route="/blog/maridar", 
    title="Maridar Vinos | Enotopía",
    description="Página de \"Maridación\" de Enotopía"
)

def maridar_vinos():
    return rx.box(
        navbar(),
        carousel_title("MARIDAJES", "/maridar.jpg", "center, center"),
        maridar(),
        footer_desktop(),
        footer_mobile()        
    )