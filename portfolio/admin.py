import reflex as rx

from .components import (navbar,
                         footer,
                         AdminState)
from .styles import *


def basics_editor() -> rx.Component:
    """Render the Basics collection editor."""
    return rx.vstack(
        rx.input(
            placeholder="Name",
            value=AdminState.basics_edit.get("name", ""),
            on_change=lambda e: AdminState.update_basics_field("name", e),
        ),
        rx.input(
            placeholder="Label",
            value=AdminState.basics_edit.get("label", ""),
            on_change=lambda e: AdminState.update_basics_field("label", e),
        ),
        rx.input(
            placeholder="Email",
            value=AdminState.basics_edit.get("email", ""),
            on_change=lambda e: AdminState.update_basics_field("email", e),
        ),
        rx.text_area(
            placeholder="Summary",
            value=AdminState.basics_edit.get("summary", ""),
            on_change=lambda e: AdminState.update_basics_field("summary", e),
        ),
        rx.button("Save Basics", on_click=AdminState.save_basics),
        spacing="3",
    )


def work_editor() -> rx.Component:
    """Render the Work collection editor."""
    return rx.vstack(
        rx.foreach(
            AdminState.work_items,
            lambda item, i: rx.button(
                f"{item['position']} @ {item['name']}",
                on_click=lambda e, idx=i: AdminState.select_work_item(idx),
            ),
        ),
        rx.input(
            placeholder="Company Name",
            value=AdminState.work_edit.get("name", ""),
            on_change=lambda e: AdminState.update_work_field("name", e),
        ),
        rx.input(
            placeholder="Position",
            value=AdminState.work_edit.get("position", ""),
            on_change=lambda e: AdminState.update_work_field("position", e),
        ),
        rx.input(
            placeholder="Start Date",
            value=AdminState.work_edit.get("startDate", ""),
            on_change=lambda e: AdminState.update_work_field("startDate", e),
        ),
        rx.input(
            placeholder="End Date",
            value=AdminState.work_edit.get("endDate", ""),
            on_change=lambda e: AdminState.update_work_field("endDate", e),
        ),
        rx.text_area(
            placeholder="Summary",
            value=AdminState.work_edit.get("summary", ""),
            on_change=lambda e: AdminState.update_work_field("summary", e),
        ),
        rx.button("Save Work", on_click=AdminState.save_work),
        spacing="3",
    )


def education_editor() -> rx.Component:
    """Render the Education collection editor."""
    return rx.vstack(
        rx.foreach(
            AdminState.education_items,
            lambda item, i: rx.button(
                f"{item['studyType']} @ {item['institution']}",
                on_click=lambda e, idx=i: AdminState.select_education_item(idx),
            ),
        ),
        rx.input(
            placeholder="Institution",
            value=AdminState.education_edit.get("institution", ""),
            on_change=lambda e: AdminState.update_education_field("institution", e),
        ),
        rx.input(
            placeholder="Area of Study",
            value=AdminState.education_edit.get("area", ""),
            on_change=lambda e: AdminState.update_education_field("area", e),
        ),
        rx.input(
            placeholder="Study Type",
            value=AdminState.education_edit.get("studyType", ""),
            on_change=lambda e: AdminState.update_education_field("studyType", e),
        ),
        rx.input(
            placeholder="Start Date",
            value=AdminState.education_edit.get("startDate", ""),
            on_change=lambda e: AdminState.update_education_field("startDate", e),
        ),
        rx.input(
            placeholder="End Date",
            value=AdminState.education_edit.get("endDate", ""),
            on_change=lambda e: AdminState.update_education_field("endDate", e),
        ),
        rx.input(
            placeholder="GPA/Score",
            value=AdminState.education_edit.get("score", ""),
            on_change=lambda e: AdminState.update_education_field("score", e),
        ),
        rx.text_area(
            placeholder="Courses (comma-separated)",
            value=AdminState.courses_str,
            on_change=lambda e: AdminState.update_education_courses(e),
        ),
        rx.button("Save Education", on_click=AdminState.save_education),
        spacing="3",
    )


def projects_editor() -> rx.Component:
    """Render the Projects collection editor."""
    return rx.vstack(
        rx.foreach(
            AdminState.project_items,
            lambda item, i: rx.button(
                f"{item['name']}",
                on_click=lambda e, idx=i: AdminState.select_project_item(idx),
            ),
        ),
        rx.input(
            placeholder="Project Name",
            value=AdminState.project_edit.get("name", ""),
            on_change=lambda e: AdminState.update_project_field("name", e),
        ),
        rx.input(
            placeholder="Role",
            value=AdminState.project_edit.get("role", ""),
            on_change=lambda e: AdminState.update_project_field("role", e),
        ),
        rx.text_area(
            placeholder="Description",
            value=AdminState.project_edit.get("description", ""),
            on_change=lambda e: AdminState.update_project_field("description", e),
        ),
        rx.text_area(
            placeholder="Technologies (comma-separated)",
            value=AdminState.highlights_str,
            on_change=lambda e: AdminState.update_project_highlights(e),
        ),
        rx.input(
            placeholder="GitHub URL",
            value=AdminState.project_edit.get("github", ""),
            on_change=lambda e: AdminState.update_project_field("github", e),
        ),
        rx.checkbox(
            "Is Active",
            checked=AdminState.project_edit.get("isActive", False),
            on_change=lambda e: AdminState.update_project_is_active(e),
        ),
        rx.button("Save Project", on_click=AdminState.save_project),
        spacing="3",
    )


def admin_page() -> rx.Component:
    """Admin page component with on_mount handled internally."""
    return rx.center(
        rx.vstack(
            navbar(),
            rx.heading("Admin Panel", size="7", margin_bottom="8"),
            rx.select(
                ["basics", "work", "education", "projects"],
                value=AdminState.selected_collection,
                on_change=lambda e: AdminState.load_collection(e),
            ),

            rx.cond(
                AdminState.selected_collection == "basics",
                basics_editor()
            ),
            rx.cond(
                AdminState.selected_collection == "work",
                work_editor()
            ),
            rx.cond(
                AdminState.selected_collection == "education",
                education_editor()
            ),
            rx.cond(
                AdminState.selected_collection == "projects",
                projects_editor()
            ),

            footer(),
            **page_layout_style
        ),
        **page_wrapper_style,
        on_mount=AdminState.on_mount
    )