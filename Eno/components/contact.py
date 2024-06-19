import reflex as rx
from Eno.components.title import title

def contact_and_title():
    return rx.vstack(
        title("CONTACTANOS"),
        rx.box(
            rx.html(
                """<iframe id="" allowtransparency="true" allowfullscreen="true" allow="geolocation; microphone; camera" src="https://my.forms.app/form/664e193a033ee128ad551fb4" frameborder="0" style="width: 99vw; min-width:100%; height:600px; border:none;"></iframe>"""
            )
        ),
        align_items="center",
    )
    
def br_contact_and_title():
    return rx.vstack(
        title("CONTATE-NOS"),
        rx.box(
            rx.html(
                """<iframe id="" allowtransparency="true" allowfullscreen="true" allow="geolocation; microphone; camera" src="https://my.forms.app/form/664e193a033ee128ad551fb4" frameborder="0" style="width: 99vw; min-width:100%; height:400px; border:none;"></iframe>"""
            )
        ),
        align_items="center",
    )


