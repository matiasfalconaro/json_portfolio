import os

from portfolio.components import get_version


def test_get_version_file(tmp_version_file):
    assert get_version() == "1.4.0"


def test_get_version_missing(monkeypatch, tmp_path):
    monkeypatch.chdir(tmp_path)
    assert get_version() == "dev"
