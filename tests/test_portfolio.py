import reflex as rx

from typing import Any
from portfolio.portfolio import index
from portfolio.components import footer, navbar


def test_index_page_component() -> None:
    """
    Test that index, navbar, and footer components are Reflex components.
    """
    comp: rx.Component = index()
    assert isinstance(comp, rx.Component)

    nav: rx.Component = navbar()
    assert isinstance(nav, rx.Component)

    ft: rx.Component = footer()
    assert isinstance(ft, rx.Component)


def component_contains_text(comp: Any, text: str) -> bool:
    """
    Recursively search a Reflex component and its children for a specific text.
    """
    if hasattr(comp, "children"):
        for child in comp.children:
            if isinstance(child, str) and text in child:
                return True
            elif component_contains_text(child, text):
                return True
    return False


def test_footer_text() -> None:
    """
    Test that the footer component contains the expected copyright text.
    """
    ft: rx.Component = footer()
    text: str = str(ft).encode().decode("unicode_escape")
    assert "© 2025 Matias Falconaro." in text
