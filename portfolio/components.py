import reflex as rx

from database.repository import get_certificates
from .states import *
from .styles import *


def navbar() -> rx.Component:
    """Renders the navbar section."""
    return rx.hstack(
        rx.hstack(
            rx.link("Home", href="/", **link_style),
            rx.link("Work", href="/#work", **link_style),
            rx.link("Education", href="/#education", **link_style),
            rx.link("Projects", href="/#projects", **link_style),
            **nav_links_container       
        ),

        rx.spacer(),

        rx.hstack(
            rx.link(
                rx.image(src="/code.svg", **icon_image_size),
                on_click=States.toggle_code_modal,
                cursor="pointer"
            ),
            rx.link(
                rx.image(src="/github.svg", **icon_image_size),
                href="https://github.com/matiasfalconaro",
                is_external=True
            ),
            rx.link(
                rx.image(src="/linkedin.svg", **icon_image_size),
                href="https://www.linkedin.com/in/matiasfalconaro/",
                is_external=True
            ),
            **nav_icons_container
        ),

        **navbar_style
    )


def contact_modal() -> rx.Component:
    """Renders a modal dialog displaying contact information from the admin state."""
    return rx.cond(
        States.show_modal,
        rx.box(
            rx.box(
                rx.heading("Contact Information", **section_heading_style),
                rx.vstack(
                    rx.hstack(
                        rx.icon(tag="mail"),
                        rx.text(AdminState.basics.get("email", "")),
                        align_items="center"
                    ),
                    rx.hstack(
                        rx.icon(tag="phone"),
                        rx.text(AdminState.basics.get("phone", "")),
                        align_items="center"
                    ),
                    rx.hstack(
                        rx.icon(tag="map-pin"),
                        rx.text(
                            rx.cond(
                                AdminState.basics.get("location"),
                                AdminState.basics["location"].to(str),
                                "Location not available"
                            )
                        ),
                        align_items="center"
                    ),
                    **contact_info_style
                ),
                rx.center(
                    rx.button("Close",
                              on_click=States.toggle_modal,
                              **modal_button_style),
                    margin_top="16px"
                ),
                **modal_card_style
            ),
            **modal_overlay_style
        ),
        None
    )


