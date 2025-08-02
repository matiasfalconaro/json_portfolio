import os
import reflex as rx

config = rx.Config(
    app_name="portfolio",
    port=int(os.environ.get("PORT", 8000)),
    proxy_headers=True,
    api_url=os.environ.get("API_URL", "https://mfalconaro.up.railway.app"),
    disable_plugins=["reflex.plugins.sitemap.SitemapPlugin"],
    tailwind=None
)