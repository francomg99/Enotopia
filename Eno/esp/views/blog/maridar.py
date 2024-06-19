import reflex as rx
from Eno.components.maridacion import maridar
from Eno.esp.views.navbar import navbar
from Eno.components.carrusel_blog import carousel_title

@rx.page(
    route="/blog/maridar", 
    title="Maridar Vinos | Enotopía",
    description="Página de \"Maridación\" de Enotopía"
)

def maridar_vinos():
    return rx.box(
        navbar(),
        carousel_title("MARIDACIÓN", "/maridar.jpeg", "center, center"),
        maridar(),        
    )