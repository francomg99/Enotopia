import reflex as rx
from Eno.esp.views.navbar import navbar
from Eno.esp.views.index.header import header_with_image_and_text
from Eno.esp.views.index.index_blog import blog_mobile, blog_desktop
from Eno.components.contact import contact_and_title
from Eno.components.wine_line import wine_line
from Eno.esp.views.quienes_somos.quienes_somos import quienes_somos_desktop, quienes_somos_mobile
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
        header_with_image_and_text(),
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