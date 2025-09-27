import reflex as rx

from .states import AdminState
from .admin import admin_page
from .components import *
from .styles import *


def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            navbar(),
            header_section(),
            rx.divider(),
            rx.heading("Work Experience",
                       id="work",
                       **section_heading_style),
            work_section(),
            rx.divider(),

            rx.heading("Education",
                       id="education",
                       **section_heading_style),
            education_section(),
            rx.divider(),

            rx.heading("Projects",
                       id="projects",
                       **section_heading_style),
            project_section(),
            rx.divider(),

            footer(),
            contact_modal(),
            code_info_modal(),
            **page_layout_style
        ),
        **page_wrapper_style,
        on_mount=AdminState.on_mount
    )


# App Setup
app = rx.App()
app.add_page(index, title="Matias Falconaro | Portfolio")
app.add_page(admin_page, route="/admin", title="Admin Panel")
