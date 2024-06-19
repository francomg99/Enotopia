import reflex as rx
from Eno.components.info_vinos import info_vinos
import Eno.styles.styles as styles

def maridar():
    return rx.vstack(
        rx.spacer(height="2em"),  # Add space after the text content
        rx.hstack(
            info_vinos(
                "/red_wine.png",
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
                "phone",
                "phone",
                "phone",
                "Phone"),
            rx.spacer(width="4em"),  # Add space between the two boxes
            info_vinos(
                "/white_wine.png",
                "VInos Blancos",
                "• Chardonnay: ",
                "Pollo, mariscos, salsas cremosas",
                "• Sauvignon Blanc: ",
                "Ensaladas, mariscos, queso de cabra",
                "• Riesling: ",
                "Platos picantes, cocina asiática, cerdo",
                "• Pinot Grigio: ",
                "Mariscos, ensaladas ligeras, platos vegetarianos",
                "• Gewürztraminer: ",
                "Cocina asiática, comida picante, quesos fuertes",
                "phone",
                "phone",
                "phone",
                "phone"
                ),
            justify_content="center",  # Center both boxes horizontally
            align_items="center"  # Center both boxes vertically
        ),
        rx.hstack(
            info_vinos(
                "/rose.png",
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
                "phone",
                "phone",
                "phone",
                "Phone"),
            rx.spacer(width="4em"),  # Add space between the two boxes
            info_vinos(
                "/white_wine.png",
                "VInos Blancos",
                "• Chardonnay: ",
                "Pollo, mariscos, salsas cremosas",
                "• Sauvignon Blanc: ",
                "Ensaladas, mariscos, queso de cabra",
                "• Riesling: ",
                "Platos picantes, cocina asiática, cerdo",
                "• Pinot Grigio: ",
                "Mariscos, ensaladas ligeras, platos vegetarianos",
                "• Gewürztraminer: ",
                "Cocina asiática, comida picante, quesos fuertes",
                "phone",
                "phone",
                "phone",
                "phone"
                ),
            justify_content="center",  # Center both boxes horizontally
            align_items="center"  # Center both boxes vertically
        ),        rx.spacer(height="2em"),  # Add space after the boxes
        justify_content="center",  # Center everything vertically in the main vstack
        align_items="center"  # Center everything horizontally in the main vstack
    )
