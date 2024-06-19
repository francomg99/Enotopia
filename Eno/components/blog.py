import reflex as rx
from Eno.styles.styles import Color, Size, TextColor

def mobile_blog(src:str, text: str, url:str)->rx.Component:
      return rx.mobile_only(
                rx.center(
                    rx.vstack(
                    rx.card(
                        rx.inset(
                            rx.image(
                                src=src,
                                width="100%",
                                height="auto",
                                _hover={
                                    "opacity": 0.8,
                                },
                            ),
                            side="top",
                            pb="current",
                        ),
                            rx.text(
                                text,
                                style={
                                    'background':Color.ACCENT.value,
                                    'color':TextColor.PRIMARY.value,
                                    'font_size':Size.LETTER.value,
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
                        width=["100%","43vw"],
                        bg=Color.ACCENT.value,
                        border_color=Color.SECONDARY.value
                    ),
                    padding_left=[Size.SMALL.value, Size.BIG.value],
                    padding_right=[Size.SMALL.value, Size.ZERO.value]
                    )
      )
      )
      

def blog(src: str,text: str, url:str) -> rx.Component:
    return rx.center(
        rx.box(  # Contenedor general con borde
            rx.hstack(
                rx.image(
                    src=src,
                    width="45%",
                    height="auto",
                    _hover={"opacity": 0.8},
                ),
                rx.vstack(
                rx.chakra.text(
                    text,
                    padding_right=Size.SMALL.value,
                    bg=Color.ACCENT.value,
                    style={
                        'color':TextColor.PRIMARY.value,
                        'font_size':Size.LETTER.value,
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
                ),
                align_items="center",  # Alineación entre imagen y texto
            ),
            width="90%",
            spacing="4",
            padding=Size.SMALL.value,
            margin=Size.SMALL.value,
            #border="0.5px solid #ECDAE2",
            border_radius="20px"# Estilo de borde agregado aquí
        )
    )