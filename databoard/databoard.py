import reflex as rx
from .pages.index import index # type: ignore
from .pages.trial import trial # type: ignore

app = rx.App(
    theme=rx.theme(
        appearance="light",
        has_background=True,
        radius="large",
        scaling="100%",
        accent_color="orange",
        gray_color="sand",
        panel_background="solid",
    )
)
# app.add_page(index)