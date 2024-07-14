import reflex as rx
from Eno.esp.views.navbar import navbar
from Eno.components.carrusel_blog import carousel_title, slick
from Eno.components.caracteristicas import caracteristicas
from Eno.components.wine_line import other_line, footer_line
from Eno.components.title import title
from Eno.components.vinos import vinos
from Eno.esp.views.footer import footer_desktop,footer_mobile


# Definir la clase de estado con los datos del gráfico de pastel
data1 = [
    {"subject": "Acidez", "Vinos": 80, "fullMark": 100},
    {"subject": "Cuerpo", "Vinos": 70, "fullMark": 100},
    {"subject": "Taninos", "Vinos": 86, "fullMark": 100},
    {"subject": "Aroma", "Vinos": 90, "fullMark": 100},
    {"subject": "Equilibrio", "Vinos": 85, "fullMark": 100},
    {"subject": "Alcohol", "Vinos": 90, "fullMark": 100},
]

data2 = [
    {"subject": "Acidez", "Vinos": 60, "fullMark": 100},
    {"subject": "Cuerpo", "Vinos": 75, "fullMark": 100},
    {"subject": "Taninos", "Vinos": 80, "fullMark": 100},
    {"subject": "Aroma", "Vinos": 85, "fullMark": 100},
    {"subject": "Equilibrio", "Vinos": 80, "fullMark": 100},
    {"subject": "Alcohol", "Vinos": 95, "fullMark": 100},
]

data3 = [
    {"subject": "Acidez", "Vinos": 40, "fullMark": 100},
    {"subject": "Cuerpo", "Vinos": 55, "fullMark": 100},
    {"subject": "Taninos", "Vinos": 90, "fullMark": 100},
    {"subject": "Aroma", "Vinos": 80, "fullMark": 100},
    {"subject": "Equilibrio", "Vinos": 70, "fullMark": 100},
    {"subject": "Alcohol", "Vinos": 95, "fullMark": 100},
]

@rx.page(
    route="/blog/maipu", 
    title="Maipu | Enotopía",
    description="Página de \"Valle de Uco\" de Enotopía"
)


def maipu() -> rx.Component:
    return rx.box(
        navbar(),
        slick(
            carousel_title("Maipú", "/luigi.jpg", "center center"),
            carousel_title("Maipu", "/flichman.jpg", "center center"),
            carousel_title("Maipu", "/vigil1.jpg", "center center"),
            #carousel_title("Maipu", "/vigil2.jpg", "center center"),             
            ),
        title("Caracteristicas"),
        caracteristicas(
            "Clima",
            """Posee un clima semiárido con influencia continental. Sus veranos son cálidos (18°C - 35°C) 
            y los inviernos frescos (hasta 0°C), con poca lluvia anual. Este clima intensifica los aromas y 
            sabores de las uvas, y favorecen la salud de las plantas al reducir enfermedades.""",
            "Altitud",
            """Se encuentra entre 700 y 800 metros sobre el nivel del mar. Esta altitud moderada crea condiciones 
            climáticas favorables. Durante el día, el sol intenso promueve la maduración de las uvas, mientras que 
            las noches frescas preservan la acidez natural de las uvas, contribuyendo a vinos equilibrados y complejos.""",
            "Suelo",
            """Los suelos aluviales, con buena retención de agua y drenaje adecuado, son ideales para variedades 
            como Cabernet Sauvignon, Malbec, Merlot, Tempranillo, Chardonnay y Sauvignon Blanc, beneficiándose 
            de un ciclo vegetativo prolongado y una tradición vitivinícola que realza su calidad.""",
            "/bodega1.jpeg"           
        ),        
        title("Vinos"),
        vinos(
            "Gran Enemigo - Cabernet Franc",
            "/enemigo.png",
            data1,
            "Antigal - Malbec",
            "/uno.png",
            data2,
            "Trapiche - Malbec",
            "/trapiche.png",
            data3
            ),
        other_line(),
        footer_desktop(),
        footer_mobile(),
        footer_line(),
        width="100%"
    )