import os
import pytest
import requests

from typing import (Optional,
                    Dict,
                    Any)
from portfolio.data import data


@pytest.mark.parametrize("file_path", [
                        "assets/code.svg",
                        "assets/github.svg",
                        "assets/linkedin.svg",
                        "assets/python.svg",
                        "assets/1736345293938.jfif",
                        "assets/resume_v1.3.0.pdf"
                        ])
def test_local_files_exist(file_path: str) -> None:
    """
    Test that required local files exist in the assets directory.
    """
    normalized_path: str = file_path.lstrip("/\\")
    full_path: str = os.path.join(os.getcwd(), normalized_path)
    assert os.path.exists(full_path), f"El archivo {file_path} no existe"


@pytest.mark.parametrize("url", [
    "https://github.com/matiasfalconaro",
    # LinkedIn often blocks bots, so disabled for now
    # "https://www.linkedin.com/in/matiasfalconaro/"
])
def test_external_urls_reachable(url: str) -> None:
    """
    Test that external URLs are reachable.
    """
    try:
        response = requests.head(url, allow_redirects=True, timeout=5)
        assert response.status_code < 400, f"URL inaccesible: {url}"
    except requests.RequestException:
        pytest.fail(f"No se pudo acceder a la URL: {url}")


@pytest.mark.parametrize("cert", data.get("certificates", []))
def test_certificate_urls(cert: Dict[str, Any]) -> None:
    """
    Test that certificate URLs in the portfolio are accessible.
    """
    url: Optional[str] = cert.get("url")
    if url:
        try:
            response = requests.head(url, allow_redirects=True, timeout=5)
            assert response.status_code < 400, f"Certificado inaccesible: {url}"
        except requests.RequestException:
            pytest.fail(f"No se pudo acceder al certificado: {url}")
