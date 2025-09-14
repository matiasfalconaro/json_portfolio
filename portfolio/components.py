import glob
import os
import reflex as rx

from .data import data
from .styles import *
from .states import States


def navbar() -> rx.Component:
    return rx.hstack(
        rx.hstack(
            rx.link("Home", href="/", **link_style),
            rx.link("Work", href="#work", **link_style),
            rx.link("Education", href="#education", **link_style),
            rx.link("Projects", href="#projects", **link_style),
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
    basics = data["basics"]
    return rx.cond(
        States.show_modal,
        rx.box(
            rx.box(
                rx.heading("Contact Information", **section_heading_style),

                rx.vstack(
                    rx.hstack(
                        rx.icon(tag="mail"),
                        rx.text(basics["email"]),
                        align_items="center"
                    ),
                    rx.hstack(
                        rx.icon(tag="phone"),
                        rx.text(basics.get("phone", "N/A")),
                        align_items="center"
                    ),
                    rx.hstack(
                        rx.icon(tag="map-pin"),
                        rx.text(
                            f"{basics['location']['city']}, "
                            f"{basics['location']['region']}, "
                            f"{basics['location']['countryCode']}"
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


def find_resume_pdf() -> str:
    """
    Finds matching file with 'resume' in its name.
    I want to keep track of my resumes version in their names, so names change.
    """
    pdf_files = glob.glob("**/*.pdf", recursive=True) # Returns a List of matching paths
    
    resume_files = [f for f in pdf_files if 'resume' in f.lower()]
    
    if resume_files:
        resume_files.sort(key=os.path.getmtime, reverse=True)
        return f"/{resume_files[0]}"
    
    return "/resume.pdf"


def header_section() -> rx.Component:
    """Render header with name/title aligned vertically center with image."""
    basics = data["basics"]
    
    resume_path = find_resume_pdf()

    return rx.vstack(
        rx.grid(
            rx.vstack(
                rx.heading(basics["name"], size="8"),
                rx.text(basics["label"], font_weight="bold"),

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
                        href=resume_path,
                        is_external=True,
                        download=True
                    ),
                    spacing="3"
                ),

                **header_text_block
            ),
            rx.box(
                rx.image(src=basics["image"], **header_image_style),
                display="flex",
                justify_content="flex-end"
            ),
            **header_grid_style
        ),
        rx.text(basics["summary"], **summary_text_style),
        **header_section_style
    )


def work_section() -> rx.Component:
    """Render the work experience section."""
    return rx.vstack(
        *[
            rx.box(
                rx.heading(f'{job["position"]} @ {job["name"]}',
                           **work_heading_style),
                rx.text(
                    f'{job["startDate"]} – '
                    f'{job.get("endDate") or "Present"}'
                ),
                rx.box(height="1em"),
                rx.text(job["summary"]),
                rx.unordered_list(
                    *[rx.list_item(item) for item in job["highlights"]]
                ),
                **work_item_style
            )
            for job in data["work"]
        ],
        **work_section_style
    )


def education_section() -> rx.Component:
    """Render the education section."""
    return rx.vstack(
        *[
            rx.box(
                rx.heading(
                    f"{edu['studyType']} in {edu['area']}",
                    **heading_education_style
                ),
                rx.text(edu["institution"]),
                rx.text(f"{edu['startDate']} – {edu.get('endDate') or 'Present'}"),
                rx.text(f"GPA: {edu['score']}") if edu.get("score") else None,
                rx.unordered_list(
                    *[rx.list_item(course) for course in edu.get("courses", [])]
                ) if edu.get("courses") else None,
                **education_item_style
            )
            for edu in data["education"]
        ],
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
            for cert in data["certificates"]
        ],
        **certificates_section_style
    )


def project_section() -> rx.Component:
    """Render the projects section in a grid of cards."""
    return rx.box(
        rx.flex(
            *[
                rx.box(
                    rx.vstack(
                        rx.heading(project["name"], **project_heading_style),
                        rx.text(project["description"]),
                        rx.hstack(
                            *[
                                rx.box(
                                    tech,
                                    **tech_tag_style
                                )
                                for tech in project["highlights"]
                            ],
                            **tech_tag_container_style
                        ),
                        rx.text(project["role"], font_weight="bold"),
                        (
                            rx.link(
                                "GitHub",
                                href=project["github"],
                                is_external=True
                            )
                            if project.get("github") 
                               and project["github"].startswith("http")
                            else (
                                rx.text("Code under NDA", font_style="italic")
                                if project.get("github") == "NDA"
                                else None
                            )
                        ),
                        **project_content_style
                    ),
                    **project_card_style
                )
                for project in data["projects"]
            ],
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