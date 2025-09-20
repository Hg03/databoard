import reflex as rx

def contact() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.text("Contact Us", size="6", weight="bold"),
        ),
        align_items="center",
        id="contact-section"
    )