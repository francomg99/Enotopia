import reflex as rx
from Eno.styles.styles import Size
from Eno.components.title import title
from Eno.components.blog import blog

def blog_desktop() -> rx.Component:
    return rx.vstack(
             rx.box(
                title("BLOG"),
                        padding_left=Size.BIG.value,
                        width="100%"
                    ),
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
            
            
    