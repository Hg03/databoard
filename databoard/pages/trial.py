import reflex as rx
from ..components.navbar import navbar # type: ignore

@rx.page(route="/trial", title="Trial Page")
def trial() -> rx.Component:
    return rx.vstack(
        navbar("trial"),
        rx.vstack(
            rx.text("This is a trial page!"),
            align_items="center",  # Only center the content, not navbar
        ),
        width="100%",  # Ensure full width
        spacing="0",   # Remove spacing between navbar and content
        align_items="center",
    )