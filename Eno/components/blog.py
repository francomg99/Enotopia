import reflex as rx
from Eno.styles.styles import Size, Color, TextColor

def blog(src: str, text: str, url: str) -> rx.Component:
    return rx.center(
        rx.box(  
            rx.hstack(
                rx.image(
                    src=src,
                    width=["100%", "40%"],  # Responsivo para móviles y pantallas grandes
                    height="auto",
                    _hover={"opacity": 0.8},
                ),
                rx.vstack(
                    rx.chakra.text(
                        text,
                        padding_right=Size.SMALL.value,
                        bg=Color.ACCENT.value,
                        style={
                            'color': TextColor.PRIMARY.value,
                            'font_size': Size.LETTER.value,
                            'text_align': 'justify'
                        }
                    ),
                    rx.chakra.link(
                        rx.chakra.button(
                            "+ info",                   
                            rx.icon(tag="wine", padding_left=Size.SMALL.value, size=30),                    
                            color=TextColor.ACCENT.value,
                            bg=Color.TERTIARY.value,
                            size="md",
                            margin_top=Size.MEDIUM.value,
                            _hover={
                                "background": Color.PRIMARY.value,
                                "color": TextColor.PRIMARY.value
                            },                  
                        ),
                        href=url,
                    ),
                    align_items="flex-start",  # Alineación de los textos al inicio
                ),
                align_items="center",  # Alineación entre imagen y texto
                spacing="4",
                flex_direction=["column", "row"],  # Direcciones diferentes para móviles y pantallas grandes
            ),
            width="90%",
            spacing="4",
            padding=Size.SMALL.value,
            margin=Size.SMALL.value,
            border_radius="20px",  # Estilo de borde agregado aquí
            bg=Color.ACCENT.value,  # Fondo opcional
            box_shadow="lg",  # Sombra opcional para darle profundidad
        )
    )
