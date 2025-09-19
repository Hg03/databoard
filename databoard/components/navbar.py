import reflex as rx


def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium", href=url)
    )

def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.heading(
                        "DataBoard", size="7", weight="bold"
                    ),
                    align_items="center"
                ),
                rx.hstack(
                    navbar_link("Home", '/components/header/header'),
                    navbar_link("Gallery", '/components/gallery/gallery'),
                    navbar_link("Try", '/pages/trial/trial'),
                    justify="end",
                    spacing="5"
                ),
                justify="between",
                align_items="center"      
            )
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.heading(
                        "DataBoard", size="6", weight="bold"
                        ),
                        align_items="center",
                    ),
                    rx.menu.root(
                        rx.menu.trigger(
                            rx.icon("menu", size=30),
                        ),
                        rx.menu.content(
                            rx.menu.item("Home"),
                            rx.menu.item("Gallery"),
                            rx.menu.item("Try")
                        ),
                        justify="end"
                    ),
                    justify="between",
                    align_items="center"
            )
        ),
        bg=rx.color("accent", 3),
        padding="1em",
        width="100%"
    )
