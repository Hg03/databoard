import reflex as rx
from PIL import Image # type: ignore
import requests # type: ignore

class ImageState(rx.State):
    url: str = f"https://picsum.photos/1000/100"
    image: Image.Image = Image.open(
            requests.get(url, stream=True).raw
        )


class DescriptionState(rx.State):
    description: str = "Your AI-powered data exploration assistant."

def header() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.image(src=ImageState.image),
            rx.heading("DataBoard", size="7", weight="bold"),
            rx.text(DescriptionState.description),
            padding="1em",
            width="100%",
        )
    )