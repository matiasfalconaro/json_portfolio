import reflex as rx

from database.repository import (get_certificates)
from .states import *
from .styles import *


def navbar() -> rx.Component:
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
    location = AdminState.basics["location"].to(dict)
    return rx.cond(
        States.show_modal,
        rx.box(
            rx.box(
                rx.heading("Contact Information", **section_heading_style),
                rx.vstack(
                    rx.hstack(
                        rx.icon(tag="mail"),
                        rx.text(AdminState.basics["email"].to(str)),
                        align_items="center"
                    ),
                    rx.hstack(
                        rx.icon(tag="phone"),
                        rx.text(AdminState.basics.get("phone", "").to(str)),
                        align_items="center"
                    ),
                    rx.hstack(
                        rx.icon(tag="map-pin"),
                        rx.text([
                            location.get("city", ""), ", ",
                            location.get("region", ""), ", ",
                            location.get("countryCode", "")
                        ]),
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
    """Lee la versión desde un archivo."""
    try:
        with open('version.txt', 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        return "dev"


def code_info_modal() -> rx.Component:
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


def work_section() -> rx.Component:
    return rx.vstack(
        rx.foreach(
            AdminState.work_items,
            lambda job: rx.box(
                rx.heading(f'{job["position"]} @ {job["name"]}', **work_heading_style),
                rx.cond(
                    job["endDate"],
                    rx.text(f'{job["startDate"]} – {job["endDate"]}'),
                    rx.text(f'{job["startDate"]} – Present')
                ),
                rx.box(height="1em"),
                rx.text(job["summary"]),
                rx.foreach(
                    job["highlights"],
                    lambda highlight: rx.list_item(highlight)
                ),
                **work_item_style
            )
        ),
        **work_section_style
    )


def education_section() -> rx.Component:
    """Render the education section using state."""
    return rx.vstack(
        rx.foreach(
            AdminState.education_items,
            lambda edu: rx.box(
                rx.heading(
                    f"{edu['studyType']} in {edu['area']}",
                    **heading_education_style
                ),
                rx.text(edu["institution"]),
                rx.cond(
                    edu["endDate"],
                    rx.text(f"{edu['startDate']} – {edu['endDate']}"),
                    rx.text(f"{edu['startDate']} – Present")
                ),
                rx.cond(
                    edu["score"],
                    rx.text(f"GPA: {edu['score']}"),
                    None
                ),
                rx.cond(
                    edu["courses"],
                    rx.unordered_list(
                        rx.foreach(
                            edu["courses"],
                            lambda course: rx.list_item(course)
                        )
                    ),
                    None
                ),
                **education_item_style
            )
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


def project_section() -> rx.Component:
    """Render the projects section using state."""
    return rx.box(
        rx.flex(
            rx.foreach(
                AdminState.project_items,
                lambda project: rx.box(
                    rx.vstack(
                        rx.heading(project["name"], **project_heading_style),
                        rx.text(project["description"]),
                        rx.hstack(
                            rx.foreach(
                                project["highlights"],
                                lambda tech: rx.box(
                                    tech,
                                    **tech_tag_style
                                )
                            ),
                            **tech_tag_container_style
                        ),
                        rx.text(project["role"], font_weight="bold"),
                        rx.cond(
                            project["github"].startswith("http"),
                            rx.link(
                                "GitHub",
                                href=project["github"],
                                is_external=True
                            ),
                            rx.cond(
                                project["github"] == "NDA",
                                rx.text("Code under NDA", font_style="italic"),
                                None
                            )
                        ),
                        **project_content_style
                    ),
                    **project_card_style
                )
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
