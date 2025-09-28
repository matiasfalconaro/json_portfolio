import reflex as rx

from .components import (navbar,
                         footer,
                         AdminState)
from .styles import *


def basics_editor() -> rx.Component:
    """Render the Basics collection editor."""
    return rx.vstack(
        rx.text("Basic Information", **section_title_style),
        rx.input(
            placeholder="Name",
            value=AdminState.basics_edit.get("name", ""),
            on_change=lambda e: AdminState.update_basics_field("name", e),
            **input_style
        ),
        rx.input(
            placeholder="Label",
            value=AdminState.basics_edit.get("label", ""),
            on_change=lambda e: AdminState.update_basics_field("label", e),
            **input_style
        ),
        rx.input(
            placeholder="Email",
            value=AdminState.basics_edit.get("email", ""),
            on_change=lambda e: AdminState.update_basics_field("email", e),
            **input_style
        ),
        rx.text_area(
            placeholder="Summary",
            value=AdminState.basics_edit.get("summary", ""),
            on_change=lambda e: AdminState.update_basics_field("summary", e),
            height="200px",
            **text_area_style
        ),
        **editor_container_style
    )


def work_editor() -> rx.Component:
    """Render the Work collection editor."""
    return rx.vstack(
        rx.text("Work Experience", **section_title_style),
        rx.input(
            placeholder="Company Name",
            value=AdminState.work_edit.get("name", ""),
            on_change=lambda e: AdminState.update_work_field("name", e),
            **input_style
        ),
        rx.input(
            placeholder="Position",
            value=AdminState.work_edit.get("position", ""),
            on_change=lambda e: AdminState.update_work_field("position", e),
            **input_style
        ),
        rx.input(
            placeholder="Start Date",
            value=AdminState.work_edit.get("startDate", ""),
            on_change=lambda e: AdminState.update_work_field("startDate", e),
            **input_style
        ),
        rx.input(
            placeholder="End Date",
            value=AdminState.work_edit.get("endDate", ""),
            on_change=lambda e: AdminState.update_work_field("endDate", e),
            **input_style
        ),
        rx.text_area(
            placeholder="Summary",
            value=AdminState.work_edit.get("summary", ""),
            on_change=lambda e: AdminState.update_work_field("summary", e),
            height="200px",
            **text_area_style
        ),
        **editor_container_style
    )


def education_editor() -> rx.Component:
    """Render the Education collection editor."""
    return rx.vstack(
        rx.text("Education", **section_title_style),
        rx.input(
            placeholder="Institution",
            value=AdminState.education_edit.get("institution", ""),
            on_change=lambda e: AdminState.update_education_field("institution", e),
            **input_style
        ),
        rx.input(
            placeholder="Area of Study",
            value=AdminState.education_edit.get("area", ""),
            on_change=lambda e: AdminState.update_education_field("area", e),
            **input_style
        ),
        rx.input(
            placeholder="Study Type",
            value=AdminState.education_edit.get("studyType", ""),
            on_change=lambda e: AdminState.update_education_field("studyType", e),
            **input_style
        ),
        rx.input(
            placeholder="Start Date",
            value=AdminState.education_edit.get("startDate", ""),
            on_change=lambda e: AdminState.update_education_field("startDate", e),
            **input_style
        ),
        rx.input(
            placeholder="End Date",
            value=AdminState.education_edit.get("endDate", ""),
            on_change=lambda e: AdminState.update_education_field("endDate", e),
            **input_style
        ),
        rx.input(
            placeholder="GPA/Score",
            value=AdminState.education_edit.get("score", ""),
            on_change=lambda e: AdminState.update_education_field("score", e),
            **input_style
        ),
        rx.text_area(
            placeholder="Courses (comma-separated)",
            value=AdminState.courses_str,
            on_change=lambda e: AdminState.update_education_courses(e),
            height="200px",
            **text_area_style
        ),
        **editor_container_style
    )


def projects_editor() -> rx.Component:
    """Render the Projects collection editor."""
    return rx.vstack(
        rx.text("Project Details", **section_title_style),
        rx.input(
            placeholder="Project Name",
            value=AdminState.project_edit.get("name", ""),
            on_change=lambda e: AdminState.update_project_field("name", e),
            **input_style
        ),
        rx.input(
            placeholder="Role",
            value=AdminState.project_edit.get("role", ""),
            on_change=lambda e: AdminState.update_project_field("role", e),
            **input_style
        ),
        rx.input(
            placeholder="GitHub URL",
            value=AdminState.project_edit.get("github", ""),
            on_change=lambda e: AdminState.update_project_field("github", e),
            **input_style
        ),
        rx.text_area(
            placeholder="Description",
            value=AdminState.project_edit.get("description", ""),
            on_change=lambda e: AdminState.update_project_field("description", e),
            height="120px",
            **text_area_style
        ),
        rx.text_area(
            placeholder="Technologies (comma-separated)",
            value=AdminState.highlights_str,
            on_change=lambda e: AdminState.update_project_highlights(e),
            height="100px",
            **text_area_style
        ),
        rx.hstack(
            rx.checkbox(
                "Is Active",
                checked=AdminState.project_edit.get("isActive", False),
                on_change=lambda e: AdminState.update_project_is_active(e),
                **checkbox_style
            ),
            **checkbox_container_style
        ),
        **editor_container_style
    )


