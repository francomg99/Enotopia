import reflex as rx
from Eno.esp.views.navbar import navbar
from Eno.components.carrusel_blog import carousel_title, slick
from Eno.components.caracteristicas import caracteristicas 
from Eno.components.wine_line import other_line
from Eno.components.title import title
from Eno.components.vinos import vinos

data1 = [
    {"subject": "Acidez", "A": 80, "fullMark": 100},
    {"subject": "Cuerpo", "A": 70, "fullMark": 100},
    {"subject": "Taninos", "A": 86, "fullMark": 100},
    {"subject": "Aroma", "A": 90, "fullMark": 100},
    {"subject": "Equilibrio", "A": 85, "fullMark": 100},
    {"subject": "Alcohol", "A": 90, "fullMark": 100},
]

data2 = [
    {"subject": "Acidez", "A": 60, "fullMark": 100},
    {"subject": "Cuerpo", "A": 75, "fullMark": 100},
    {"subject": "Taninos", "A": 80, "fullMark": 100},
    {"subject": "Aroma", "A": 85, "fullMark": 100},
    {"subject": "Equilibrio", "A": 80, "fullMark": 100},
    {"subject": "Alcohol", "A": 95, "fullMark": 100},
]

data3 = [
    {"subject": "Acidez", "A": 40, "fullMark": 100},
    {"subject": "Cuerpo", "A": 55, "fullMark": 100},
    {"subject": "Taninos", "A": 90, "fullMark": 100},
    {"subject": "Aroma", "A": 80, "fullMark": 100},
    {"subject": "Equilibrio", "A": 70, "fullMark": 100},
    {"subject": "Alcohol", "A": 95, "fullMark": 100},
]

@rx.page(
    route="/blog/valle_de_uco", 
    title="Valle de Uco | Enotopía",
    description="Página de \"Valle de Uco\" de Enotopía"
)


def valle_de_uco() -> rx.Component:
    return rx.box(
        navbar(),
        slick(
            carousel_title("Valle de Uco", "/uco1.jpg", "center"),
            carousel_title("Vale do Uco", "/uco2.jpg", "up"),
            carousel_title("Uco Valley", "/uco3.jpg", "bottom")
        ),
        title("Caracteristicas del Valle de Uco"),
        caracteristicas(
            "Clima",
            """El clima es continental, con veranos cálidos y secos e inviernos fríos. 
            La amplitud térmica diaria (diferencia de temperatura entre el día y la noche) 
            es significativa, lo que ayuda a desarrollar mejor la acidez y los aromas de las uvas.""",
            "Altitud",
            """Las viñas se encuentran a altitudes que varían entre los 900 y 1.500 metros sobre el nivel del mar. 
            Esta altura permite una mayor exposición solar y temperaturas más frescas, favoreciendo una maduración 
            lenta y equilibrada de las uvas.""",
            "Suelo",
            """Los suelos del Valle de Uco son diversos, predominando los suelos aluviales con buen drenaje, 
            lo que contribuye a la concentración y calidad de las uvas.""",
            "/bodega.jpeg"           
        ),
        title("Vinos"),
        vinos(
            "Gran Enemigo 2019",
            "/enemigo.png",
            data1,
            "Antigal - UNO",
            "/uno.png",
            data2,
            "Trapiche - Malbec",
            "/trapiche.png",
            data3
            ),
        other_line(),
        other_line(),
        width="100%"
    )