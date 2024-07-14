import reflex as rx
from Eno.components.porcentaje import porcentajes
from Eno.styles.styles import Size
import Eno.styles.styles as styles

def vinos(text, src, data1, text1, src1, data2, text2, src2, data3):
    return rx.hstack(
        rx.vstack(
            rx.text(text, style=styles.other_titles),
            rx.image(src=src, width=["5em", "100px"], height="auto"),
            porcentajes(data1),
            align_items="center",
            justify_content="center"
        ),
        rx.vstack(
            rx.text(text1, style=styles.other_titles),
            rx.image(src=src1, width=["5em", "100px"], height="auto"),
            porcentajes(data2),
            align_items="center",
            justify_content="center"
        ),
        rx.vstack(
            rx.text(text2, style=styles.other_titles),
            rx.image(src=src2, width=["5em", "100px"], height="auto"),
            porcentajes(data3),
            align_items="center",
            justify_content="center"
        ),
        justify_content="space-around",
        align_items="center",
        flex_direction=["column", "row"]  # Vertical en móvil y horizontal en escritorio
    )
