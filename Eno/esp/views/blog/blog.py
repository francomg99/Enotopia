import reflex as rx
from Eno.styles.styles import Size
from Eno.styles.styles import Size
from Eno.styles.fonts import Font
from Eno.styles.colors import TextColor
from Eno.components.carrusel_blog import carousel_title
from Eno.components.wine_line import other_line
from Eno.components.blog import blog

def wine_blog() -> rx.Component:
    return rx.box(
        carousel_title("BLOG", "/blog.jpg", "center bottom"),
        rx.vstack(
                rx.text(
                    """
                    ¡Bienvenidos a la tierra del vino en Mendoza! En nuestra región, cada terruño cuenta una historia única, 
                    reflejada en los vinos que producimos. Explora y vive con nosotros los distintos terroirs que hacen de Mendoza un 
                    destino vinícola de renombre mundial.""",
                    padding_top=["1.5em", Size.BIG.value],
                    padding_right=[Size.SMALL.value, Size.VERY_BIG.value],
                    padding_left=[Size.SMALL.value, Size.VERY_BIG.value],
                    padding_bottom=["1.5em", Size.BIG.value],
                    style={
                        "font_size": Size.LETTER.value,
                        'text_align': 'justify'
                        }
                ),
            rx.box(
                rx.center(
                    "• Explora los Terroirs de Mendoza •", 
                    align="center", 
                    size="6", 
                    as_="div",
                    color=TextColor.PRIMARY.value,
                    font_family=Font.TITLE.value,
                    style={
                        'font_size': ["1.75em", "3em"]
                    }
                ),           
                style={
                    "background": f"linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('/racimo.jpeg')",
                    "background_size": "cover", 
                    "background_position": "center center", 
                    "padding": "20px",
                    "position": "relative",
                    "z_index": "0", 
                },                
                display="flex", 
                justify_content="center", 
                align_items="center",  
                spacing="4",
                width="100%",
                height=["3em", "10em"],
                padding_x="1em",
                padding_y=["3em", "3em"],
                top="0"
            )
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
                    'font_size':["1.75em","3em"]
                }
            ),           
                style={
                    "background": f"linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('/servir.jpeg')",
                    "background_size": "cover", 
                    "background_position": "center center", 
                    "padding": "20px",
                    "position": "relative",
                    "z_index": "0", 
                },                
                display="flex", 
                justify_content="center", 
                align_items="center",  
                spacing="4",
                width="100%",
                height=["3em", "10em"],
                padding_x="1em",
                padding_y=["3em", "3em"],
                top="0"
            )
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
            
    
