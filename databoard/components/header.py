import reflex as rx
from PIL import Image # type: ignore
import requests # type: ignore

class ImageState(rx.State):
    url: str = f"https://picsum.photos/1000/100"


class DescriptionState(rx.State):
    description: str = "Your AI-powered data exploration assistant."

def header() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.image(src=ImageState.url),
            rx.heading("DataBoard", size="7", weight="bold"),
            rx.text(DescriptionState.description),
            padding="1em",
            width="100%",
        ),
        id="header-section"
    )