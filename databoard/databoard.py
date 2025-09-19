import reflex as rx
from .pages.index import index # type: ignore

app = rx.App()
app.add_page(index, route="/")