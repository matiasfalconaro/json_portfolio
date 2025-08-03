import reflex as rx
import os

config = rx.Config(
    app_name="portfolio",
    port=int(os.environ.get("PORT", 3000)),
    tailwind=None,
)