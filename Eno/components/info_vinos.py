import reflex as rx 
import Eno.styles.styles as styles
from Eno.styles.styles import Size, TextColor

def info_vinos(src, title, title1, text1, title2, text2, title3, text3, title4, text4, title5, text5, icon1, icon2, icon3, icon4):
    text_style = {
        'color': TextColor.PRIMARY.value,
        'font_size': Size.LETTER.value,
        'margin_top': '0.5em',
    }
    
    return rx.box(
                rx.hstack(
                    rx.image(src=src, width="10em", height="auto", zoom_scale=2),
                    rx.vstack(
                        rx.text(title, style=styles.other_titles),
                        rx.text(rx.text.strong(title1), text1, style=text_style),
                        rx.text(rx.text.strong(title2), text2, style=text_style),
                        rx.text(rx.text.strong(title3), text3, style=text_style),
                        rx.text(rx.text.strong(title4), text4, style=text_style),
                        rx.text(rx.text.strong(title5), text5, style=text_style),
                        rx.hstack(
                            rx.image(icon1, width="2em"),
                            rx.image(icon2, width="2em"),
                            rx.image(icon3, width="2em"),
                            rx.image(icon4, width="2em"),
                            justify_content="start"  # Align icons within hstack to start
                        ),
                        align_items="start",  # Align text and icons vertically to start
                    ),
                    align_items="center",  # Center image and text vertically
                    justify_content="center"  # Center image and text horizontally
                ),
                width="50%",
                justify_content="center",  # Center the box content horizontally
                align_items="center",  # Center the box content vertically
                padding="1em"  # Add padding inside the box for spacing
            ),
    
