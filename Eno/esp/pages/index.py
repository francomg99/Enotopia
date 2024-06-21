import reflex as rx
from Eno.esp.views.navbar import navbar
from Eno.components.carrusel_blog import header_title, slick
from Eno.esp.views.index.index_blog import blog_mobile, blog_desktop
from Eno.esp.views.index.index_reservas import contact_and_title
from Eno.components.wine_line import wine_line
from Eno.esp.views.index.index_nosotros import quienes_somos_desktop, quienes_somos_mobile
from Eno.esp.views.footer import footer_desktop, footer_mobile
from Eno.components.foto_ig import foto_ig

@rx.page(
    route="/", 
    title="Enotopía | Donde los viajes se encuentran con el vino.",
    description="Página web de Enotopía"
    )

def index() -> rx.Component:
    return rx.box(
        navbar(),
        slick(
            header_title(
                "DONDE LOS VIAJES",
                "SE ENCUENTRAN CON EL VINO",
                "Reserva con nosotros",
                "/reservas",
                "/diamandes.jpg"
            ),
            header_title(
                "EXPLORÁ BODEGAS EXCLUSIVAS",
                "EN NUESTRA AGENCIA DE TURISMO",
                "Reserva con nosotros",
                "/reservas",
                "/monteviejo.jpeg"
            ),            
            header_title(
                "DESCUBRÍ EN CADA VINO",
                "LA EXPRESIÓN DE SU TIERRA",
                "Reserva con nosotros",
                "/reservas",
                "/monteviejo.jpg"
            ),
            header_title(
                "CADA VIAJE ES UNA OPORTUNIDAD",
                "PARA DESCUBRIR EXPERIENCIAS ÚNICAS",
                "Reserva con nosotros",
                "/reservas",
                "/cava1.jpg"
            ),
            ),
        quienes_somos_desktop(),
        quienes_somos_mobile(),
        #wine_line(),
        blog_desktop(),
        blog_mobile(),
        contact_and_title(),
        foto_ig(),
        wine_line(),
        footer_desktop(),
        footer_mobile(),
        wine_line()
    )

#