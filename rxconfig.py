import os
import reflex as rx


config = rx.Config(
    app_name="portfolio",
    port=int(os.environ.get("PORT", 3000)),
    tailwind=None,
    db_url=os.environ.get("MONGO_URI", "mongodb://localhost:27017/portfolio_db"),
)
