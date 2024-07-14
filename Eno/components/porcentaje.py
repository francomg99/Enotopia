import reflex as rx
from Eno.styles.styles import Size

# Definir la función de la página
def porcentajes(data):
    return rx.recharts.radar_chart(
        rx.recharts.radar(
            data_key="Vinos",
            stroke="#dcb32a",
            fill="#1c0911",
        ),
        rx.recharts.polar_grid(),
        rx.recharts.polar_angle_axis(data_key="subject"),
        rx.recharts.legend(),
        data=data,
        width=375,  # Establece el ancho del gráfico
        height=215,  # Establece la altura del gráfico
        )