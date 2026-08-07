import reflex as rx

from pathlib import Path
from pytest_bdd import (scenarios,
                        given,
                        when,
                        then)
from portfolio.components import (navbar, contact_modal, code_info_modal,
                                 header_section, work_section,
                                 education_section, project_section,
                                 footer)
from portfolio.states import States
from typing import List


FEATURE_FILE = Path(__file__).parent.parent / "features" / "components.feature"
scenarios(str(FEATURE_FILE))


@given("a fresh state", target_fixture="state")
def state() -> States:
    """Provide a fresh Reflex state for each scenario."""
    return States()


@when("I render the navbar")
def render_navbar() -> rx.Component:
    """Render the navbar. No caching of Reflex component."""
    return navbar()


@then("it should be a Reflex Component")
def check_component() -> None:
    comp = navbar()
    assert isinstance(comp, rx.Component)


@when("I render all main sections")
def render_sections() -> List[rx.Component]:
    """Render main sections. No caching of Reflex components."""
    return [
        header_section(),
        work_section(),
        education_section(),
        project_section(),
        footer(),
    ]


@then("each should be a Reflex Component")
def check_sections() -> None:
    """Verify that all main portfolio sections are valid Reflex components."""
    sections = [
        header_section(),
        work_section(),
        education_section(),
        project_section(),
        footer(),
    ]
    for comp in sections:
        assert isinstance(comp, rx.Component)


@when("I enable show_modal and show_code_modal")
def enable_modals(state) -> States:
    """Set flags in the Reflex state."""
    state.show_modal = True
    state.show_code_modal = True
    return state


@then("contact_modal and code_info_modal should be Reflex Components")
def check_modals() -> None:
    """Verify that both modal components are valid Reflex components."""
    assert isinstance(contact_modal(), rx.Component)
    assert isinstance(code_info_modal(), rx.Component)
