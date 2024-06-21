import reflex as rx
from Eno.esp.views.navbar import navbar
from Eno.components.carrusel_blog import carousel_title, slick
from Eno.components.caracteristicas import caracteristicas 
from Eno.components.wine_line import other_line
from Eno.components.title import title
from Eno.components.vinos import vinos

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
    route="/blog/valle_de_uco", 
    title="Valle de Uco | Enotopía",
    description="Página de \"Valle de Uco\" de Enotopía"
)


def valle_de_uco() -> rx.Component:
    return rx.box(
        navbar(),
        slick(
            carousel_title("Valle de Uco", "/diamandes2.jpg", "center"),
            carousel_title("Vale do Uco", "/alfa.jpg", "center"),
            carousel_title("Uco Valley", "/zuccardi.jpg", "center"),
            carousel_title("Uco Valley", "/monteviejo2.jpeg", "center"),
            carousel_title("Uco Valley", "/salentein3.jpg", "center")
        ),
        title("Caracteristicas de esta región"),
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
            "/bodega2.jpeg"           
        ),
        title("Vinos"),
        vinos(
            "Salentein - SP Los Jabalíes - Malbec",
            "/salentein.png",
            data1,
            "Zuccardi - Aluvional Malbec",
            "/aluvional.png",
            data2,
            "Rutini - Malbec",
            "/rutini.png",
            data3
            ),
        other_line(),
        other_line(),
        width="100%"
    )