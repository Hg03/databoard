import reflex as rx
from ..components.navbar import navbar # type: ignore
from ..components.header import header # type: ignore
from ..components.gallery import gallery # type: ignore
from ..components.contact import contact # type: ignore

@rx.page(route="/", title="DataBoard")
def index() -> rx.Component:
    return rx.vstack(
        navbar("main"),
        rx.vstack(
            header(),
            gallery(),
            contact(),
            align_items="center",  # Only center the content, not navbar
        ),
        width="100%",  # Ensure full width
        spacing="0",   # Remove spacing between navbar and content
        align_items="center",
    )