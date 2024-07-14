import reflex as rx
from Eno.styles.styles import Size

import reflex as rx

def footer_desktop() -> rx.Component:
    return rx.tablet_and_desktop(
        rx.center(
            rx.image(
                src="/enotopia.png",
                alt="Logo de Enotopia, palabra encerrada en las esquinas",
                width="15em"
            ),
            rx.text(
                "©Hermes Dev | Franco Martínez",
                color="#828282"
            ),
            style={
                "background": "linear-gradient(to bottom, #532135, #3E1A28)",
                "padding": "0.1em", 
            },
            width="100%",  
        )
    )

    
def footer_mobile()->rx.Component:
    return rx.mobile_only(
                rx.vstack(
                        rx.image(
                            src="/enotopia.png",
                            alt="Logo de Enotopia, palabra encerrada en las esquinas",
                            width="10em"
                        ),
                        rx.link(
                        "©Hermes Dev | Franco Martínez",
                            href="https://hermesdev.es",
                            is_external=True,
                            margin="1em",
                            color="#828282",
                            style={'font_size':Size.MEDIUM.value}
                        ),
                style={
                "background": "linear-gradient(to bottom, #532135, #3E1A28)", 
                "padding": "1em",  
            },                    
                witdh="60%",
                align="center",
                )
            )    