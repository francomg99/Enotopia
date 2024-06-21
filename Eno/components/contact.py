import reflex as rx
from Eno.components.carrusel_blog import carousel_title

def contact_and_title():
    return rx.vstack(
        rx.box(
        carousel_title("RESERVAS", "/fila_vinos.jpg", "center center"),
        width="100%"
        ),
            rx.html(
                """<iframe id="" allowtransparency="true" allowfullscreen="true" allow="geolocation; microphone; camera" src="https://my.forms.app/form/664e193a033ee128ad551fb4" frameborder="0" style="width: 99vw; min-width:100%; height:300px; border:none;"></iframe>"""
            ),
        align_items="center",
    )
    
def br_contact_and_title():
    return rx.vstack(
        carousel_title("RESERVAS", "/dar_vino.jpg", "center center"),
        rx.box(
            rx.html(
                """<iframe id="" allowtransparency="true" allowfullscreen="true" allow="geolocation; microphone; camera" src="https://my.forms.app/form/664e193a033ee128ad551fb4" frameborder="0" style="width: 99vw; min-width:100%; height:400px; border:none;"></iframe>"""
            )
        ),
        align_items="center",
    )


