import reflex as rx
import json

from pathlib import Path
from typing import Any


def load_portfolio() -> dict[str, Any]:
    """Load portfolio data from the resume.json file."""
    with open(Path(__file__).parent / "resume.json", "r", encoding="utf-8") as f:
        return json.load(f)


data = load_portfolio()


def navbar() -> rx.Component:
    return rx.hstack(
        rx.hstack(
            rx.link("Work", href="#work"),
            rx.link("Education", href="#education"),
            rx.link("Projects", href="#projects"),
            rx.link("Contact", href="#contact"),
            spacing="6"
        ),

        rx.spacer(),

        rx.hstack(
            rx.link(
                rx.image(src="/github.svg", width="20px", height="20px"),
                is_external=True
            ),
            rx.link(
                rx.image(src="/linkedin.svg", width="20px", height="20px"),
                is_external=True
            ),
            spacing="3"
        ),

        padding="4",
        border_bottom="1px solid #e2e8f0",
        position="sticky",
        top="0",
        z_index="10",
        background_color="white",
        width="100%",
        align="center"
    )


def header_section() -> rx.Component:
    """Render header with name/title aligned vertically center with image."""
    basics = data["basics"]

    return rx.vstack(
        rx.grid(
            rx.vstack(
                rx.heading(basics["name"], size="7"),
                rx.text(basics["label"]),
                spacing="2",
                align="start"
            ),
            rx.box(
                rx.image(
                    src=basics["image"],
                    width="150px",
                    border_radius="5px"
                ),
                display="flex",
                justify_content="flex-end"
            ),
            columns="2",
            spacing="4",
            width="100%",
            align_items="center"
        ),

        rx.text(
            basics["summary"],
            max_width="800px",
            text_align="start"
        ),

        spacing="4",
        align="start",
        padding="4"
    )


def education_section() -> rx.Component:
    """Render the education section."""
    return rx.vstack(
        *[rx.box(
            rx.heading(f"{edu['studyType']} in {edu['area']}", size="5"),
            rx.text(edu["institution"]),
            rx.text(f"{edu['startDate']} – {edu.get('endDate') or 'Present'}"),
            rx.text(f"GPA: {edu['score']}") if edu.get("score") else None,
            rx.unordered_list(
                *[rx.list_item(course) for course in edu.get("courses", [])]
            ) if edu.get("courses") else None,
            margin_bottom="6"
        )
        for edu in data["education"]],
        spacing="4",
        align="start",
        width="100%",
        max_width="800px"
    )


def certificates_section() -> rx.Component:
    """Render the certificates section."""
    return rx.vstack(
        *[rx.box(
            rx.heading(cert["name"], size="5"),
            rx.text(f"Issued by {cert['issuer']} on {cert['date']}"),
            rx.link("View Certificate", href=cert["url"], is_external=True)
            if cert.get("url") else None,
            margin_bottom="4"
        )
        for cert in data["certificates"]],
        spacing="4",
        align="start",
        width="100%",
        max_width="800px"
    )


def work_section() -> rx.Component:
    """Render the work experience section."""
    return rx.vstack(
        *[rx.box(
            rx.heading(f'{job["position"]} @ {job["name"]}', size="5"),
            rx.text(
                f'{job["startDate"]} – '
                f'{job.get("endDate") or "Present"}'
            ),
            rx.text(job["summary"]),
            rx.unordered_list(
                *[rx.list_item(item) for item in job["highlights"]]
            ),
            margin_bottom="6"
        )
        for job in data["work"]],
        spacing="4",
        align="start",
        width="100%",
        max_width="800px"
    )


def project_section() -> rx.Component:
    """Render the projects section in a grid of cards."""
    return rx.box(
        rx.grid(
            *[
                rx.box(
                    rx.vstack(
                        rx.heading(project["name"], size="5"),
                        rx.text(project["description"]),

                        # Wrapp tech tags
                        rx.hstack(
                            *[
                                rx.box(
                                    tech,
                                    padding="5px",
                                    border_radius="5px",
                                    color="#2D3748",
                                    background_color="#EDF2F7",
                                    font_size="sm",
                                    font_weight="medium",
                                    margin="1",
                                    display="inline-block"
                                )
                                for tech in project["highlights"]
                            ],
                            wrap="wrap",
                            spacing="2"
                        ),

                        rx.text(project["role"], font_weight="bold"),

                        rx.link(
                            "GitHub",
                            href=project["github"],
                            is_external=True
                        ) if project.get("github") else None,

                        spacing="3",
                        align="start"
                    ),
                    padding="16px",
                    border="1px solid #e2e8f0",
                    border_radius="10px",
                    box_shadow="sm",
                    background_color="white",
                    width="100%",
                )
                for project in data["projects"]
            ],
            columns="3",
            spacing="4"
        )
    )


def footer() -> rx.Component:
    """Render footer."""
    return rx.vstack(
        rx.text("© 2025 Matias Falconaro.", font_size="sm"),
        spacing="2",
        padding="4",
        align="center",
        border_top="1px solid #e2e8f0",
        width="100%",
        background_color="#f7fafc"
    )


def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            navbar(),
            header_section(),
            rx.divider(),

            rx.heading("Work Experience", id="work", size="6"),
            work_section(),
            rx.divider(),

            rx.heading("Education", id="education", size="6"),
            education_section(),
            rx.divider(),

            rx.heading("Certificates", id="certificates", size="6"),
            certificates_section(),
            rx.divider(),

            rx.heading("Projects", id="projects", size="6"),
            project_section(),
            rx.divider(),

            footer(),

            spacing="6",
            align="center",
            width="100%",
            max_width="900px"
        ),
        padding="6",
        width="100%"
    )


# App Setup
app = rx.App()
app.add_page(index, title="Matias Falconaro | Portfolio")
