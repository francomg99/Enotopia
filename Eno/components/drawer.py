import reflex as rx
from Eno.styles.styles import Size
from Eno.styles.fonts import Font
from Eno.styles.colors import Color, TextColor
from Eno.components.title import others_titles


class DrawerState(rx.State):
    show_menu: bool = False

    def toggle_menu(self):
        self.show_menu = not self.show_menu
    
    def redirect_and_close(self, path):
        self.toggle_menu()
        return rx.redirect(path)  

def menu():
    return rx.chakra.vstack(
        rx.chakra.button(
            "Inicio",
            bg="#ecdae2", 
            color=TextColor.ACCENT.value, 
            style={
                "font_size": Size.LETTER.value
            },
            _hover={
                'background': Color.TERTIARY.value,
                'color':TextColor.PRIMARY.value
            },            
            on_click=lambda: DrawerState.redirect_and_close("/")
            ),
        rx.chakra.button(
            "Blog", 
            bg="#ecdae2", 
            color=TextColor.ACCENT.value, 
            style={
                "font_size": Size.LETTER.value
            },           
            _hover={
                'background': Color.TERTIARY.value,
                'color':TextColor.PRIMARY.value
            },  
            on_click=lambda: DrawerState.redirect_and_close("/blog")
        ),
        rx.chakra.button(
            "¿Quiénes somos?", 
            bg="#ecdae2", 
            color=TextColor.ACCENT.value, 
            style={
                "font_size": Size.LETTER.value
            },
            _hover={
                'background': Color.TERTIARY.value,
                'color':TextColor.PRIMARY.value
            },  
            on_click=lambda: DrawerState.redirect_and_close("/quienes_somos")
        ),
        rx.chakra.button(
            "Reservas", 
            bg="#ecdae2", 
            color=TextColor.ACCENT.value, 
            style={
                "font_size": Size.LETTER.value
            },
            _hover={
                'background': Color.TERTIARY.value,
                'color':TextColor.PRIMARY.value
            },  
            on_click=lambda: DrawerState.redirect_and_close("/reservas")
        ),
        rx.chakra.button(
            "Cerrar", 
            on_click=DrawerState.toggle_menu, 
            bg=Color.ACCENT.value,
            _hover={
                'background': Color.TERTIARY.value,
                'color':TextColor.PRIMARY.value
            },        
            ),
        rx.chakra.image(
            src="/copas.png",
            width=["18em","20em"]
        ),
        spacing="4",
    )

def wine_menu_desktop():
    return rx.tablet_and_desktop(
        rx.chakra.vstack(
        rx.chakra.button(
            rx.html(
                """<script src="https://cdn.lordicon.com/lordicon.js"></script>
            <lord-icon
                src="https://cdn.lordicon.com/dabfbizw.json"
                trigger="hover"
                style="width:90px;height:90px">
            </lord-icon>"""
                ),
            on_click=DrawerState.toggle_menu, 
            size="lg", 
            bg=Color.CUARTIARY.value, 
            _hover={
                'background': Color.CUARTIARY.value,
                'color':TextColor.SECONDARY.value}
        ),
        rx.chakra.drawer(
            rx.chakra.drawer_overlay(
                rx.chakra.drawer_content(
                    others_titles("MENÚ"),
                    rx.chakra.drawer_body(menu()),
                    bg="#ecdae2",
                )
            ),
            is_open=DrawerState.show_menu,
            size="sm",  # Puedes ajustar el tamaño a "xs", "sm", "md", "lg", "xl", "full"
        ),
    )
    )
    
def wine_menu_mobile():
    return rx.mobile_only(
        rx.chakra.vstack(
        rx.chakra.button(
            rx.html(
                """<script src="https://cdn.lordicon.com/lordicon.js"></script>
            <lord-icon
                src="https://cdn.lordicon.com/dabfbizw.json"
                trigger="hover"
                style="width:90px;height:90px">
            </lord-icon>"""
                ),            on_click=DrawerState.toggle_menu, 
            size="lg", 
            bg=Color.CUARTIARY.value, 
            _hover={
                'background': Color.CUARTIARY.value,
                'color':TextColor.SECONDARY.value}
        ),
        rx.chakra.drawer(
            rx.chakra.drawer_overlay(
                rx.chakra.drawer_content(
                    others_titles("MENÚ"),
                    rx.chakra.drawer_body(menu()),
                    bg="#ecdae2",
                )
            ),
            is_open=DrawerState.show_menu,
            size="sm",# Puedes ajustar el tamaño a "xs", "sm", "md", "lg", "xl", "full"
        ),
    )
    )

