import os
import reflex as rx


config = rx.Config(
    app_name="portfolio",
    port=int(os.environ.get("PORT", 3000)),
    proxy_headers=True,
    api_url=os.environ["API_URL"],
    disable_plugins=["reflex.plugins.sitemap.SitemapPlugin"],
    tailwind=None
)
