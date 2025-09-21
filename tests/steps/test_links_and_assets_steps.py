import os
import requests
import pytest

from pathlib import Path
from pytest_bdd import (scenarios,
                        given,
                        when,
                        then,
                        parsers)
from typing import (List,
                    Dict,
                    Any,
                    Optional)
from portfolio.data import data


FEATURE_FILE = Path(__file__).parent.parent / "features" / "links_and_assets.feature"
scenarios(str(FEATURE_FILE))


@given("I have a list of required asset files", target_fixture="asset_files")
def asset_files() -> List[str]:
    """Provide the list of required asset files."""
    return [
        "assets/code.svg",
        "assets/github.svg",
        "assets/linkedin.svg",
        "assets/python.svg",
        "assets/1736345293938.jfif",
        "assets/resume_v1.3.0.pdf"
    ]


@given("I have a list of external URLs to test", target_fixture="external_urls")
def external_urls() -> List[str]:
    """Provide the list of external URLs to test."""
    return [
        "https://github.com/matiasfalconaro",
        # LinkedIn often blocks bots, so disabled for now
        # "https://www.linkedin.com/in/matiasfalconaro/"
    ]


@given("I have certificate data from portfolio", target_fixture="certificates")
def certificates() -> List[Dict[str, Any]]:
    """Provide certificate data from portfolio."""
    return data.get("certificates", [])


@when("I check each file path")
def check_file_paths(asset_files: List[str]) -> None:
    """This step is implemented in the 'then' step for simplicity."""
    pass


@when("I check each URL")
def check_urls(external_urls: List[str]) -> None:
    """This step is implemented in the 'then' step for simplicity."""
    pass


@when("I check each certificate URL")
def check_certificate_urls(certificates: List[Dict[str, Any]]) -> None:
    """This step is implemented in the 'then' step for simplicity."""
    pass


@then("all local asset files should exist")
def verify_asset_files_exist(asset_files: List[str]) -> None:
    """Test that required local files exist in the assets directory."""
    for file_path in asset_files:
        normalized_path: str = file_path.lstrip("/\\")
        full_path: str = os.path.join(os.getcwd(), normalized_path)
        assert os.path.exists(full_path), f"El archivo {file_path} no existe"


@then("all external URLs should be accessible")
def verify_external_urls_accessible(external_urls: List[str]) -> None:
    """Test that external URLs are reachable."""
    for url in external_urls:
        try:
            response = requests.head(url, allow_redirects=True, timeout=5)
            assert response.status_code < 400, f"URL inaccesible: {url}"
        except requests.RequestException:
            pytest.fail(f"No se pudo acceder a la URL: {url}")


@then("all certificate URLs should be accessible")
def verify_certificate_urls_accessible(certificates: List[Dict[str, Any]]) -> None:
    """Test that certificate URLs in the portfolio are accessible."""
    for cert in certificates:
        url: Optional[str] = cert.get("url")
        if url:
            try:
                response = requests.head(url, allow_redirects=True, timeout=5)
                assert response.status_code < 400, f"Certificado inaccesible: {url}"
            except requests.RequestException:
                pytest.fail(f"No se pudo acceder al certificado: {url}")
