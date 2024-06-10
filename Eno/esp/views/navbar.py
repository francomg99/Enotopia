import reflex as rx
from Eno.styles.styles import Size, Color, TextColor
from Eno.components.drawer import wine_menu_desktop, wine_menu_mobile

def navbar() -> rx.Component:
    return rx.hstack(
        rx.hstack(
            rx.flex(
            rx.link(
            rx.image(
                src="/brasil.png",
                alt="Bandera de Brasil - Cambio de idioma",
                width=["2.5em","1.5em"],
                margin_left=["1em","3em"],
            ),
                href="/br",
                align_items="center"
            ),
            rx.tablet_and_desktop(
            rx.link("Portugués", align="left", weight="light", color=TextColor.PRIMARY.value, href="/br"),
            direction="row",
            align="center",
            spacing="2"
            )
            ),
            rx.chakra.link(
            rx.chakra.image(
                src="/enotopia.png",
                alt="Logo de Enotopía - Letras Negras",
                width=["25em","15em"],
                margin_left=["1em","4em"],
            ),
                href="/",
            ),
            rx.spacer(),       
                wine_menu_desktop(),
                wine_menu_mobile(),           
            width="100%",
            align_items="center",
            spacing="4",
            margin_right=Size.BIG.value            
        ),
        position="sticky",
        bg=Color.CUARTIARY.value,
        z_index="9999",
        top="0",
        width="100%",
        align="center"
    )#