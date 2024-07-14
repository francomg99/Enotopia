import reflex as rx
from Eno.styles.styles import Size, Color, TextColor
from Eno.components.button import other_button
from Eno.components.title import title

def foto_ig()-> rx.Component:
    return rx.center(
            rx.vstack(
                title("INSTAGRAM"),
                rx.box(
                    rx.avatar(
                        name="Enotopía",
                        size="9",
                        src="/enotopia_amarillo.png",
                        radius="full",
                        color=TextColor.SECONDARY.value,
                        bg=Color.ACCENT.value,
                        border=f"4px solid {Color.CUARTIARY.value}",
                        _hover={
                            "opacity": 0.8,
                        }
                    ),
                padding=Size.DEFAULT.value,
                position="relative"
                ),
                rx.vstack(
                    rx.heading(
                        "Enotopía",
                        size="8",
                        color=TextColor.SECONDARY.value
                    ),
                    rx.text.strong(
                        "@enotopia_",
                        margin_top="0.2em",
                        color=Color.PRIMARY.value,
                        style={'font_size':Size.LETTER.value}
                    ),
                    rx.hstack(
                        other_button(
                            "Seguir",
                            "https://www.instagram.com/enotopia_/"
                        )
                    ),
                spacing="0",
                align_items="center"                        
                ),
            align="center",
            spacing="0"
            )
    )