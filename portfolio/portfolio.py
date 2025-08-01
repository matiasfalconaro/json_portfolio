import reflex as rx

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

            rx.heading("Certificates",
                       id="certificates",
                       **section_heading_style),
            certificates_section(),
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
        **page_wrapper_style
    )


# App Setup
app = rx.App()
app.add_page(index, title="Matias Falconaro | Portfolio")
