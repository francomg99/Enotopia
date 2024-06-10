import reflex as rx
from Eno.esp.views.navbar import navbar
from Eno.esp.views.blog.blog import blog_desktop, blog_mobile
from Eno.esp.views.footer import footer_desktop, footer_mobile
from Eno.components.wine_line import wine_line

@rx.page(
    route="/blog", 
    title="Blog | Enotopía",
    description="Página web de Enotopía"
    )

def blog() -> rx.Component:
    return rx.box(
        navbar(),
        blog_desktop(),
        blog_mobile(),
        wine_line(),
        footer_desktop(),
        footer_mobile()
    )