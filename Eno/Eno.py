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

import Eno.styles.styles as styles

app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE
)