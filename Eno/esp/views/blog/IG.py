import reflex as rx
from Eno.esp.views.navbar import navbar
from Eno.esp.views.footer import footer_desktop
from Eno.components.carrusel_blog import carousel_title, slick
from Eno.components.title import title
from Eno.components.wine_line import footer_line, other_line
from Eno.esp.views.footer import footer_desktop, footer_mobile
from Eno.components.ind_geo import ind_geo
from Eno.styles.styles import Size
import Eno.styles.styles as styles

@rx.page(
    route="/blog/bodegas", 
    title="Bodegas | Enotopía",
    description="Página de \"Bodegas\" de Enotopía"
)
def indicacion_geo():
    text_style={
        "font_size": Size.LETTER.value,
        'text_align': 'justify'
    }
    
    return rx.box(
            navbar(),
            slick(
                carousel_title("IG", "/viñas1.jpg", "center center"),
                carousel_title("IG", "/viñas2.jpg", "center center"),
                carousel_title("IG", "/viñas3.jpg", "center center")
            ),
            title("¿Qué son las IG?"),                 
            rx.text(
                """
                Las Indicaciones Geográficas (IG) son una faceta fascinante y a menudo desconocida del mundo de la protección de productos regionales. Este sistema no solo protege contra la falsificación y el uso indebido de nombres geográficos, sino que también tiene aspectos curiosos y únicos:""",
                padding_top=["0em",Size.MEDIUM.value],
                padding_right=[Size.SMALL, Size.VERY_BIG.value],
                padding_left=[Size.SMALL, Size.VERY_BIG.value],
                padding_bottom=Size.SMALL.value,
                style=text_style
            ),  
            rx.text(
                rx.text.strong("• Orígenes en el Vino:", font_size=Size.DEFAULT.value),
                """
                Las IG comenzaron originalmente en la industria del vino en Europa como una forma de proteger las denominaciones de origen como Champagne, Chianti, y Porto. Esto aseguró que solo los vinos producidos en esas regiones específicas pudieran llevar esos nombres.""",
                padding_right=[Size.SMALL, Size.VERY_BIG.value],
                padding_left=[Size.SMALL, Size.VERY_BIG.value],
                padding_bottom=Size.SMALL.value,
                style=text_style
            ),             
            rx.text(
                rx.text.strong("৹ Protección de sabores: ", font_size=Size.DEFAULT.value),
                """
                En algunos casos, las IG no solo protegen nombres geográficos, sino también métodos tradicionales de producción y hasta ciertos perfiles de sabor característicos de un lugar.""",
                padding_right=[Size.SMALL, Size.VERY_BIG.value],
                padding_left=[Size.SMALL, Size.VERY_BIG.value],
                style=text_style
            ), 
            other_line(),
            ind_geo(
                "IG CHACAYES",
                "Los Chacayes, en el Valle de Uco, Mendoza, es una región vinícola famosa por sus vinos excepcionales. Situada a 1,100-1,500 metros sobre el nivel del mar, combina un clima con amplias variaciones térmicas y suelos aluvionales ideales para el cultivo de la vid. Esto resulta en vinos intensos y complejos.",
                "Las uvas principales son Malbec, Cabernet Sauvignon, Syrah, Merlot, Chardonnay y Sauvignon Blanc, destacando los Malbec por sus aromas a frutas rojas y negras, con toques especiados y florales. Reconocida oficialmente como IG en 2018, Los Chacayes es un destino imperdible para los amantes del vino, con bodegas que ofrecen tours, catas y experiencias gastronómicas únicas. Descubre los secretos detrás de algunos de los mejores vinos de Argentina.",
                "Bodega Piedra Negra, icóno de IG CHACAYES",
                "/piedranegra.gif"
            ), 
            other_line(),              
            rx.text(
                rx.text.strong("• Variedades Poco Conocidas: ", font_size=Size.DEFAULT.value),
                """
                Algunas IG protegen productos derivados de variedades de plantas o animales que son únicas de una región específica. Por ejemplo, el queso Roquefort en Francia se elabora con leche de ovejas de una raza particular y solo en ciertas cuevas de la región.""",
                padding_right=[Size.SMALL, Size.VERY_BIG.value],
                padding_left=[Size.SMALL, Size.VERY_BIG.value],
                padding_bottom=Size.SMALL.value,
                style=text_style
            ),            
            rx.text(
                rx.text.strong("৹ Impacto Económico: ", font_size=Size.DEFAULT.value),
                """
                Las IG no solo protegen el patrimonio cultural y natural de una región, sino que también tienen un impacto significativo en la economía local al atraer turismo y valorizar los productos locales.""",
                padding_right=[Size.SMALL, Size.VERY_BIG.value],
                padding_left=[Size.SMALL, Size.VERY_BIG.value],
                style=text_style
            ),
            other_line(),
            ind_geo(
                "PARAJE ALTAMIRA",
                "Paraje Altamira, ubicado en el Valle de Uco de Mendoza, Argentina, es reconocido mundialmente por su excepcional terroir para la producción de vinos. Situado entre 1,000 y 1,200 metros sobre el nivel del mar, este paraje se distingue por sus suelos pedregosos y una altitud que proporciona condiciones óptimas para el cultivo de la vid.",
                "Principalmente conocido por sus Malbecs, Paraje Altamira produce vinos que destacan por su elegancia y complejidad. Los suelos aluviales y calcáreos junto con las variaciones térmicas diarias favorecen una maduración lenta y equilibrada de las uvas, resultando en vinos con aromas profundos a frutas maduras, notas florales y una estructura firme.",
                "Bodega Zuccardi, emblema de Paraje Altamira",
                "/zuccardi.gif"
            ),  
            other_line(),              
            rx.text(
                rx.text.strong("• Conflictos y Negociaciones Internacionales: ", font_size=Size.DEFAULT.value),
                """
               A nivel global, las negociaciones sobre IG pueden ser intensas y complejas, especialmente en acuerdos comerciales internacionales donde se discute la protección de denominaciones de origen frente a intereses comerciales más amplios.""",
                padding_right=[Size.SMALL, Size.VERY_BIG.value],
                padding_left=[Size.SMALL, Size.VERY_BIG.value],
                padding_bottom=Size.SMALL.value,
                style=text_style
            ),            
            rx.text(
                rx.text.strong("৹ Desafíos Tecnológicos: ", font_size=Size.DEFAULT.value),
                """
                Con el avance de la tecnología, la protección de las IG también debe adaptarse para prevenir el uso indebido en plataformas digitales y en el comercio electrónico global.""",
                padding_right=[Size.SMALL, Size.VERY_BIG.value],
                padding_left=[Size.SMALL, Size.VERY_BIG.value],
                style=text_style
            ), 
            other_line(),
            ind_geo(
                "LAS COMPUERTAS",
                "La Indicación Geográfica \"Las Compuertas\" en Luján de Cuyo, Mendoza, Argentina, es conocida por su excepcional terroir, caracterizado por su suelo pedregoso y un microclima favorable para el cultivo de uvas de alta calidad. Esto permite a los viticultores producir vinos únicos que reflejan la autenticidad y el carácter distintivo del lugar, destacándose por su estructura, complejidad y elegancia.",
                "La Indicación Geográfica \"Las Compuertas\" asegura la calidad y autenticidad de los vinos que llevan su nombre, fortaleciendo la reputación de los productores locales y atrayendo turistas interesados en explorar las bodegas y viñedos de la región. Este reconocimiento promueve el patrimonio vitivinícola argentino y preserva las tradiciones locales.",
                "Bodega Durigutti, reconocida bodega de Las Compuertas",
                "/durigutti.gif"
            ),      
            other_line(),                  
            rx.box(
                "Ley Nº 25.163 Vinos y bebidas de origen vínico (INV.)",
                background="linear-gradient(to right, transparent, var(--plum-1), transparent)",
                padding="12px",
                border_radius="5px",
                width="100%",
                text_align="center",
                style=styles.other_titles
            ),
            rx.text(
                rx.text.quote(
                """
                Una IG no se inventa, se reconoce. Es parte de un sistema que garantiza que las características 
                del producto sean auténticas y genuinas, transmitidas a través de generaciones y ligadas al 
                conocimiento local compartido."""),
                padding_right=[Size.SMALL, Size.VERY_BIG.value],
                padding_left=[Size.SMALL, Size.VERY_BIG.value],
                padding_top=Size.SMALL.value,
                font_size=Size.DEFAULT.value
            ),              
            other_line(),
            footer_desktop(),
            footer_mobile(),
            footer_line(),    
            )
