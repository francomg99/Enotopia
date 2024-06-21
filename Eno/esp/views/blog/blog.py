import reflex as rx
from Eno.styles.styles import Size
from Eno.styles.styles import Size
from Eno.styles.fonts import Font
from Eno.styles.colors import TextColor
from Eno.components.carrusel_blog import carousel_title
from Eno.components.wine_line import other_line
from Eno.components.blog import blog, mobile_blog

def blog_desktop() -> rx.Component:
    return rx.tablet_and_desktop(
        carousel_title("BLOG", "/blog.jpg", "center bottom"),
        rx.vstack(
                rx.text(
                    """
                    ¡Bienvenidos a la tierra del vino en Mendoza! En nuestra región, cada terruño cuenta una historia única, 
                    reflejada en los vinos que producimos. Explora y vive con nosotros los distintos terroirs que hacen de Mendoza un 
                    destino vinícola de renombre mundial.""",
                    padding_top=Size.BIG.value,
                    padding_right=[Size.VERY_BIG.value],
                    padding_left=Size.VERY_BIG.value,
                    padding_bottom=Size.BIG.value,
                    style={
                        "font_size": Size.LETTER.value
                        }
                ),
            rx.box(
            rx.center(
                "• Explora los Diversos Terroirs de Mendoza: Luján de Cuyo, Maipú y Valle de Uco •", 
                align="center", 
                size="6", 
                as_="div",
                color=TextColor.PRIMARY.value,
                font_family=Font.TITLE.value,
                style={
                    'font_size':["1em","3em"]
                }
            ),           
                bg="center/cover url('/copa2.jpg')",
                align_items="center",
                spacing="4",
                width="100%",
                height=["25em","10em"],
                padding_x="3em",
                padding_y=["5em","3em"],
                top="0"
                ),
                ),
                rx.vstack(
                    rx.vstack(
                        blog(
                            "/lujan_de_cuyo.png",
                            """ Conocido como el corazón histórico de la viticultura mendocina, Luján de Cuyo también llamada 
                            “Primera zona” ofrece una combinación perfecta de altitud, diversos perfiles de suelos y un clima 
                            óptimo para el cultivo de la vid. Las bodegas de renombre internacional, el río Mendoza y los viñedos 
                            centenarios aquí dan lugar a vinos de carácter profundo y elegante, especialmente Malbec, 
                            la cepa insignia de la región.""",
                            "/blog/lujan_de_cuyo"  
                            ),
                        blog(
                            "/maipu.png",
                            """Este distrito vitivinícola es la cuna de algunas de las bodegas más antiguas de Mendoza. 
                            Maipu, además se caracteriza por sus Olivicolas, entre ellas:
                            Olivícola Laur es una reconocida empresa ubicada en la región de Maipú, 
                            en la provincia de Mendoza, Argentina. 
                            Especializada en la producción de aceite de oliva de alta calidad, 
                            Olivicola Laur ha establecido una sólida reputación por su compromiso con la excelencia y la tradición.""",
                            "/blog/maipu"  
                            ),
                        blog(
                            "/valle_de_uco.png",
                            """Elevándose majestuosamente en la cordillera de los Andes, el Valle de Uco es un 
                            paraíso para los amantes del vino en busca de aventuras enológicas. Con sus diversos 
                            distritos cada vez con mayor expansion vitivinícola, altitudes extremas que alcanzan los 1700 
                            metros sobre el nivel del mar y suelos aluviales únicos, este valle produce vinos de carácter 
                            fresco y vibrante, con una expresión única de suelos, el clima y el agua. Aquí, variedades como 
                            el Malbec, el Cabernet Sauvignon y el Chardonnay encuentran su máxima expresión, atrayendo a 
                            enófilos de todo el mundo.""",
                            "/blog/valle_de_uco"  
                            ),
                width="100%",   
            ), 
            other_line(),
            rx.box(
            rx.center(
                "• CONSEJOS PARA TU VISITA A MENDOZA •", 
                align="center", 
                size="6", 
                as_="div",
                color=TextColor.PRIMARY.value,
                font_family=Font.TITLE.value,
                style={
                    'font_size':["1em","3em"]
                }
            ),           
                bg="center/cover url('/ruca.jpg')",
                align_items="center",
                spacing="4",
                width="100%",
                height=["25em","10em"],
                padding_x="3em",
                padding_y=["5em","3em"],
                top="0"
                ),
                    other_line(),
                    rx.vstack(  
                    rx.vstack(
                        blog(
                            "/maridar.png",
                            """Puede significar una mejora en la experiencia gastronómica, por ejemplo los vinos tintos son geniales 
                            con carnes, los blancos van bien con pescados y aves, 
                            y los rosados son versátiles y van con una variedad de platos ligeros. 
                            Experimenta para encontrar tus combinaciones favoritas.""",
                            "/blog/maridar"  
                            ),
                        blog(
                            "/cinco_bodegas.png",
                            """Cinco opciones excelentes incluyen Catena Zapata, 
                            reconocido por su carácter y complejidad; Enemigo, destacado por su elegancia y potencia; Luigi 
                            Bosca, emblemático y estructurado; Zuccardi, con una amplia variedad que va desde frescos hasta 
                            complejos; y Bianchi, accesible y consistente.""",
                            "/blog/bodegas"  
                            ),
                        )
                    ),
                width="100%",      
            ),             
            )
    
