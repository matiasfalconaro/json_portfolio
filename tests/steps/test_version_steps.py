import os
import pytest

from pathlib import Path
from pytest_bdd import scenarios, given, when, then
from portfolio.components import get_version


FEATURE_FILE = Path(__file__).parent.parent / "features" / "version.feature"
scenarios(str(FEATURE_FILE))


@given("I have a version file with content \"2.0.0\"")
def use_version_file(monkeypatch, tmp_version_file: Path) -> None:
    """Use the existing version file fixture."""
    monkeypatch.chdir(tmp_version_file.parent)


@given("I am in a directory without version file")
def setup_no_version_file(monkeypatch, tmp_path: Path) -> None:
    """Setup directory without version file."""
    version_file = tmp_path / "version.txt"
    if version_file.exists():
        version_file.unlink()
    
    monkeypatch.chdir(tmp_path)


@when("I call get_version", target_fixture="version_result")
def call_get_version() -> str:
    """Call the get_version function."""
    return get_version()


@then("it should return \"2.0.0\"")
def verify_version(version_result: str) -> None:
    """Verify that get_version returns the expected version."""
    assert version_result == "2.0.0"


@then("it should return \"dev\"")
def verify_dev_version(version_result: str) -> None:
    """Verify that get_version returns 'dev' when no version file exists."""
    assert version_result == "dev"