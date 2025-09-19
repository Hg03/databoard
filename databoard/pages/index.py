import reflex as rx
from ..components.navbar import navbar # type: ignore

def index() -> rx.Component:
    return rx.vstack(
        navbar(),
        # Your main page content here
        rx.text("Welcome to DataBoard!"),
        spacing="0",
        width="100%"
    )