def get_version() -> str:
    """Reeds version from file."""
    try:
        with open('version.txt', 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        return "dev"


def code_info_modal() -> rx.Component:
    """Renders a modal dialog displaying technical information about the application."""
    return rx.cond(
        States.show_code_modal,
        rx.box(
            rx.box(
                rx.heading("Page Info", **section_heading_style),

                rx.vstack(
                    rx.hstack(
                        rx.icon(tag="git-branch"),
                        rx.text(get_version()),
                        align_items="center"
                    ),
                    rx.hstack(
                        rx.image(src="/python.svg", width="1.25em", height="1.25em"),
                        rx.text("Python (Reflex)"),
                        align_items="center"
                    ),
                    rx.hstack(
                        rx.icon(tag="github"),
                        rx.link("Source code",
                                href="https://github.com/matiasfalconaro/json_portfolio",
                                is_external=True),
                        align_items="center"
                    ),
                    **contact_info_style
                ),

                rx.center(
                    rx.button("Close",
                              on_click=States.toggle_code_modal,
                              **modal_button_style),
                    margin_top="16px"
                ),

                **modal_card_style
            ),
            **modal_overlay_style
        ),
        None
    )


def header_section() -> rx.Component:
    """Renders the header section."""
    return rx.vstack(
        rx.grid(
            rx.vstack(
                rx.heading(AdminState.basics.get("name", ""), size="8"),
                rx.text(AdminState.basics.get("label", ""), font_weight="bold"),

                rx.hstack(
                    rx.button(
                        "Contact",
                        on_click=States.toggle_modal,
                        **contact_button_style
                    ),
                    rx.link(
                        rx.button(
                            rx.hstack(
                                rx.text("Resume"),
                                spacing="2",
                                align="center"
                            ),
                            **download_button_style
                        ),
                        href="/resume_v1.3.0.pdf",
                        is_external=True,
                        download=True
                    ),
                    rx.link(
                        rx.button(
                            "Admin",
                            **contact_button_style
                        ),
                        href="/admin"
                    ),
                    spacing="3"
                ),
                **header_text_block
            ),
            rx.box(
                rx.image(src=AdminState.basics.get("image", ""), **header_image_style),
                display="flex",
                justify_content="flex-end"
            ),
            **header_grid_style
        ),
        rx.text(AdminState.basics.get("summary", ""), **summary_text_style),
        **header_section_style
    )


def _render_work_item(job: dict) -> rx.Component:
    """Render a single work item."""
    position = job.get("position", "")
    name = job.get("name", "")
    start_date = job.get("startDate", "")
    end_date = job.get("endDate", "")
    summary = job.get("summary", "")
    highlights = job.get("highlights", [])
    
    if not isinstance(highlights, list):
        highlights = []
        
    return rx.box(
        rx.heading(f'{position} @ {name}', **work_heading_style),
        rx.cond(
            end_date,
            rx.text(f'{start_date} – {end_date}'),
            rx.text(f'{start_date} – Present')
        ),
        rx.box(height="1em"),
        rx.text(summary),
        rx.foreach(
            highlights,
            lambda highlight: rx.list_item(highlight)
        ),
        **work_item_style
    )


def work_section() -> rx.Component:
    """Renders the work experience section."""    
    return rx.vstack(
        rx.foreach(
            AdminState.work_items,
            _render_work_item
        ),
        **work_section_style
    )


def _render_education_item(edu: dict) -> rx.Component:
    """Render a single education item."""
    study_type = edu.get("studyType", "")
    area = edu.get("area", "")
    institution = edu.get("institution", "")
    start_date = edu.get("startDate", "")
    end_date = edu.get("endDate", "")
    score = edu.get("score", "")
    courses = edu.get("courses", [])
    
    if not isinstance(courses, list):
        courses = []
        
    return rx.box(
        rx.heading(
            f"{study_type} in {area}",
            **heading_education_style
        ),
        rx.text(institution),
        rx.cond(
            end_date,
            rx.text(f"{start_date} – {end_date}"),
            rx.text(f"{start_date} – Present")
        ),
        rx.cond(
            score,
            rx.text(f"GPA: {score}"),
            None
        ),
        rx.cond(
            courses,
            rx.unordered_list(
                rx.foreach(
                    courses,
                    lambda course: rx.list_item(course)
                )
            ),
            None
        ),
        **education_item_style
    )

def education_section() -> rx.Component:
    """Render the education section using state."""    
    return rx.vstack(
        rx.foreach(
            AdminState.education_items,
            _render_education_item
        ),
        **education_section_style
    )


def certificates_section() -> rx.Component:
    """Render the certificates section."""
    return rx.vstack(
        *[
            rx.box(
                rx.heading(cert["name"], **certificate_heading_style),
                rx.text(f"Issued by {cert['issuer']} on {cert['date']}"),
                rx.link(
                    "View Certificate",
                    href=cert["url"],
                    is_external=True
                ) if cert.get("url") else None,
                **certificate_item_style
            )
            for cert in get_certificates()
        ],
        **certificates_section_style
    )


def _render_project_item(project: dict) -> rx.Component:
    """Render a single project item."""
    name = project.get("name", "")
    description = project.get("description", "")
    highlights = project.get("highlights", [])
    role = project.get("role", "")
    github = project.get("github", "")
    
    if not isinstance(highlights, list):
        highlights = []

    github_component = rx.cond(
        github == "NDA",
        rx.text("Code under NDA", font_style="italic"),
        rx.cond(
            github != "",
            rx.link("GitHub", href=github, is_external=True),
            None
        )
    )
        
    return rx.box(
        rx.vstack(
            rx.heading(name, **project_heading_style),
            rx.text(description),
            rx.hstack(
                rx.foreach(
                    highlights,
                    lambda tech: rx.box(
                        tech,
                        **tech_tag_style
                    )
                ),
                **tech_tag_container_style
            ),
            rx.text(role, font_weight="bold"),
            github_component,
            **project_content_style
        ),
        **project_card_style
    )


def project_section() -> rx.Component:
    """Render the projects section using state."""    
    return rx.box(
        rx.flex(
            rx.foreach(
                AdminState.project_items,
                _render_project_item
            ),
            **project_flex_container
        ),
        width="100%"
    )


def footer() -> rx.Component:
    """Render footer."""
    return rx.vstack(
        rx.text("© 2025 Matias Falconaro.", **footer_text_style),
        **footer_style
    )
