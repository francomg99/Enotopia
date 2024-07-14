import reflex as rx
from Eno.esp.views.navbar import navbar
from Eno.components.carrusel_blog import carousel_title, slick
from Eno.components.caracteristicas import caracteristicas 
from Eno.components.wine_line import other_line, footer_line
from Eno.components.title import title
from Eno.components.vinos import vinos
from Eno.esp.views.footer import footer_desktop,footer_mobile

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
    route="/blog/lujan_de_cuyo", 
    title="Luján de Cuyo | Enotopía",
    description="Página de \"Luján de Cuyo\" de Enotopía"
)


def lujan_de_cuyo() -> rx.Component:
    return rx.box(
        navbar(),
        slick(
            carousel_title("Luján de Cuyo", "/decero.jpg", "center center"),
            carousel_title("Luján de Cuyo", "/cobos.jpg", "center center"),
            carousel_title("Luján de Cuyo", "/penedo.jpg", "center center"),
            carousel_title("Luján de Cuyo", "/balbo.jpg", "center center"),
            carousel_title("Luján de Cuyo", "/bressia.jpg", "center center"),        
            ),
        title("Caracteristicas"),
        caracteristicas(
            "Clima",
            """Luján de Cuyo tiene un clima semiárido ideal para la viticultura, con veranos calurosos (18°C a 33°C) e inviernos frescos (3°C a 15°C) y una marcada amplitud térmica diaria. La baja precipitación anual, concentrada en verano, permite un control preciso del riego.""",
            "Altitud",
            """Se sitúa entre los 900 y 1100 msnm, lo que genera una amplitud térmica diaria favorable para una maduración fenólica equilibrada de las uvas. La intensa radiación solar mejora la calidad y el color de los vinos, produciendo Malbec con acidez balanceada, buena estructura y excelente potencial de envejecimiento.""",
            "Suelo",
            """Los suelos de Luján de Cuyo son aluviales, compuestos por una mezcla de arena, limo y arcilla, con abundante grava y piedras que aseguran un buen drenaje. La presencia de minerales como calcio y magnesio mejora la salud de la vid y la calidad del fruto.""",
            "/bodega3.jpeg"           
        ),
        title("Vinos"),
        vinos(
            "DV Catena - Malbec Malbec",
            "/catena.png",
            data1,
            "Bressia - Lagrima de Canela",
            "/bressia.png",
            data2,
            "Guarda - Malbec",
            "/guarda.png",
            data3
            ),
        other_line(),
        footer_desktop(),
        footer_mobile(),
        footer_line(),
        width="100%"
    )