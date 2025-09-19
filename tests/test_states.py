from portfolio.states import States


def test_toggle_modal(mock_state: States) -> None:
    """
    Test that the general modal toggles correctly.
    """
    assert not mock_state.show_modal
    mock_state.toggle_modal()
    assert mock_state.show_modal
    mock_state.toggle_modal()
    assert not mock_state.show_modal


def test_toggle_code_modal(mock_state: States) -> None:
    """
    Test that the code modal toggles correctly.
    """
    assert not mock_state.show_code_modal
    mock_state.toggle_code_modal()
    assert mock_state.show_code_modal
    mock_state.toggle_code_modal()
    assert not mock_state.show_code_modal