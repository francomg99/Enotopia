import reflex as rx
import Eno.styles.styles as styles
from Eno.styles.styles import Size, TextColor

def caracteristicas(title, text, title1, text1, title2, text2, src):
    text_style = {
        'color': TextColor.PRIMARY.value,
        'font_size': Size.LETTER.value,
        'text_align': 'justify',
        'margin_top': '0.5em',
    }

    return rx.heading(
        rx.box(
            # Contenedor principal
            rx.box(
                # Bloque 1: Izquierda
                rx.box(
                    rx.text(
                        title,
                        as_="div",
                        style=styles.subtitles
                    ),
                    rx.text(
                        text,
                        weight="light",
                        style=text_style,
                        width=["100%", "33%"],  # Ancho responsivo
                    ),
                    style={
                        "margin_bottom": ["2em", "0"],  # Espacio vertical en móviles
                        "z_index": "1"
                    }
                ),
                # Bloque 2: Centro derecha
                rx.box(
                    rx.text(
                        title1,
                        as_="div",
                        style=styles.subtitles
                    ),
                    rx.text(
                        text1,
                        align="right",
                        weight="light",
                        style={**text_style, 'text_align': 'justify'},
                        width=["100%", "35%"],  # Ancho responsivo
                    ),
                    style={
                        "margin_bottom": ["2em", "0"],  # Espacio vertical en móviles
                        "z_index": "1"
                    }
                ),
                # Bloque 3: Abajo izquierda
                rx.box(
                    rx.heading(
                        title2,
                        as_="div",
                        style=styles.subtitles
                    ),
                    rx.text(
                        text2,
                        weight="light",
                        style=text_style,
                        width=["100%", "33%"],  # Ancho responsivo
                    ),
                    style={
                        "z_index": "1"
                    }
                ),
                style={
                    "background": f"linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), url('{src}')",
                    "background_size": "cover",  # Ajustar el tamaño de fondo
                    "background_position": "center",  # Centrar la imagen de fondo
                    "position": "relative",
                    "z_index": "0",  # Fondo detrás del texto
                    "flex_direction": ["column", "row"],  # Vertical en móvil, horizontal en escritorio
                },
                width="100%",
                height=["50em", "30em"],  # Altura responsivo
                display="flex",
                spacing="4",
                padding_x=["1em", "3em"],  # Padding responsivo
                padding_y=["2em", "10em"],  # Padding responsivo
                justify_content="space-between",  # Espaciado entre elementos
                align_items="center"  # Alineación de elementos
            ),
        ),
        size="4"
    )
