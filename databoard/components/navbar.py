import reflex as rx


def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium"),
        href=url
    )

def navbar(page_type: str = "main") -> rx.Component:
    # Define links based on page type
    if page_type == "main":
        home_link = '#header-section'
        gallery_link = '#gallery-section' 
        contact_link = '#contact-section'
    else:
        # For other pages, redirect to main page with sections
        home_link = '/#header-section'
        gallery_link = '/#gallery-section'
        contact_link = '/#contact-section'
    
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
                    navbar_link("Home", home_link),
                    navbar_link("Gallery", gallery_link),
                    navbar_link("Contact", contact_link),
                    navbar_link("Try", '/trial'),
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
                            rx.menu.item(
                                rx.link("Home", href=home_link)
                            ),
                            rx.menu.item(
                                rx.link("Gallery", href=gallery_link)
                            ),
                            rx.menu.item(
                                rx.link("Contact", href=contact_link)
                            ),
                            rx.menu.item(
                                rx.link("Try", href="/trial")
                            )
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