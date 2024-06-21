import reflex as rx
import Eno.styles.styles as styles
from Eno.styles.styles import Size
from Eno.styles.fonts import Font
from Eno.styles.colors import Color, TextColor

class Slick(rx.Component):
    """Slick slider component for main page carousel."""

    library = "react-slick@0.21.0"
    tag = "Slider"

    dots: bool = False
    arrows: bool = False
    infinite: bool = True
    speed: int = 500
    autoplay: bool = True
    autoplaySpeed: int = 5000
    lazyload: bool = True
    is_default = True
    slides_to_show: int = 1
    slides_to_scroll: int = 1
    initial_slide: int = 2
    pause_on_hover: bool = False

    lib_dependencies: list[str] = ["slick-carousel@1.8.1"]

    def _get_custom_code(self) -> str | None:
        return """
        import "slick-carousel/slick/slick.css";
        import "slick-carousel/slick/slick-theme.css";
        """


slick = Slick.create

def carousel_title(text, src, text1) -> rx.Component:
    # Definir la animación
    slide_in_left_keyframes = {
        "0%": {"transform": "translateX(-40px)"},
        "100%": {"transform": "translateX(0)"}
    }

    return rx.heading(
        rx.box(
            rx.text(
                text, 
                align="center", 
                size="8",                 
                weight="light",
                as_="div",
                style={
                    'animation': 'slideInLeft 1s ease-out forwards',
                    **styles.title_style
                },
            ),
            style={
                "background": f"linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)), url('{src}')",
                "background_size": "cover",  # Ajustar el tamaño de fondo
                "background_position": f"{text1}",  # Centrar la imagen de fondo
                "padding": "20px",
                "position": "relative",
                "z_index": "0",  # Fondo detrás del texto
            },
            width="100%",
            height="30em",
            display="flex",           # Usar display flex
            flex_direction="column",  # Organizar los hijos en una columna
            justify_content="center", # Alinear los hijos verticalmente al centro
            align_items="center",     # Alinear los hijos horizontalmente al centro
            spacing="4",
            padding_x=["1em", "3em"],
            padding_y=["5.5em", "10em"],
        ),
        size="4",
        style={
            '@keyframes slideInLeft': slide_in_left_keyframes
        }
    )
    
def header_title(text= " ", text1= "", text2="", link="", src="") -> rx.Component:
    # Definir las animaciones
    slide_in_keyframes = {
        "0%": {"transform": "translateX(-20px)"},
        "100%": {"transform": "translateX(0)"}
    }

    # Aplicar la animación a los elementos
    return rx.hstack(
        rx.box(
            rx.text(
                text, 
                line_height=["0.8", "1"],
                align="left", 
                as_="div",
                color=TextColor.PRIMARY.value,
                font_family=Font.TITLE.value,
                style={
                    'font_size': ["4em", "4em"],
                    'animation': 'slideIn 1s ease-out forwards'
                }
            ),
            rx.text(
                text1,
                line_height=["0.8", "1"], 
                align="left", 
                size="7", 
                as_="div",
                color=TextColor.PRIMARY.value,
                font_family=Font.TITLE.value,
                style={
                    'font_size': ["4em", "4em"],
                    'animation': 'slideIn 1s ease-out forwards'
                }
            ),            
            rx.chakra.link(
                rx.chakra.button(
                    text2,                   
                    color=TextColor.ACCENT.value,
                    bg=Color.PRIMARY.value,
                    size="md",
                    margin_top=Size.MEDIUM.value,
                    _hover={
                        "background": Color.TERTIARY.value,
                        "color": TextColor.PRIMARY.value
                    },
                    style={
                        'animation': 'slideIn 1s ease-out forwards'
                    }                
                ),
                href=link,
            ),
            style={
                "background": f"linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('{src}')",
                "background_size": "cover",  # Ajustar el tamaño de fondo
                "background_position": f"center center",  # Centrar la imagen de fondo
                "padding": "20px",
                "position": "relative",
                "z_index": "0",  # Fondo detrás del texto
            },
            align_items="center",
            spacing="4",
            width="100%",
            height=["25em", "32em"],
            padding_x=["1.5em", "3em"],
            padding_y=["5em", "10em"],
            top="0"
        ),
        style={
            '@keyframes slideIn': slide_in_keyframes
        }
    )


"""class ClickState(rx.State):
    cursor = "grab"

    def change_cursor(self):
        if self.cursor == "grabbing":
            self.cursor = "grab"
        else:
            self.cursor = "grabbing"""


