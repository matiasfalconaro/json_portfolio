import os

from pathlib import Path
from typing import (Dict,
                    Any,
                    List)
from pytest_bdd import (scenarios,
                        given,
                        then)
from portfolio.data import (load_portfolio,
                            data)


FEATURE_FILE = Path(__file__).parent.parent / "features" / "data.feature"
print(f"Looking for feature file at: {FEATURE_FILE}")
print(f"File exists: {FEATURE_FILE.exists()}")
scenarios(str(FEATURE_FILE))

@given("the portfolio data is loaded", target_fixture="portfolio_data")
def portfolio_data() -> Dict[str, Any]:
    """Load portfolio data for tests."""
    return load_portfolio()


@then("it should be a dictionary")
def check_is_dict(portfolio_data: Dict[str, Any]) -> None:
    """Verify that the loaded portfolio is a dictionary."""
    assert isinstance(portfolio_data, dict)


@then('the data should contain the keys "basics", "work", "education", "projects", "certificates"')
def check_keys_exist(portfolio_data: Dict[str, Any]) -> None:
    """Verify expected top-level keys exist in the data."""
    expected_keys: List[str] = ["basics", "work", "education", "projects", "certificates"]
    for key in expected_keys:
        assert key in portfolio_data, f"Key '{key}' is missing in portfolio data"


@then('each project should have "name", "description" and "highlights" as a list')
def check_project_fields(portfolio_data: Dict[str, Any]) -> None:
    """Check that all projects have required fields with correct types."""
    projects = portfolio_data.get("projects", [])
    for project in projects:
        assert "name" in project and project["name"], "Project missing 'name'"
        assert "description" in project and project["description"], "Project missing 'description'"
        assert "highlights" in project and isinstance(project["highlights"], list), \
            "'highlights' must be a list"


@then("the main image and logos should exist in the assets folder")
def check_assets_exist() -> None:
    """Check that main image and logo assets exist."""
    assets_dir = Path("assets")
    
    # Check main image
    main_image_path = assets_dir / data["basics"]["image"]
    assert main_image_path.exists(), f"{main_image_path} no existe"
    
    # Check logos
    for logo_name in ["code.svg", "github.svg", "linkedin.svg", "python.svg"]:
        logo_path = assets_dir / logo_name
        assert logo_path.exists(), f"{logo_path} no existe"
