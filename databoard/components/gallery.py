import reflex as rx
from PIL import Image # type: ignore
import requests # type: ignore

class ImageState(rx.State):
    url: str = f"https://picsum.photos/1000/100"
    image: Image.Image = Image.open(
            requests.get(url, stream=True).raw
        )

def gallery() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.text("Gallery", size="6", weight="bold"),
            rx.image(src=ImageState.image),
            rx.image(src=ImageState.image),
            rx.image(src=ImageState.image),
            rx.link("See more", href="/#")
        ),
            spacing="9",
            align_items="center"
    )