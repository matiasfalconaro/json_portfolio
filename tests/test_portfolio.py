import reflex as rx

from portfolio.portfolio import index
from portfolio.components import footer, navbar


def test_index_page_component():
    comp = index()
    assert isinstance(comp, rx.Component)
    
    nav = navbar()
    assert isinstance(nav, rx.Component)
    
    ft = footer()
    assert isinstance(ft, rx.Component)


def component_contains_text(comp, text):
    if hasattr(comp, "children"):
        for child in comp.children:
            if isinstance(child, str) and text in child:
                return True
            elif component_contains_text(child, text):
                return True
    return False


def test_footer_text():
    ft = footer()
    text = str(ft).encode().decode("unicode_escape")
    assert "© 2025 Matias Falconaro." in text
