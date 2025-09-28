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
        
        # Work Items Section
        rx.cond(
            AdminState.selected_collection == "work",
            rx.vstack(
                rx.hstack(
                    rx.text("Work Items", **item_list_title_style),
                    rx.spacer(),
                    rx.button(
                        "+ New",
                        on_click=AdminState.create_new_work_item,
                        size="2",
                        color_scheme="green"
                    ),
                    width="100%"
                ),
                rx.foreach(
                    AdminState.work_items,
                    lambda item, i: rx.hstack(
                        rx.button(
                            rx.text(
                                item['position'] + " @ " + item['name'],
                                overflow="hidden",
                                text_overflow="ellipsis", 
                                white_space="nowrap",
                            ),
                            on_click=lambda e, idx=i: AdminState.select_work_item(idx),
                            color_scheme=rx.cond(
                                (AdminState.work_edit.get("name") == item["name"]) & ~AdminState.is_creating_work,
                                "blue",
                                "gray"
                            ),
                            **item_button_style
                        ),
                        rx.button(
                            "×",
                            on_click=lambda e, idx=i: AdminState.delete_work_item(idx),
                            size="1",
                            color_scheme="red",
                            margin_left="2",
                            min_width="30px"
                        ),
                        width="100%",
                        align_items="center",
                        spacing="2"
                    ),
                ),
                **item_list_container_style
            )
        ),
        
        # Education Items Section  
        rx.cond(
            AdminState.selected_collection == "education",
            rx.vstack(
                rx.hstack(
                    rx.text("Education Items", **item_list_title_style),
                    rx.spacer(),
                    rx.button(
                        "+ New",
                        on_click=AdminState.create_new_education_item,
                        size="2",
                        color_scheme="green"
                    ),
                    width="100%"
                ),
                rx.foreach(
                    AdminState.education_items,
                    lambda item, i: rx.hstack(
                        rx.button(
                            rx.text(
                                item['studyType'] + " @ " + item['institution'],
                                overflow="hidden",
                                text_overflow="ellipsis",
                                white_space="nowrap",
                            ),
                            on_click=lambda e, idx=i: AdminState.select_education_item(idx),
                            color_scheme=rx.cond(
                                (AdminState.education_edit.get("institution") == item["institution"]) & ~AdminState.is_creating_education,
                                "blue",
                                "gray"
                            ),
                            **item_button_style
                        ),
                        rx.button(
                            "×", 
                            on_click=lambda e, idx=i: AdminState.delete_education_item(idx),
                            size="1",
                            color_scheme="red",
                            margin_left="2",
                            min_width="30px"
                        ),
                        width="100%",
                        align_items="center",
                        spacing="2"
                    ),
                ),
                **item_list_container_style
            )
        ),
        
        # Project Items Section
        rx.cond(
            AdminState.selected_collection == "projects", 
            rx.vstack(
                rx.hstack(
                    rx.text("Project Items", **item_list_title_style),
                    rx.spacer(),
                    rx.button(
                        "+ New",
                        on_click=AdminState.create_new_project_item,
                        size="2",
                        color_scheme="green"
                    ),
                    width="100%"
                ),
                rx.foreach(
                    AdminState.project_items,
                    lambda item, i: rx.hstack(
                        rx.button(
                            rx.text(
                                item['name'],
                                overflow="hidden",
                                text_overflow="ellipsis",
                                white_space="nowrap", 
                            ),
                            on_click=lambda e, idx=i: AdminState.select_project_item(idx),
                            color_scheme=rx.cond(
                                (AdminState.project_edit.get("name") == item["name"]) & ~AdminState.is_creating_project,
                                "blue",
                                "gray"
                            ),
                            **item_button_style
                        ),
                        rx.button(
                            "×",
                            on_click=lambda e, idx=i: AdminState.delete_project_item(idx),
                            size="1",
                            color_scheme="red",
                            margin_left="2",
                            min_width="30px"
                        ),
                        width="100%",
                        align_items="center",
                        spacing="2"
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
        # Creation banners
        rx.cond(
            (AdminState.selected_collection == "work") & AdminState.is_creating_work,
            rx.callout(
                "Creating new work experience - fill out the form and click Create",
                icon="plus",
                color_scheme="blue",
                width="100%"
            )
        ),
        rx.cond(
            (AdminState.selected_collection == "education") & AdminState.is_creating_education,
            rx.callout(
                "Creating new education entry - fill out the form and click Create", 
                icon="plus",
                color_scheme="blue",
                width="100%"
            )
        ),
        rx.cond(
            (AdminState.selected_collection == "projects") & AdminState.is_creating_project,
            rx.callout(
                "Creating new project - fill out the form and click Create",
                icon="plus", 
                color_scheme="blue",
                width="100%"
            )
        ),

        # Editing banners
        rx.cond(
            (AdminState.selected_collection == "work") & ~AdminState.is_creating_work,
            rx.callout(
                f"Editing: {AdminState.work_edit.get('position', '')} @ {AdminState.work_edit.get('name', '')}",
                icon="pencil",
                color_scheme="green",
                width="100%"
            )
        ),
        rx.cond(
            (AdminState.selected_collection == "education") & ~AdminState.is_creating_education,
            rx.callout(
                f"Editing: {AdminState.education_edit.get('studyType', '')} @ {AdminState.education_edit.get('institution', '')}",
                icon="pencil",
                color_scheme="green",
                width="100%"
            )
        ),
        rx.cond(
            (AdminState.selected_collection == "projects") & ~AdminState.is_creating_project,
            rx.callout(
                f"Editing: {AdminState.project_edit.get('name', '')}",
                icon="pencil",
                color_scheme="green",
                width="100%"
            )
        ),

        # Form content
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

        # Action buttons
        rx.center(
            # Basics
            rx.cond(
                AdminState.selected_collection == "basics",
                rx.button("Save Basics", on_click=AdminState.save_basics, **save_button_style)
            ),
            
            # Work
            rx.cond(
                AdminState.selected_collection == "work", 
                rx.hstack(
                    rx.cond(
                        AdminState.is_creating_work,
                        rx.button("Create Work", on_click=AdminState.save_work, color_scheme="green", **save_button_style),
                        rx.button("Update Work", on_click=AdminState.save_work, color_scheme="blue", **save_button_style)
                    ),
                    spacing="3"
                )
            ),
            
            # Education
            rx.cond(
                AdminState.selected_collection == "education",
                rx.hstack(
                    rx.cond(
                        AdminState.is_creating_education,
                        rx.button("Create Education", on_click=AdminState.save_education, color_scheme="green", **save_button_style),
                        rx.button("Update Education", on_click=AdminState.save_education, color_scheme="blue", **save_button_style)
                    ),
                    spacing="3"
                )
            ),
            
            # Projects
            rx.cond(
                AdminState.selected_collection == "projects",
                rx.hstack(
                    rx.cond(
                        AdminState.is_creating_project,
                        rx.button("Create Project", on_click=AdminState.save_project, color_scheme="green", **save_button_style),
                        rx.button("Update Project", on_click=AdminState.save_project, color_scheme="blue", **save_button_style)
                    ),
                    spacing="3"
                )
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