def blog_mobile() -> rx.Component:
    return rx.mobile_only(
        carousel_title("BLOG", "maridar.jpeg", "center center"),
        rx.vstack(
            rx.box(
        rx.center(
            "• Explora los Diversos Terroirs de Mendoza: Luján de Cuyo, Maipú y Valle de Uco •", 
            align="center", 
            size="6", 
            as_="div",
            color=TextColor.PRIMARY.value,  # Ejemplo de uso de variable CSS para el color
            font_family=Font.TITLE.value,
            padding_top="0.1em",
            style={
                'font_size':["1.8em","3em"],
                'text_align': 'center',  # Asegura que el texto esté centrado
            }
        ),           
        # Estilos aplicados al contenedor para agregar la imagen de fondo
        style={
            'background': "center/cover url('/copa2.jpg') no-repeat",
            'align_items': 'center',
            'width': "100%",
            'height': ["8.1em","10em"],
        }
    )
        ),
        rx.text(
            rx.text.strong("""
            ¡Bienvenidos a la tierra del vino en Mendoza!"""),""" En nuestra región, cada terruño cuenta una historia única, 
            reflejada en los vinos que producimos. Explora y vive con nosotros los distintos terroirs que hacen de Mendoza un 
            destino vinícola de renombre mundial.""",
            padding_top=Size.BIG.value,
            padding_right=[Size.SMALL.value],
            padding_left=Size.SMALL.value,
            padding_bottom=Size.BIG.value,
            style={
                "font_size": Size.LETTER.value,
                'text_align': 'justify'
                }
                ),
                rx.vstack(
                    rx.vstack(
                        mobile_blog(
                            "/lujan_de_cuyo.png",
                            """ Conocido como el corazón histórico de la viticultura mendocina, Luján de Cuyo también llamada 
                            “Primera zona” ofrece una combinación perfecta de altitud, diversos perfiles de suelos y un clima 
                            óptimo para el cultivo de la vid. Las bodegas de renombre internacional, el río Mendoza y los viñedos 
                            centenarios aquí dan lugar a vinos de carácter profundo y elegante, especialmente Malbec, 
                            la cepa insignia de la región.""",
                            "/blog/lujan_de_cuyo"  
                            ),
                        mobile_blog(
                            "/maipu.png",
                            """Este distrito vitivinícola es la cuna de algunas de las bodegas más antiguas de Mendoza. 
                            Maipu, además se caracteriza por sus Olivicolas, entre ellas:
                            Olivícola Laur es una reconocida empresa ubicada en la región de Maipú, 
                            en la provincia de Mendoza, Argentina. 
                            Especializada en la producción de aceite de oliva de alta calidad, 
                            Olivicola Laur ha establecido una sólida reputación por su compromiso con la excelencia y la tradición.""",
                            "/blog/maipu"  
                            ),
                        mobile_blog(
                            "/valle_de_uco.png",
                            """Elevándose majestuosamente en la cordillera de los Andes, el Valle de Uco es un 
                            paraíso para los amantes del vino en busca de aventuras enológicas. Con sus diversos 
                            distritos cada vez con mayor expansion vitivinícola, altitudes extremas que alcanzan los 1700 
                            metros sobre el nivel del mar y suelos aluviales únicos, este valle produce vinos de carácter 
                            fresco y vibrante, con una expresión única de suelos, el clima y el agua. Aquí, variedades como 
                            el Malbec, el Cabernet Sauvignon y el Chardonnay encuentran su máxima expresión, atrayendo a 
                            enófilos de todo el mundo.""",
                            "/blog/valle_de_uco"  
                            ),
                width="100%",   
            ), 
            other_line(),
            rx.box(
            rx.center(
                "• CONSEJOS PARA TU VISITA A MENDOZA •", 
            align="center", 
            size="6", 
            as_="div",
            color=TextColor.PRIMARY.value,  # Ejemplo de uso de variable CSS para el color
            font_family=Font.TITLE.value,
            #margin_top="1em",
            padding="1em",
            style={
                'font_size':["1.8em","3em"],
                'text_align': 'center',  # Asegura que el texto esté centrado
            }
        ),           
        # Estilos aplicados al contenedor para agregar la imagen de fondo
        style={
            'background': "center/cover url('/ruca.jpg') no-repeat",
            'align_items': 'center',
            'width': "100%",
            'height': ["8.1em","10em"],
        }
    ),
                    other_line(),
                    rx.vstack(  
                    rx.vstack(
                        mobile_blog(
                            "/maridar.png",
                            """Puede significar una mejora en la experiencia gastronómica, por ejemplo los vinos tintos son geniales 
                            con carnes, los blancos van bien con pescados y aves, 
                            y los rosados son versátiles y van con una variedad de platos ligeros. 
                            Experimenta para encontrar tus combinaciones favoritas.""",
                            "/blog/maridar"  
                            ),
                        mobile_blog(
                            "/cinco_bodegas.png",
                            """Cinco opciones excelentes incluyen Catena Zapata, 
                            reconocido por su carácter y complejidad; Enemigo, destacado por su elegancia y potencia; Luigi 
                            Bosca, emblemático y estructurado; Zuccardi, con una amplia variedad que va desde frescos hasta 
                            complejos; y Bianchi, accesible y consistente.""",
                            "/blog/bodegas"  
                            ),
                        )
                    ),
                width="100%",      
            ),             
            )
        
    
    