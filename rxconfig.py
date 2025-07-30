import os
import reflex as rx

config = rx.Config(
    app_name="portfolio",
    port=int(os.environ.get("PORT", 8000)),
    tailwind=None,
    disable_plugins=['reflex.plugins.sitemap.SitemapPlugin']
)
