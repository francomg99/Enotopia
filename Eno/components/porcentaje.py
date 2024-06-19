import reflex as rx

# Definir la función de la página
def porcentajes(data):
    return rx.recharts.radar_chart(
        rx.recharts.radar(
            data_key="A",
            stroke="#dcb32a",
            fill="#1c0911",
        ),
        rx.recharts.polar_grid(),
        rx.recharts.polar_angle_axis(data_key="subject"),
        rx.recharts.legend(),
        data=data,
        width=400,  # Establece el ancho del gráfico
        height=215,  # Establece la altura del gráfico
    )