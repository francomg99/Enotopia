import reflex as rx
from Eno.styles.styles import Color

def wine_line() -> rx.Component:
    return rx.divider(
        height=["3em","6em"],
        bg=Color.ACCENT.value
    )
    
def other_line() -> rx.Component:
    return rx.divider(
        height=["1.1em","4em"],
        bg=Color.ACCENT.value
    )

def footer_line() -> rx.Component:
    return rx.divider(
        height=["1em","4em"],
        bg=Color.CUARTIARY.value
    )