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


def admin_page() -> rx.Component:
    return rx.center(
        rx.vstack(
            navbar(),
            rx.heading("Admin Panel", size="7", margin_bottom="8"),
            rx.select(
                ["basics", "work"],
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

            footer(),
            **page_layout_style
        ),
        **page_wrapper_style
    )
