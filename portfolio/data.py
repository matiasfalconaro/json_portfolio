import json

from pathlib import Path
from database.db import db
from database.models import (Basics,
                             Work,
                             Education,
                             Certificate,
                             Skill,
                             Language,
                             Interest,
                             Reference,
                             Project)
from typing import (Any,
                    Union,
                    List,
                    Dict)
from pydantic import HttpUrl


with open(Path(__file__).parent / "resume.json", encoding="utf-8") as f:
    data = json.load(f)


def load_portfolio() -> dict:
    """Return the raw portfolio data from resume.json"""
    return data


def serialize(obj: Any) -> Union[str, List[Any], Dict[str, Any], int, float, bool, None]:
    """
    - Makes complex objects (HttpUrl, etc.) type compatible with MongoDB.
    - Recursively processes data structures to convert Pydantic types like HttpUrl
    to MongoDB-compatible primitive types.
    
    Args:
        obj: Any Python object to serialize, can be list, dict, HttpUrl, or primitive
        
    Returns:
        Union[str, List[Any], Dict[str, Any], Any]: MongoDB-compatible data structure
        with complex types converted to primitives
    """
    if isinstance(obj, list):
        return [serialize(i) for i in obj]
    elif isinstance(obj, dict):
        return {k: serialize(v) for k, v in obj.items()}
    #elif hasattr(obj, "__str__") and type(obj).__name__ == "HttpUrl":
    elif isinstance(obj, HttpUrl):
        return str(obj)
    else:
        return obj


def main() -> None:
    """ Main entry point for loading and validating portfolio data into MongoDB."""
    basics = Basics(**data["basics"])
    work = [Work(**w) for w in data["work"]]
    education = [Education(**e) for e in data["education"]]
    certificates = [Certificate(**c) for c in data["certificates"]]
    skills = [Skill(**s) for s in data["skills"]]
    languages = [Language(**l) for l in data["languages"]]
    interests = [Interest(**i) for i in data["interests"]]
    references = [Reference(**r) for r in data["references"]]
    projects = [Project(**p) for p in data["projects"]]

    collections = {
        "basics": basics,
        "work": work,
        "education": education,
        "certificates": certificates,
        "skills": skills,
        "languages": languages,
        "interests": interests,
        "references": references,
        "projects": projects,
    }

    for name, items in collections.items():
        if name == "basics":
            db.basics.replace_one({}, serialize(items.model_dump()), upsert=True)
        else:
            db[name].insert_many([serialize(i.model_dump()) for i in items])

    print("✅ Resume validated and inserted into MongoDB!")


if __name__ == "__main__":
    main()
