import reflex as rx
from Eno.styles.styles import Size, TextColor, Color
from Eno.components.title import title, others_titles
from reflex_image_zoom import ImageZoom

def enotopia_desktop() -> rx.Component:
    return rx.tablet_and_desktop(
                rx.vstack(
                title("ENOTOPÍA"),
            rx.chakra.responsive_grid(
            rx.box(
                rx.vstack(
                rx.box(
                rx.text(
                    """Mi nombre es""", 
                    rx.text.strong(rx.text.em(" Valentina "), color=TextColor.SECONDARY.value), 
                    """y soy una apasionada del turismo enológico en la hermosa provincia de Mendoza, 
                    conocida como la capital internacional del vino. Desde pequeña he sido testigo del encanto y 
                    la riqueza cultural que esta tierra ofrece a sus visitantes, y es por eso que decidí dedicarme 
                    a compartir esta experiencia con el mundo.""",
                ),
                rx.text(
                    """Como gestora de turismo y fundadora de""", 
                    rx.text.strong(rx.text.em(" Enotopía, "), color=TextColor.SECONDARY.value),
                    """una agencia dio sus primeros pasos en 2024, mi misión es ofrecer a los turistas 
                    una experiencia inolvidable que combine la belleza de nuestros paisajes con la excelencia de nuestros vinos. 
                    Desde la organización de recorridos por las principales bodegas hasta la gestión de guías especializados, 
                    cada detalle está pensado para sumergir a nuestros visitantes en la cultura vitivinícola de Mendoza.""",
                ),
                rx.text(
                    """En""", 
                    rx.text.strong(rx.text.em(" Enotopía, "), color=TextColor.SECONDARY.value), 
                    """nuestro objetivo es convertirnos en el punto de referencia para todos aquellos que deseen descubrir los secretos 
                    de esta tierra bendecida por el sol y el buen vino. Con pasión, dedicación y un profundo amor por nuestra provincia, 
                    estamos seguros de que cada viaje con nosotros será una experiencia única e inolvidable. ¡Bienvenidos a Enotopía, 
                    donde los viajes se encuentran con el vino!"""
                ),                
                padding_left=[Size.SMALL.value, Size.VERY_BIG.value],
                padding_right=[Size.SMALL.value, Size.ZERO.value],
                padding_bottom="0.2em",
               # widht="100%",            
                style={
                    "text_indent": Size.DEFAULT.value,
                    "font_size": Size.LETTER.value,
                    'text_align': 'justify'
                }
                )
        )
            ),
                rx.box(
                rx.image(
                    src="/vale1.jpg",
                    alt="Valentina Martínez, fundadora de Enotopía",
                    widht="98%",
                    height=["auto","auto"],
                    align="right",
                    padding_top="10px",
                    padding_right=Size.VERY_BIG.value,
                    padding_left=[Size.SMALL.value, Size.BIG.value],
                )
            ),
            columns=[1,2],
            widht="100%"
            )
            )
    )

def enotopia_mobile() -> rx.Component:
    return rx.mobile_only(         
                title("ENOTOPÍA"),
            rx.chakra.responsive_grid(
            rx.box(
                rx.vstack(
                rx.box(
                rx.text(
                    """Mi nombre es""", 
                    rx.text.strong(rx.text.em(" Valentina "), color=TextColor.SECONDARY.value), 
                    """y soy una apasionada del turismo enológico en la hermosa provincia de Mendoza, 
                    conocida como la capital internacional del vino. Desde pequeña he sido testigo del encanto y 
                    la riqueza cultural que esta tierra ofrece a sus visitantes, y es por eso que decidí dedicarme 
                    a compartir esta experiencia con el mundo.""",
                ),
                rx.dialog.root(
                    rx.dialog.trigger(
                        rx.chakra.button(
                                "Ver más", 
                                margin_top=Size.MEDIUM.value,
                                margin_bottom=Size.MEDIUM.value,
                                style={
                                    "background":Color.TERTIARY.value,
                                    "color":TextColor.PRIMARY.value,
                                    "borderRadius": "20px"
                                    },
                                _hover={
                                    "background": Color.PRIMARY.value,
                                    "color": TextColor.SECONDARY.value
                                },  
                            ),
                        ),
                    rx.dialog.content(
                        rx.dialog.title(others_titles("Sobre mí!")),
                        rx.dialog.description(
                            """Como gestora de turismo y fundadora de""", 
                            rx.text.strong(rx.text.em(" Enotopía, "), color=TextColor.SECONDARY.value),
                            """mi misión es ofrecer a los turistas 
                            una experiencia inolvidable que combine la belleza de nuestros paisajes con la excelencia de nuestros vinos. 
                            Organizando recorridos por las principales bodegas y gestionando guías especializadas, 
                            cada detalle está pensado para sumergir a nuestros visitantes en la cultura vitivinícola de Mendoza.""",
                        ),
                        rx.dialog.description(
                            """nuestro objetivo es convertirnos en el punto de referencia para todos aquellos que deseen descubrir los secretos 
                            de esta tierra bendecida por el sol y el buen vino. Con pasión, dedicación y un profundo amor por nuestra provincia, 
                            estamos seguros de que cada viaje con nosotros será una experiencia única e inolvidable. ¡Bienvenidos a Enotopía, 
                            donde los viajes se encuentran con el vino!""",
                        ),                    
                        rx.dialog.close(
                            rx.chakra.button(
                                "Cerrar", 
                                margin_top=Size.MEDIUM.value,
                                style={
                                    "background":Color.TERTIARY.value,
                                    "color":TextColor.PRIMARY.value,
                                    "borderRadius": "20px"
                                    },
                                _hover={
                                    "background": Color.PRIMARY.value,
                                    "color": TextColor.SECONDARY.value
                                },  
                            ),
                        ),
                        bg="#431E2C",
                        color=TextColor.PRIMARY.value,
                        border=f"2px solid {Color.ACCENT.value}",
                        style={
                            'text_indent':"1em",
                            'text_align': 'justify'
                        }
                    ),
                ),               
                padding_left=[Size.SMALL.value, Size.VERY_BIG.value],
                padding_right=[Size.SMALL.value, Size.ZERO.value],
                padding_bottom="0.2em",
               # widht="100%",            
                style={
                    "text_indent": Size.DEFAULT.value,
                    "font_size": Size.LETTER.value
                }
                )
        )
            ),
                rx.box(
                rx.image(
                    src="/vale1.jpg",
                    alt="Valentina Martínez, fundadora de Enotopía",
                    widht="98%",
                    height=["auto","auto"],
                    align="right",
                    padding_top="10px",
                    padding_right=[Size.SMALL.value, Size.VERY_BIG.value],
                    padding_left=[Size.SMALL.value, Size.BIG.value],
                )
            ),
            columns=[1,2],
            widht="100%"
            )
            )
    