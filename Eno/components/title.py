import reflex as rx
import Eno.styles.styles as styles
from Eno.styles.styles import Size

def title(text: str) -> rx.Component:
    return rx.heading(
        rx.center(
            rx.text(text),        
            ),
            align="left",
            padding_top=[Size.MEDIUM.value, Size.MEDIUM.value],
            padding_bottom=[Size.MEDIUM.value],
            style=styles.title_style,
            width="100%"
            )
    
def others_titles(text: str) -> rx.Component:
    return rx.heading(
        rx.center(
            rx.text(text),        
            ),
            align="left",
            padding_top=["0em",Size.SMALL.value],
            padding_bottom=["0em","0.3em"],
            style=styles.subtitles,
            width="100%"
            )    
    