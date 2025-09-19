import pytest

from portfolio.states import States
from pathlib import Path
from typing import Generator

@pytest.fixture
def mock_state() -> States:
    """Fixture that provides a fresh instance of the States class for testing."""
    return States()


@pytest.fixture
def tmp_version_file(tmp_path: Path, monkeypatch) -> Generator[Path, None, None]:
    """
    Fixture that creates a temporary 'version.txt' file with a preset version,
    and changes the current working directory to the temporary path.    
    """
    file = tmp_path / "version.txt"
    file.write_text("1.4.0")
    monkeypatch.chdir(tmp_path)
    yield file