def sidebar_navigation() -> rx.Component:
    """Sidebar navigation with collection buttons and item selection."""
    return rx.vstack(
        rx.text("Sections", **item_list_title_style),
        rx.button(
            "Basics",
            on_click=lambda: AdminState.load_collection("basics"),
            color_scheme=rx.cond(AdminState.selected_collection == "basics", "blue", "gray"),
            **sidebar_button_style
        ),
        rx.button(
            "Work",
            on_click=lambda: AdminState.load_collection("work"),
            color_scheme=rx.cond(AdminState.selected_collection == "work", "blue", "gray"),
            **sidebar_button_style
        ),
        rx.button(
            "Education",
            on_click=lambda: AdminState.load_collection("education"),
            color_scheme=rx.cond(AdminState.selected_collection == "education", "blue", "gray"),
            **sidebar_button_style
        ),
        rx.button(
            "Projects",
            on_click=lambda: AdminState.load_collection("projects"),
            color_scheme=rx.cond(AdminState.selected_collection == "projects", "blue", "gray"),
            **sidebar_button_style
        ),
        
        rx.box(height="24px"),
        
        rx.cond(
            AdminState.selected_collection == "work",
            rx.vstack(
                rx.text("Work Items", **item_list_title_style),
                rx.foreach(
                    AdminState.work_items,
                    lambda item, i: rx.button(
                        rx.text(
                            item['position'] + " @ " + item['name'],
                            overflow="hidden",
                            text_overflow="ellipsis",
                            white_space="nowrap",
                        ),
                        on_click=lambda e, idx=i: AdminState.select_work_item(idx),
                        **item_button_style
                    ),
                ),
                **item_list_container_style
            )
        ),
        
        rx.cond(
            AdminState.selected_collection == "education",
            rx.vstack(
                rx.text("Education Items", **item_list_title_style),
                rx.foreach(
                    AdminState.education_items,
                    lambda item, i: rx.button(
                        rx.text(
                            item['studyType'] + " @ " + item['institution'],
                            overflow="hidden",
                            text_overflow="ellipsis",
                            white_space="nowrap",
                        ),
                        on_click=lambda e, idx=i: AdminState.select_education_item(idx),
                        **item_button_style
                    ),
                ),
                **item_list_container_style
            )
        ),
        
        rx.cond(
            AdminState.selected_collection == "projects",
            rx.vstack(
                rx.text("Project Items", **item_list_title_style),
                rx.foreach(
                    AdminState.project_items,
                    lambda item, i: rx.button(
                        rx.text(
                            item['name'],
                            overflow="hidden",
                            text_overflow="ellipsis",
                            white_space="nowrap",
                        ),
                        on_click=lambda e, idx=i: AdminState.select_project_item(idx),
                        **item_button_style
                    ),
                ),
                **item_list_container_style
            )
        ),
        
        **sidebar_container_style
    )


def main_content() -> rx.Component:
    """Main content area with form fields."""
    return rx.vstack(
        rx.cond(
            AdminState.selected_collection == "basics",
            rx.box(
                basics_editor(),
                **content_box_style
            )
        ),
        rx.cond(
            AdminState.selected_collection == "work",
            rx.box(
                work_editor(),
                **content_box_style
            )
        ),
        rx.cond(
            AdminState.selected_collection == "education",
            rx.box(
                education_editor(),
                **content_box_style
            )
        ),
        rx.cond(
            AdminState.selected_collection == "projects",
            rx.box(
                projects_editor(),
                **content_box_style
            )
        ),

        rx.center(
            rx.cond(
                AdminState.selected_collection == "basics",
                rx.button("Save Basics", on_click=AdminState.save_basics, **save_button_style)
            ),
            rx.cond(
                AdminState.selected_collection == "work",
                rx.button("Save Work", on_click=AdminState.save_work, **save_button_style)
            ),
            rx.cond(
                AdminState.selected_collection == "education",
                rx.button("Save Education", on_click=AdminState.save_education, **save_button_style)
            ),
            rx.cond(
                AdminState.selected_collection == "projects",
                rx.button("Save Project", on_click=AdminState.save_project, **save_button_style)
            ),
            **save_button_container_style
        ),
        
        **main_content_style
    )


def admin_page() -> rx.Component:
    """Admin page component with two-column layout."""
    return rx.vstack(
        navbar(),
        rx.hstack(
            sidebar_navigation(),
            main_content(),
            **admin_layout_style
        ),
        footer(),
        **admin_page_style,
        on_mount=AdminState.on_mount
    )