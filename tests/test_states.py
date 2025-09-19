from portfolio.states import States


def test_toggle_modal(mock_state):
    assert not mock_state.show_modal
    mock_state.toggle_modal()
    assert mock_state.show_modal
    mock_state.toggle_modal()
    assert not mock_state.show_modal

def test_toggle_code_modal(mock_state):
    assert not mock_state.show_code_modal
    mock_state.toggle_code_modal()
    assert mock_state.show_code_modal
    mock_state.toggle_code_modal()
    assert not mock_state.show_code_modal
