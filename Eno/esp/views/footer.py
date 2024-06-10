import reflex as rx
from Eno.styles.styles import Size

def footer_desktop()->rx.Component:
    return rx.tablet_and_desktop(
                rx.center(
                rx.image(
                    src="/enotopia.png",
                    alt="Logo de Enotopia, palabra encerrada en las esquinas",
                    width="20em"
                ),
                rx.text(
                    "©Pagina creada por Franco Martínez - Reflex | Python",
                    color="#828282"
                )
            )
            )
def footer_mobile()->rx.Component:
    return rx.mobile_only(
                rx.vstack(
                        rx.image(
                            src="/enotopia.png",
                            alt="Logo de Enotopia, palabra encerrada en las esquinas",
                            width=["13em","20em"]
                        ),
                        rx.link(
                            "©Pagina creada por Franco Martínez - Reflex | Python",
                            href="https://hermesdev.es",
                            is_external=True,
                            margin="1em",
                            color="#828282",
                            style={'font_size':Size.MEDIUM.value}
                        ),
                    witdh="60%",
                    align="center",
                )
            )    