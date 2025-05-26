import reflex as rx
import json

from pathlib import Path
from typing import Any


def load_portfolio() -> dict[str, Any]:
    """Load portfolio data from the resume.json file."""
    with open(
        Path(__file__).parent / "resume.json",
        "r",
        encoding="utf-8"
    ) as f:
        return json.load(f)


data = load_portfolio()


def header_section() -> rx.Component:
    """Render the header with image, name, title, summary, and links."""
    basics = data["basics"]
    return rx.vstack(
        rx.image(
            src=basics["image"],
            width="150px",
            border_radius="full"
        ),
        rx.heading(basics["name"], size="7"),
        rx.text(basics["label"]),
        rx.text(
            basics["summary"],
            max_width="700px",
            text_align="center"
        ),
        rx.hstack(
            *[
                rx.link(
                    p["network"],
                    href=p["url"],
                    is_external=True
                )
                for p in basics["profiles"]
            ],
            spacing="4"
        ),
        spacing="4",
        align="center",
        padding="4"
    )


def work_section() -> rx.Component:
    """Render the work experience section."""
    return rx.vstack(
        *[
            rx.box(
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
            for job in data["work"]
        ],
        spacing="4",
        align="start",
        width="100%",
        max_width="800px"
    )


def project_section() -> rx.Component:
    """Render the projects section."""
    return rx.box(
        rx.heading("Projects", size="6"),
        *[
            rx.box(
                rx.heading(project["name"], size="5"),
                rx.text(project["description"]),
                rx.unordered_list(
                    *[
                        rx.list_item(item)
                        for item in project["highlights"]
                    ]
                ),
                rx.text(f'Role: {project["role"]}'),
                rx.link(
                    "GitHub",
                    href=project["github"],
                    is_external=True
                )
                if project.get("github") else None,
                margin_y="4"
            )
            for project in data["projects"]
        ]
    )


def index() -> rx.Component:
    """Truly centered layout with constrained section width and spacing."""
    return rx.center(
        rx.vstack(
            header_section(),
            rx.divider(),

            rx.heading("Work Experience", size="6"),
            work_section(),

            rx.divider(),

            rx.heading("Projects", size="6"),
            project_section(),

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
