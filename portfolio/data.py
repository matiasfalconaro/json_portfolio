import json

from pathlib import Path
from typing import Any


def load_portfolio() -> dict[str, Any]:
    """Load portfolio data from the resume.json file."""
    with open(Path(__file__).parent / "resume.json", "r", encoding="utf-8") as f:
        return json.load(f)

data = load_portfolio()