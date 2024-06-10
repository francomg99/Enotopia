import reflex as rx
from rxconfig import config

from Eno.esp.pages.index import index
from Eno.esp.pages.blog import blog
from Eno.esp.pages.quienes_somos import quienes_somos
from Eno.esp.pages.reservas import reservas

import Eno.styles.styles as styles

app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE
)