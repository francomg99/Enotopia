import reflex as rx 
import Eno.styles.styles as styles

def info_vinos(src, title, title1, text1, title2, text2, title3, text3, title4, text4, title5, text5, icon1, icon2, icon3, icon4):
    return rx.box(
                rx.hstack(
                    rx.image(src=src, width="10em", height="auto"),
                    rx.vstack(
                        rx.text(title, style=styles.other_titles),
                        rx.text(rx.text.strong(title1), text1),
                        rx.text(rx.text.strong(title2), text2),
                        rx.text(rx.text.strong(title3), text3),
                        rx.text(rx.text.strong(title4), text4),
                        rx.text(rx.text.strong(title5), text5),
                        rx.hstack(
                            rx.icon(icon1),
                            rx.icon(icon2),
                            rx.icon(icon3),
                            rx.icon(icon4),
                            justify_content="start"  # Align icons within hstack to start
                        ),
                        align_items="start",  # Align text and icons vertically to start
                    ),
                    align_items="center",  # Center image and text vertically
                    justify_content="center"  # Center image and text horizontally
                ),
                justify_content="center",  # Center the box content horizontally
                align_items="center",  # Center the box content vertically
                padding="1em"  # Add padding inside the box for spacing
            ),