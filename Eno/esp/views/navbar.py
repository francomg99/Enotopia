import reflex as rx
from Eno.styles.styles import Size, Color
from Eno.components.drawer import wine_menu_desktop, wine_menu_mobile

def navbar() -> rx.Component:
    return rx.hstack(
        rx.hstack(
            rx.flex(
            rx.link(
            rx.image(
                src="/brasil.png",
                alt="Bandera de Brasil - Cambio de idioma",
                width=["2em","2em"],
                margin_left=["1em","3em"],
            ),
                href="/br",
                align_items="center"
            ),
            ),
            rx.chakra.link(
            rx.chakra.image(
                src="/enotopia.png",
                alt="Logo de Enotopía - Letras Blancas",
                width=["6em","8em"],
                margin="1em",
            ),
                href="/",
            ),
            rx.spacer(),       
                wine_menu_desktop(),
                wine_menu_mobile(),           
            width="100%",
            align_items="center",
            spacing="4",
            margin_right=[Size.MEDIUM.value, Size.BIG.value ]           
        ),
        position="sticky",
        bg=Color.CUARTIARY.value,
        z_index="9999",
        top="0",
        width="100%",
        align="center"
    )