import reflex as rx
import Eno.styles.styles as styles


class Slick(rx.Component):
    """Slick slider component for main page carousel."""

    library = "react-slick@0.21.0"
    tag = "Slider"

    dots: bool = False
    arrows: bool = False
    infinite: bool = True
    speed: int = 500
    autoplay: bool = True
    autoplaySpeed: int = 4000
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
    return rx.heading(
        rx.box(
            rx.text(
                text, 
                align="center", 
                size="8",                 
                weight="light",
                as_="div",
                style=styles.title_style,
            ),
            style={
            "background": f"linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)), url('{src}')",
            "background_size": "cover",  # Ajustar el tamaño de fondo
            "background_position": f"{text1}",  # Centrar la imagen de fondo
            "padding": "20px",
            "position": "relative",
            "z_index": "0"  # Fondo detrás del texto
            },
            width="100%",
            height="25em",
            display="flex",           # Use flex display
            flex_direction="column",  # Arrange children in a column
            justify_content="center", # Align children vertically to the center
            align_items="center",     # Align children horizontally to the center
            spacing="4",
            padding_x=["1em","3em"],
            padding_y=["5.5em","10em"],
        ),
        size="4"
    )


"""class ClickState(rx.State):
    cursor = "grab"

    def change_cursor(self):
        if self.cursor == "grabbing":
            self.cursor = "grab"
        else:
            self.cursor = "grabbing"""


