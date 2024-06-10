import reflex as rx
from Eno.styles.styles import Color, TextColor, Size

def button (text:str, tag:str, url:str) -> rx.Component:
    return rx.chakra.button(
        text,
        rx.chakra.icon(
            tag=tag
        ),   
        on_click=rx.redirect(url, external=True),
            style={
                "background":TextColor.SECONDARY.value,
                "color":TextColor.ACCENT.value,
                },
            _hover={
                "background": Color.PRIMARY.value,
                "color": Color.PRIMARY.value
            },  
            size="lg",
            margin_left=Size.BIG.value,
    )
    
def other_button (text:str, url:str) -> rx.Component:
    return rx.chakra.button(
        text,   
        on_click=rx.redirect(url, external=True),
            style={
                "background":Color.TERTIARY.value,
                "color":TextColor.PRIMARY.value,
                "borderRadius": "20px"
                },
            _hover={
                "background": Color.PRIMARY.value,
                "color": TextColor.SECONDARY.value
            },  
            size="md",
            margin=Size.SMALL.value
    )