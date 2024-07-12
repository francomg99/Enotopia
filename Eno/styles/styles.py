from enum import Enum
from .fonts import Font
from .colors import Color, TextColor

class Size(Enum):
    ZERO = "0px !important"
    SMALL = "0.5em"
    MEDIUM = "1em"
    LETTER = "1.1em"
    DEFAULT = "1.2em"
    BIG = "2em"
    METHOD_TITLE="2.3em"
    TITLE= "4em"
    BUTTON = "3em"
    VERY_BIG = "4em"
    
STYLESHEETS = [
        "https://fonts.googleapis.com/css2?family=Noto+Sans:ital,wght@0,100..900;1,100..900&display=swap",
        "https://fonts.googleapis.com/css2?family=Bebas+Neue&display=swap"
]

BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "color": TextColor.PRIMARY.value,
    "background": Color.ACCENT.value,
}

title_style = dict(
    width="100%",
    font_size=[Size.VERY_BIG.value, Size.TITLE.value],
    font_family=Font.TITLE.value,
    color=TextColor.SECONDARY.value,
    )

subtitles = dict(
    width="100%",
    font_size=[Size.METHOD_TITLE.value, Size.METHOD_TITLE.value],
    font_family=Font.TITLE.value,
    color=TextColor.SECONDARY.value,
    )

other_titles = dict(
    width="100%",
    font_size=["1.8em", Size.BIG.value],
    font_family=Font.TITLE.value,
    color=TextColor.PRIMARY.value,
    text_align= 'center'   
    )