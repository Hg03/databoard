import reflex as rx
from ..components.navbar import navbar # type: ignore

@rx.page(route="/trial", title="Trial Page")
def trial() -> rx.Component:
    return rx.container(
        rx.vstack(
            navbar(),
            rx.text("This is a trial page!"),
            spacing="9",
            width="100%"
        )
    )