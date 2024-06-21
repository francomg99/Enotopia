import reflex as rx
from Eno.components.info_vinos import info_vinos
import Eno.styles.styles as styles
from Eno.styles.styles import Size, TextColor
from Eno.components.wine_line import other_line

def maridar():
    text_style = {
        'color': TextColor.PRIMARY.value,
        'font_size': Size.LETTER.value,
        'margin_top': '0.5em',
    }
    return rx.vstack(
        rx.spacer(height="2em"),  # Add space after the text content
        rx.hstack(
            info_vinos(
                "/tinto.png",
                "Vinos Tintos",
                "• Malbec: ",
                "Carne de vacuno, carnes a la parrilla ",
                "• Cabernet Sauvignon: ",
                "Carnes rojas asadas, cordero ",
                "• Pinot Noir: ",
                "Aves de corral, cerdo, setas ",
                "• Merlot: ",
                "Carnes rojas a la parrilla, estofados ",
                "• Syrah: ",
                "Carnes a la parrilla, barbacoas ",
                "/carne.png",
                "/setas.png",
                "/cerdo.png",
                "/pollo.png",
            ),
            rx.spacer(width="3em"),  # Add space between the two boxes
            info_vinos(
                "/blanco.png",
                "VInos Blancos",
                "• Chardonnay: ",
                "Pollo, mariscos, salsas cremosas",
                "• Sauvignon Blanc: ",
                "Ensaladas, mariscos, queso de cabra",
                "• Riesling: ",
                "Platos picantes, cocina asiática, cerdo",
                "• Pinot Grigio: ",
                "Mariscos, ensaladas ligeras, platos veggies",
                "• Gewürztraminer: ",
                "Cocina asiática, picante, quesos fuertes",
                "/pollo.png",
                "/zanahoria.png",
                "/queso.png",
                "/pimiento.png",
            ),
            justify_content="center",  # Center both boxes horizontally
            align_items="center"  # Center both boxes vertically
        ),
        rx.spacer(height="2em"),  # Add space after the boxes
        rx.hstack(
            info_vinos(
                "/rosado.png",
                "Vinos Rosados",
                "• Malbec: ",
                "Empanadas, carnes blancas, ensaladas",
                "• Syrah: ",
                "Carnes especiadas, pizzas",
                "• Pinot Noir: ",
                "Salmón, sushi, quesos suaves.",
                "• Cabernet Sauvignon: ",
                "Carnes a la parrilla, pastas.",
                "• Torrontes: ",
                "Comida asiática, mariscos, ceviche.",
                "/empanada.png",
                "/pizza.png",
                "/sushi.png",
                "/queso.png",
            ),
            rx.spacer(width="3em"),  # Add space between the two boxes
            info_vinos(
                "/espumante.png",
                "VInos Espumosos",
                "• Extra Brut: ",
                "Ostras, sushi, verdes, aperitivos ligeros",
                "• Brut Nature: ",
                "Quesos, ceviche, Mariscos",
                "• Brut: ",
                "Pescados asados, pollo, aves",
                "• Demi-Sec: ",
                "Postres ligeros, tartas, comida hindi, quesos azules",
                "• Sweet: ",
                "Postres dulces, frutas frescas, pasteles, foie gras.",
                "/frutilla.png",
                "/postre.png",
                "/queso.png",
                "/pescado.png",
            ),
            justify_content="center",  # Center both boxes horizontally
            align_items="center"  # Center both boxes vertically
        ),
        other_line(),
        rx.hstack(
            rx.spacer(width="2em"),  # Add space after the boxes
            rx.image(src="/quesos_madera.png", width="30em") ,
            rx.vstack(
            rx.text("CONSEJOS", style=styles.subtitles),
            rx.text(rx.text.strong("Prueba y experimenta: "), "La mejor manera de aprender sobre maridaje es experimentar y probar diferentes combinaciones.", style=text_style),
            rx.text(rx.text.strong("Considera las preferencias personales: "), "Los gustos personales juegan un papel importante, así que adapta las sugerencias a tus preferencias y las de tus invitados.", style=text_style),
            rx.text(rx.text.strong("No temas romper las reglas: "), "Las reglas de maridaje son guías, no leyes. Si encuentras una combinación que disfrutas, eso es lo más importante.", style=text_style)     
        ),
            rx.spacer(width="2em"),  # Add space after the boxes
            justify_content="center",  # Center both boxes horizontally
            align_items="center"  # Center both boxes vertically        
            ),
        rx.spacer(height="2em"),  # Add space after the boxes
        justify_content="center",  # Center everything vertically in the main vstack
        align_items="center"  # Center everything horizontally in the main vstack
    )
