import reflex as rx
from Eno.styles.styles import Size, Font, TextColor
from Eno.components.title import title, others_titles
from Eno.components.wine_line import wine_line
from Eno.components.carrusel import que_ofrecemos
import Eno.styles.styles as styles

def quienes_somos_desktop()->rx.Component:
    return rx.tablet_and_desktop(
                rx.vstack( 
                    title("¿QUIÉNES SOMOS?"),
                rx.text(
                    """
                    Somos una agencia especializada en ofrecer experiencias auténticas y enriquecedoras en el mundo del vino. 
                    Desde visitas a bodegas familiares hasta recorridos por viñedos pintorescos, nuestro objetivo es sumergir a 
                    nuestros clientes en la cultura del vino de una manera inolvidable.
                    Como apasionados del turismo y amantes del vino, hemos combinado nuestras dos pasiones para ofrecerles 
                    una experiencia única y memorable.""",
                    padding_right=[Size.VERY_BIG.value],
                    padding_left=Size.VERY_BIG.value,
                    padding_bottom=Size.SMALL.value,
                    style={
                        "font_size": Size.LETTER.value,
                        'text_align': 'justify'
                        }
                ),
                rx.chakra.responsive_grid(
                    rx.box(
                        rx.image(
                            src="/cava_salentein.jpg",
                            alt="Imagén en montaña de Bodegas Salentein",
                            widht="98%",
                            height=["auto","auto"],
                            align="right",
                            padding_top="10px",
                            padding_left=Size.VERY_BIG.value,
                            padding_right=[Size.BIG.value],
                        )
                    ),
                    rx.box(
                        rx.vstack(
                            rx.box(
                                others_titles(
                                "¿Por qué elegirnos?"
                                ),
                            ),
                        rx.text.strong(
                            "• Descubre el Encanto y la Historia del Vino con Nosotros •",
                            style={
                                'width':"100%",
                                "font_size":["1.8em", Size.BIG.value],
                                "font_family":Font.TITLE.value,
                                "color":TextColor.PRIMARY.value,
                                "text_align": 'left'  
                            }
                        ),
                        rx.box(
                            rx.text(
                                """Nuestro equipo esta compuesto por expertos ecoturísticos apasionados por compartir su amor por el vinos y la cultura vitivinícola."""
                            ),
                            rx.text(
                            """Nos esforzamos por crear experiencias a medida para cada clientes, asegurando que cada visita sea única y memorable. Gracias a nuestras
                            sólidas relaciones con bodegas locales y productos de vino, podemos ofrecer a nuestros clientes acceso exclusivo a lugares y experiencias
                            que no encontrarán en ningún otro lugar."""  
                            ),                
                            padding_right=[Size.VERY_BIG.value],
                            padding_left=[Size.ZERO.value],
                            padding_bottom="0.2em",
                            style={
                                'text_align': 'justify',
                                "font_size": Size.LETTER.value
                            }
                        )
                        ),
                    wine_line()
                ),
                columns=[1,2],
                widht="100%"
                ),
                rx.box(
                    rx.vstack(
                        rx.box(
                            others_titles(
                                "¿Qué ofrecemos?"
                            )
                        ),
                        que_ofrecemos(),                                 
                        padding_left=[Size.VERY_BIG.value],
                        padding_right=[Size.ZERO.value],
                        padding_bottom="0.2em",
                        style={
                            "font_size": Size.LETTER.value
                        }
                    ),
                    width="100%",
                ),
                )
            )

def quienes_somos_mobile()->rx.Component:
    return rx.mobile_only(
                rx.vstack( 
                    title("¿QUIÉNES SOMOS?"),
                rx.text(
                    """
                Somos una agencia especializada en ofrecer experiencias auténticas y enriquecedoras en el mundo del vino. 
                Desde visitas a bodegas familiares hasta recorridos por viñedos pintorescos, nuestro objetivo es sumergir a nuestros
                clientes en la cultura del vino de una manera inolvidable.
                Como apasionados del turismo y amantes del vino, hemos combinado nuestras dos pasiones para ofrecerles 
                una experiencia única y memorable.""",
                    padding_right=[Size.SMALL.value],
                    padding_left=Size.SMALL.value,
                    padding_bottom=Size.SMALL.value,
                    style={
                        "font_size": Size.LETTER.value,
                        'text_align': 'justify'
                        }
                ),
                rx.chakra.responsive_grid(
                    rx.box(
                        rx.image(
                            src="/cava_salentein.jpg",
                            alt="Imagén en montaña de Bodegas Salentein",
                            widht="98%",
                            height=["auto","auto"],
                            align="right",
                            padding_left=Size.SMALL.value,
                            padding_right=Size.SMALL.value,
                            padding_top=Size.SMALL.value
                        )
                    ),
                    wine_line(),
                    rx.box(
                        rx.vstack(
                            rx.box(
                                others_titles(
                                "¿Por qué elegirnos?"
                            ),
                        rx.center(
                            rx.text.strong(
                            "• Descubre el Encanto y la Historia del Vino con Nosotros •",
                            style=styles.other_titles,
                            padding_left=Size.SMALL.value,
                            padding_right=Size.SMALL.value,
                            padding_top=Size.MEDIUM.value,
                            paddin_bottom=Size.MEDIUM.value
                            )
                        )
                            ),
                    rx.box(
                        rx.text(
                            """Nuestro equipo esta compuesto por expertos ecoturísticos apasionados por compartir su amor por el vinos y la cultura vitivinícola."""
                        ),
                        rx.text(
                        """Nos esforzamos por crear experiencias a medida para cada clientes, asegurando que cada visita sea única y memorable. Gracias a nuestras
                        sólidas relaciones con bodegas locales y productos de vino, podemos ofrecer a nuestros clientes acceso exclusivo a lugares y experiencias
                        que no encontrarán en ningún otro lugar."""  
                        ),                
                        padding_right=[Size.SMALL.value],
                        padding_left=[Size.SMALL.value],
                        style={
                            'text_indent':"0.5 em",
                            "font_size": Size.LETTER.value,
                            'text_align': 'justify'
                        }
                    )
                        ),
                wine_line()
            ),
            rx.box(
                rx.vstack(
                rx.box(
                others_titles(
                    "¿Qué ofrecemos?"
            
                ),
                rx.box(
                #que_ofrecemos(),                                 
                style={
                    "font_size": Size.LETTER.value,
                    'text_indent':"0.5 em",
                    'text_align': 'justify'
                }
                )
                )
        )
            ),
            columns=[1,2],
            widht="100%",
            padding_left=Size.SMALL.value,
            padding_right=Size.SMALL.value
            )
            )
    )
