import reflex as rx
import Eno.styles.styles as styles
from Eno.styles.styles import Size

class Slick(rx.Component):
    """Slick slider component for main page carousel."""

    library = "react-slick@0.21.0"
    tag = "Slider"

    dots: bool = True
    infinite: bool = True
    speed: int = 500
    arrows: bool = False
    fade: bool = True
    is_default = True
    slides_to_show: int = 3,
    slides_to_scroll: int = 3
    autoplay: bool = True
    autoplaySpeed: int = 4000
    pause_on_hover: bool = True
    draggable: bool = True

    lib_dependencies: list[str] = ["slick-carousel@1.8.1"]

    def _get_custom_code(self) -> str | None:
        return """
        import "slick-carousel/slick/slick.css";
        import "slick-carousel/slick/slick-theme.css";
        """


slick = Slick.create


def development_card(text, text1, text2, src) -> rx.Component:
    return rx.box(
        rx.flex(
            rx.box(
                rx.text(text, size="9", style=styles.other_titles),
                rx.text(
                    text1,
                    size="4",
                    as_="p",
                    padding="10px",
                    style={
                        'text_align': 'justify'
                    }                
                ),
                rx.text(
                    text2,
                    size="4",
                    as_="p",
                    padding="10px",
                    style={
                        'text_align': 'justify'
                    }                
                ),
                width="70%",  # Define el ancho del texto
            ),
            rx.box(
                rx.image(src=src, width="600px", height="auto"),  # Tamaño fijo para la imagen
                width="600px",  # Mantén el contenedor del mismo tamaño que la imagen
                flex_shrink=0,  # Evita que el contenedor de la imagen se contraiga
                background_color="#f0f0f0",
            ),
            direction="row",
            gap="4px",
            align="center",
            justify="center",
        ),
        width="100%",
    )

def development_card_mobile(text, text1, text2) -> rx.Component:
    return rx.box(
        rx.flex(
            rx.box(
                rx.text(text, size="9", style=styles.other_titles),
                rx.text(
                    text1,
                    size="4",
                    as_="p",
                    padding="10px",
                    style={
                        'text_align': 'justify'
                    }                
                ),
                rx.text(
                    text2,
                    size="4",
                    as_="p",
                    padding="10px",
                    style={
                        'text_align': 'justify'
                    }                
                ),
                width="10%",  # Define el ancho del texto
            ),
            #direction="column",
            gap="4px",
            align="start",
            justify="start",
        ),
        width="30%"
    )


class ClickState(rx.State):
    cursor = "grab"

    def change_cursor(self):
        if self.cursor == "grabbing":
            self.cursor = "grab"
        else:
            self.cursor = "grabbing"


def que_ofrecemos() -> rx.Component:
    return rx.box(
        slick(
            development_card(
                """• Visitas guiadas a bodegas •""",
                """Te invitamos a nuestras exclusivas visitas guiadas a las bodegas más hermosas de la provincia. Sumérgete en los viñedos más prestigiosos, 
                aprende sobre el proceso de elaboración del vino y disfruta de degustaciones exclusivas maridadas con delicias locales.""", 
                """Mendoza ofrece un entorno inigualable para una experiencia enoturística. No solo te sumergirás en la cultura del vino, 
                sino que también disfrutarás de la calidez de su gente y la belleza de sus paisajes. Cada visita es una oportunidad para vivir 
                momentos memorables.""",
                """/andeluna.png"""
                ),
            development_card(
                """• Cata de vinos exclusiva •""",
                """Organizamos catas de vinos dirigidas por los mejores y más expertos enólogos y sommeliers, que permiten a nuestros turistas explorar una amplia 
                gama de vinos locales y descubrir nuevas variedades y estilos.""", 
                """Las catas se llevan a cabo en entornos totalmente innovadores, como bodegas históricas, salas de degustación con vistas panorámicas 
                y encantadores patios al aire libre.""",
                """/copa2.jpg"""
                ),
            development_card(
                """• Recorridos por Viñedos •""",
                """Ofrecemos a los visitantes la oportunidad de sumergirse en la belleza natural de los paisajes vinícolas mendocinos, 
                mientras aprenden sobre las diferentes variedades de uva cultivadas en la región. Los participantes tienen la oportunidad de interactuar con 
                viticultores locales y aprender sobre todas las prácticas de cultivo.""", 
                """Además, podrán disfrutar de la hospitalidad mendocina y degustar productos locales frescos directamente de la fuente.
                Cada recorrido está diseñado para ser educativo y entretenido, proporcionando una comprensión profunda de la historia y la cultura vinícola 
                de Mendoza.""",
                """/viñedos.jpg"""
                ),
            development_card(
                """• Gastronomía Local •""",
                """Enriquecemos nuestras experiencias vinícolas con exquisitas degustaciones de la gastronomía local. Nuestros eventos incluyen maridajes de vinos 
                con una selección de platos tradicionales y gourmet que resaltan lo mejor de la región. En colaboración con chefs locales y 
                restaurantes de renombre.""", 
                """Cada evento se celebra en un ambiente acogedor y elegante, variando desde patios al aire libre hasta bodegas históricas. 
                Nuestros sommeliers expertos están siempre disponibles para guiar a los participantes a través de la experiencia de maridaje, explicando cómo 
                cada vino complementa y realza los sabores de los platos.""",
                """/barrica1.jpg"""
                ),
            development_card(
                """• Actividades Especiales •""",
                """Además ofrecemos una amplia variedad de actividades especiales. 
                Desde emocionantes paseos en globo aerostático sobre los viñedos hasta clases de cocina con temática de vino y talleres de elaboración de vinos, 
                hay algo para cada gusto. También puedes participar en excursiones en bicicleta por los viñedos y explorar lugares históricos y culturales cercanos.""", 
                """Estas experiencias te permiten sumergirte aún más en la cultura del vino y disfrutar de la belleza de la región mientras aprendes sobre 
                prácticas de cultivo sostenible y viticultura orgánica de la mano de viticultores locales.""",
                """/vinos.jpg"""
                ),            
        ),
        on_mouse_down=ClickState.change_cursor,
        on_mouse_up=ClickState.change_cursor,
        width="95%",
    )
    
