import reflex as rx
from Eno.styles.styles import Size, Color

def icon_link (text:str, url:str) -> rx.Component:
    return rx.link(
                rx.icon(
                    text,
                    _hover={
                        "color": Color.PRIMARY.value
                    }                                
                ),
                href=url,
                is_external=True,
                margin_top=Size.SMALL.value,
                color=Color.SECONDARY.value
            )