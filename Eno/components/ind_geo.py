import reflex as rx
import Eno.styles.styles as styles
from Eno.styles.styles import Size, TextColor, Font
from Eno.components.button import other_button

def ind_geo(title, text, text1, bottom_text, url):
    text_style = {
        'color': TextColor.PRIMARY.value,
        'font_size': Size.LETTER.value,
        'text_align': 'justify',
        'margin_top': '0.5em',
    }
    bottom_text_style = {
        'color': TextColor.PRIMARY.value,
        'font_size': '0.75em',
        'text_align': 'left',
        'margin_top': '0.5em',
    }
    title_style = {
        "width" : "100%",
        "font_size" : "2.7em",
        "font_family" : Font.TITLE.value,
        "color" : TextColor.SECONDARY.value,
    }
    return rx.heading(
        rx.box(
            # Bloque 1: Izquierda
            rx.box(
                rx.text(
                    title,
                    as_="div",
                    style=title_style,
                    padding_bottom="0.2em"
                ),
                rx.text(
                    text,
                    weight="light",
                    style=text_style,
                    width="100%"
                ),
                rx.text(
                    text1,
                    weight="light",
                    style=text_style,
                    width="100%"
                ),
                other_button(
                    "¿Cómo llegar?",
                    "https://maps.com"
                ),
                style={
                    "position": "absolute",
                    "top": "50%",
                    "left": "5%",
                    "transform": "translateY(-50%)",
                    "text_align": "left",
                    "width": "40%",
                    "z_index": "1",
                }
            ),
            # Bloque 2: Abajo a la izquierda
            rx.box(
                rx.text(
                    bottom_text,
                    weight="light",
                    style=bottom_text_style,
                    width="100%"
                ),
                style={
                    "position": "absolute",
                    "bottom": "2.5%",
                    "right": "2.5%",
                    "z_index": "1"
                }
            ),
            style={
                "background": f"linear-gradient(rgba(0, 0, 0, 0.75), rgba(0, 0, 0, 0.75)), url('{url}')",
                "background_size": "cover",  # Ajustar el tamaño de fondo
                "background_position": "center center",  # Centrar la imagen de fondo
                "position": "relative",
                "z_index": "0"  # Fondo detrás del texto
            },
            width="100%",
            height="30em",
            display="flex",
            spacing="4",
            padding_x=["1em", "3em"],
            padding_y=["5.5em", "10em"],
        ),
        size="4"
    )