def br_menu():
    return rx.chakra.vstack(
        rx.chakra.button(
            "Inicio",
            bg="#ecdae2", 
            color=TextColor.ACCENT.value, 
            style={
                "font_size": Size.LETTER.value
            },
            _hover={
                'background': Color.TERTIARY.value,
                'color':TextColor.PRIMARY.value
            },            
            on_click=lambda: DrawerState.redirect_and_close("/br")
            ),
        rx.chakra.button(
            "Blog", 
            bg="#ecdae2", 
            color=TextColor.ACCENT.value, 
            style={
                "font_size": Size.LETTER.value
            },           
            _hover={
                'background': Color.TERTIARY.value,
                'color':TextColor.PRIMARY.value
            },  
            on_click=lambda: DrawerState.redirect_and_close("/br/blog")
        ),
        rx.chakra.button(
            "¿Quem somos?", 
            bg="#ecdae2", 
            color=TextColor.ACCENT.value, 
            style={
                "font_size": Size.LETTER.value
            },
            _hover={
                'background': Color.TERTIARY.value,
                'color':TextColor.PRIMARY.value
            },  
            on_click=lambda: DrawerState.redirect_and_close("/br/quienes_somos")
        ),
        rx.chakra.button(
            "Reservas", 
            bg="#ecdae2", 
            color=TextColor.ACCENT.value, 
            style={
                "font_size": Size.LETTER.value
            },
            _hover={
                'background': Color.TERTIARY.value,
                'color':TextColor.PRIMARY.value
            },  
            on_click=lambda: DrawerState.redirect_and_close("/br/reservas")
        ),
        rx.chakra.button(
            "Fechar", 
            on_click=DrawerState.toggle_menu, 
            bg=Color.ACCENT.value,
            _hover={
                'background': Color.TERTIARY.value,
                'color':TextColor.PRIMARY.value
            },        
            ),
        rx.chakra.image(
            src="/copas.png",
            width=["18em","20em"]
        ),
        spacing="4",
    )

def br_wine_menu_desktop():
    return rx.tablet_and_desktop(
        rx.chakra.vstack(
        rx.chakra.button(
            rx.html(
                """<script src="https://cdn.lordicon.com/lordicon.js"></script>
            <lord-icon
                src="https://cdn.lordicon.com/dabfbizw.json"
                trigger="hover"
                style="width:90px;height:90px">
            </lord-icon>"""
                ),
            on_click=DrawerState.toggle_menu, 
            size="lg", 
            bg=Color.CUARTIARY.value, 
            _hover={
                'background': Color.CUARTIARY.value,
                'color':TextColor.SECONDARY.value}
        ),
        rx.chakra.drawer(
            rx.chakra.drawer_overlay(
                rx.chakra.drawer_content(
                    others_titles("MENÚ"),
                    rx.chakra.drawer_body(br_menu()),
                    bg="#ecdae2",
                )
            ),
            is_open=DrawerState.show_menu,
            size="sm",  # Puedes ajustar el tamaño a "xs", "sm", "md", "lg", "xl", "full"
        ),
    )
    )
    
def br_wine_menu_mobile():
    return rx.mobile_only(
        rx.chakra.vstack(
        rx.chakra.button(
            rx.html(
                """<script src="https://cdn.lordicon.com/lordicon.js"></script>
            <lord-icon
                src="https://cdn.lordicon.com/dabfbizw.json"
                trigger="hover"
                style="width:90px;height:90px">
            </lord-icon>"""
                ),
            on_click=DrawerState.toggle_menu, 
            size="lg", 
            bg=Color.CUARTIARY.value, 
            _hover={
                'background': Color.CUARTIARY.value,
                'color':TextColor.SECONDARY.value}
        ),
        rx.chakra.drawer(
            rx.chakra.drawer_overlay(
                rx.chakra.drawer_content(
                    others_titles("MENÚ"),
                    rx.chakra.drawer_body(br_menu()),
                    bg="#ecdae2",
                )
            ),
            is_open=DrawerState.show_menu,
            size="sm",# Puedes ajustar el tamaño a "xs", "sm", "md", "lg", "xl", "full"
        ),
    )
    )