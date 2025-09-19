import reflex as rx
import pytest
from typing import Callable

from portfolio.components import (navbar,
                                 contact_modal,
                                 code_info_modal,
                                 header_section,
                                 work_section,
                                 education_section,
                                 project_section,
                                 footer)
from portfolio.states import States


def test_navbar_returns_component() -> None:
    """
    Test that the navbar function returns a Reflex Component.
    """
    comp: rx.Component = navbar()
    assert isinstance(comp, rx.Component)


def test_sections_components() -> None:
    """
    Test that all main section functions return Reflex Components.
    """
    for comp_fn in [header_section,
                    work_section,
                    education_section,
                    project_section,
                    footer]:
        comp: rx.Component = comp_fn()
        assert isinstance(comp, rx.Component)


def test_modals_component(mock_state: States) -> None:
    """
    Test that contact_modal and code_info_modal return Reflex Components
    when the corresponding state flags are set.
    """
    mock_state.show_modal = True
    assert isinstance(contact_modal(), rx.Component)

    mock_state.show_code_modal = True
    assert isinstance(code_info_modal(), rx.Component)


def test_contact_modal_returns_component() -> None:
    """
    Test that contact_modal returns a Reflex Component when show_modal is True.
    """
    state: States = States()
    state.show_modal = True
    comp: rx.Component = contact_modal()
    assert isinstance(comp, rx.Component)


def test_code_info_modal_returns_component() -> None:
    """
    Test that code_info_modal returns a Reflex Component when show_code_modal is True.
    """
    state: States = States()
    state.show_code_modal = True
    comp: rx.Component = code_info_modal()
    assert isinstance(comp, rx.Component)


def test_header_section_component() -> None:
    """
    Test that header_section returns a Reflex Component.
    """
    comp: rx.Component = header_section()
    assert isinstance(comp, rx.Component)


def test_work_section_component() -> None:
    """
    Test that work_section returns a Reflex Component.
    """
    comp: rx.Component = work_section()
    assert isinstance(comp, rx.Component)


def test_education_section_component() -> None:
    """
    Test that education_section returns a Reflex Component.
    """
    comp: rx.Component = education_section()
    assert isinstance(comp, rx.Component)


def test_project_section_component() -> None:
    """
    Test that project_section returns a Reflex Component.
    """
    comp: rx.Component = project_section()
    assert isinstance(comp, rx.Component)


def test_footer_component() -> None:
    """
    Test that footer returns a Reflex Component.
    """
    comp: rx.Component = footer()
    assert isinstance(comp, rx.Component)
