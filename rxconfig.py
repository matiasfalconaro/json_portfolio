import os
import reflex as rx

config = rx.Config(
    app_name="portfolio",
    api_url=f"https://mfalconaro.onrender.com:8000",
    port=int(os.environ.get("PORT", 8000)),
    host="0.0.0.0",
    tailwind=None,
    disable_plugins=["reflex.plugins.sitemap.SitemapPlugin"]
)