def que_ofrecemos_mobile() -> rx.Component:
    return rx.box(
        slick(
            development_card_mobile(
                """• Visitas guiadas a bodegas •""",
                """Te invitamos a nuestras exclusivas visitas guiadas a las bodegas más hermosas de la provincia. Sumérgete en los viñedos más prestigiosos, 
                aprende sobre el proceso de elaboración del vino y disfruta de degustaciones exclusivas maridadas con delicias locales.""", 
                """Mendoza ofrece un entorno inigualable para una experiencia enoturística. No solo te sumergirás en la cultura del vino, 
                sino que también disfrutarás de la calidez de su gente y la belleza de sus paisajes. Cada visita es una oportunidad para vivir 
                momentos memorables.""",
                ),
            development_card_mobile(
                """• Cata de vinos exclusiva •""",
                """Organizamos catas de vinos dirigidas por los mejores y más expertos enólogos y sommeliers, que permiten a nuestros turistas explorar una amplia 
                gama de vinos locales y descubrir nuevas variedades y estilos.""", 
                """Las catas se llevan a cabo en entornos totalmente innovadores, como bodegas históricas, salas de degustación con vistas panorámicas 
                y encantadores patios al aire libre.""",
                ),
            development_card_mobile(
                """• Recorridos por Viñedos •""",
                """Ofrecemos a los visitantes la oportunidad de sumergirse en la belleza natural de los paisajes vinícolas mendocinos, 
                mientras aprenden sobre las diferentes variedades de uva cultivadas en la región. Los participantes tienen la oportunidad de interactuar con 
                viticultores locales y aprender sobre todas las prácticas de cultivo.""", 
                """Además, podrán disfrutar de la hospitalidad mendocina y degustar productos locales frescos directamente de la fuente.
                Cada recorrido está diseñado para ser educativo y entretenido, proporcionando una comprensión profunda de la historia y la cultura vinícola 
                de Mendoza.""",
                ),
            development_card_mobile(
                """• Gastronomía Local •""",
                """Enriquecemos nuestras experiencias vinícolas con exquisitas degustaciones de la gastronomía local. Nuestros eventos incluyen maridajes de vinos 
                con una selección de platos tradicionales y gourmet que resaltan lo mejor de la región. En colaboración con chefs locales y 
                restaurantes de renombre.""", 
                """Cada evento se celebra en un ambiente acogedor y elegante, variando desde patios al aire libre hasta bodegas históricas. 
                Nuestros sommeliers expertos están siempre disponibles para guiar a los participantes a través de la experiencia de maridaje, explicando cómo 
                cada vino complementa y realza los sabores de los platos.""",
                ),
            development_card_mobile(
                """• Actividades Especiales •""",
                """Además ofrecemos una amplia variedad de actividades especiales. 
                Desde emocionantes paseos en globo aerostático sobre los viñedos hasta clases de cocina con temática de vino y talleres de elaboración de vinos, 
                hay algo para cada gusto. También puedes participar en excursiones en bicicleta por los viñedos y explorar lugares históricos y culturales cercanos.""", 
                """Estas experiencias te permiten sumergirte aún más en la cultura del vino y disfrutar de la belleza de la región mientras aprendes sobre 
                prácticas de cultivo sostenible y viticultura orgánica de la mano de viticultores locales.""",
                ),            
        ),
        on_mouse_down=ClickState.change_cursor,
        on_mouse_up=ClickState.change_cursor,
        width="95%",
    )