import os

from pathlib import Path
from portfolio.components import get_version


def test_get_version_file(tmp_version_file: Path) -> None:
    """
    Test that `get_version` returns the correct version from the version file.
    """
    assert get_version() == "2.0.0"


def test_get_version_missing(monkeypatch, tmp_path: Path) -> None:
    """
    Test that `get_version` returns 'dev' when no version file exists.
    """
    monkeypatch.chdir(tmp_path)
    assert get_version() == "dev"
