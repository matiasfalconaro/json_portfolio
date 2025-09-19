import pytest

import os
from portfolio.data import (load_portfolio,
                            data)


def test_load_portfolio_returns_dict():
    result = load_portfolio()
    assert isinstance(result, dict)


def test_data_keys_exist():
    keys = ["basics",
            "work",
            "education",
            "projects",
            "certificates"]
    for key in keys:
        assert key in data


def test_project_fields():
    for project in data["projects"]:
        assert "name" in project and project["name"]
        assert "description" in project and project["description"]
        assert "highlights" in project and isinstance(project["highlights"], list)


def test_assets_exist():
    basics_image = data["basics"]["image"]
    assert os.path.exists(os.path.join("assets", basics_image)), f"{basics_image} no existe"

    for logo in ["code.svg", "github.svg", "linkedin.svg", "python.svg"]:
        assert os.path.exists(os.path.join("assets", logo)), f"{logo} no existe"