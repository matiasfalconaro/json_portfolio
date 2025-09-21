import pytest

from pathlib import Path
from pytest_bdd import scenarios, given, when, then
from portfolio.states import States


FEATURE_FILE = Path(__file__).parent.parent / "features" / "states.feature"
scenarios(str(FEATURE_FILE))


@pytest.fixture
def mock_state() -> States:
    """Provide a fresh state for each scenario."""
    return States()


@given("I have a fresh state", target_fixture="state")
def fresh_state() -> States:
    """Provide a fresh state for testing."""
    return States()


@when("I toggle the general modal")
def toggle_general_modal(state: States) -> None:
    """Toggle the general modal."""
    state.toggle_modal()


@when("I toggle the general modal again")
def toggle_general_modal_again(state: States) -> None:
    """Toggle the general modal again."""
    state.toggle_modal()


@when("I toggle the code modal")
def toggle_code_modal(state: States) -> None:
    """Toggle the code modal."""
    state.toggle_code_modal()


@when("I toggle the code modal again")
def toggle_code_modal_again(state: States) -> None:
    """Toggle the code modal again."""
    state.toggle_code_modal()


@then("the modal should be shown")
def verify_modal_shown(state: States) -> None:
    """Verify that the modal is shown."""
    assert state.show_modal, "Modal should be shown"


@then("the modal should be hidden")
def verify_modal_hidden(state: States) -> None:
    """Verify that the modal is hidden."""
    assert not state.show_modal, "Modal should be hidden"


@then("the code modal should be shown")
def verify_code_modal_shown(state: States) -> None:
    """Verify that the code modal is shown."""
    assert state.show_code_modal, "Code modal should be shown"


@then("the code modal should be hidden")
def verify_code_modal_hidden(state: States) -> None:
    """Verify that the code modal is hidden."""
    assert not state.show_code_modal, "Code modal should be hidden"