import reflex as rx

from pathlib import Path
from pytest_bdd import scenarios, given, when, then
from typing import Any, List, Tuple, Dict
from portfolio.portfolio import index
from portfolio.components import footer, navbar


FEATURE_FILE = Path(__file__).parent.parent / "features" / "portfolio.feature"
scenarios(str(FEATURE_FILE))


@given("I have the portfolio page components", target_fixture="portfolio_components")
def portfolio_components() -> List[Tuple[str, rx.Component]]:
    """Provide the portfolio page components for testing."""
    return [
        ("index", index()),
        ("navbar", navbar()),
        ("footer", footer())
    ]


@given("I have the footer component", target_fixture="footer_component")
def footer_component() -> rx.Component:
    """Provide the footer component for testing."""
    return footer()


@when("I check each component type")
def check_component_types(portfolio_components: List[Tuple[str, rx.Component]]) -> None:
    """This step is implemented in the 'then' step for simplicity."""
    pass


@when("I render the footer")
def render_footer(footer_component: rx.Component) -> None:
    """This step is implemented in the 'then' step for simplicity."""
    pass


@then("all components should be valid Reflex components")
def verify_components_are_reflex(portfolio_components: List[Tuple[str, rx.Component]]) -> None:
    """Test that index, navbar, and footer components are Reflex components."""
    for name, comp in portfolio_components:
        assert isinstance(comp, rx.Component), f"{name} is not a Reflex Component"


@then('it should contain the copyright text "© 2025 Matias Falconaro."')
def verify_footer_copyright_text(footer_component: rx.Component) -> None:
    """Test that the footer component contains the expected copyright text."""
    text: str = str(footer_component).encode().decode("unicode_escape")
    assert "© 2025 Matias Falconaro." in text, \
        f"Copyright text not found in footer. Content: {text}"