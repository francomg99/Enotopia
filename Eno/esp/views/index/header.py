import reflex as rx
from Eno.styles.styles import Size
from Eno.styles.fonts import Font
from Eno.styles.colors import Color, TextColor

def header_with_image_and_text():
    return rx.hstack(
        rx.box(
            rx.text(
                "Donde los viajes", 
                line_height=["0.8", "1"],
                align="left", 
                size="8", 
                as_="div",
                color=TextColor.ACCENT.value,
                font_family=Font.TITLE.value,
                style={
                    'font_size':["4em","5em"]
                }
            ),
            rx.text(
                "se encuentran con el vino",
                line_height=["0.8", "1"], 
                align="left", 
                size="8", 
                as_="div",
                color=TextColor.ACCENT.value,
                font_family=Font.TITLE.value,
                style={
                    'font_size':["4em","5em"]
                }
            ),            
            rx.chakra.link(
                rx.chakra.button(
                    "Reservá con nosotros",                   
                    rx.icon(tag="phone", padding_left=Size.SMALL.value, size=30),                    
                    color=TextColor.ACCENT.value,
                    bg=Color.PRIMARY.value,
                    size="md",
                    margin_top=Size.MEDIUM.value,
                    _hover={
                        "background": Color.TERTIARY.value,
                        "color": TextColor.PRIMARY.value
                    },                  
                    ),
                    href="/reservas",
            ),
                bg="center/cover url('/montaña.jpg')",
                align_items="center",
                spacing="4",
                width="100%",
                height=["25em","37em"],
                padding_x=["1.5em","3em"],
                padding_y=["5em","14em"],
                top="0"
                ),
    )

