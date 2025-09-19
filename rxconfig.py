import reflex as rx

config = rx.Config(
    app_name="databoard",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)