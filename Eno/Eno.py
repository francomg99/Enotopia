import reflex as rx
from rxconfig import config

from Eno.esp.pages.index import index
from Eno.esp.pages.blog import blog
from Eno.esp.pages.quienes_somos import quienes_somos
from Eno.esp.pages.reservas import reservas
from Eno.esp.views.blog.valle_de_uco import valle_de_uco
from Eno.esp.views.blog.maipu import maipu
from Eno.esp.views.blog.lujan_de_cuyo import lujan_de_cuyo
from Eno.esp.views.blog.maridar import maridar_vinos
from Eno.esp.views.blog.IG import indicacion_geo

import Eno.styles.styles as styles

app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE
)

# Agregar rutas
app.add_page(index, route="/")
app.add_page(blog, route="/blog")
app.add_page(quienes_somos, route="/quienes_somos")
app.add_page(reservas, route="/reservas")
app.add_page(valle_de_uco, route="/blog/valle_de_uco")
app.add_page(maipu, route="/blog/maipu")
app.add_page(lujan_de_cuyo, route="/blog/lujan_de_cuyo")
app.add_page(maridar_vinos, route="/blog/maridar_vinos")
app.add_page(indicacion_geo, route="/blog/bodegas")

# Ejecutar la aplicación
if __name__ == "__main__":
    app.run()
