from typing import (List,
                    Optional)
from .db import db
from .models import (Basics,
                     Work,
                     Education,
                     Certificate, 
                     Skill,
                     Language,
                     Interest,
                     Reference,
                     Project)


def get_basics() -> Optional[Basics]:
    """Returns 'basics' data as Basics model."""
    basics_data = db.basics.find_one({}, {"_id": 0})
    return Basics(**basics_data) if basics_data else None


def get_work() -> List[Work]:
    """Returns the list of work experiences."""
    work_data = db.work.find({}, {"_id": 0})
    return [Work(**item) for item in work_data]


def get_education() -> List[Education]:
    """Returns the list of education records."""
    education_data = db.education.find({}, {"_id": 0})
    return [Education(**item) for item in education_data]


def get_certificates() -> List[Certificate]:
    """Returns the list of certificates."""
    certificates_data = db.certificates.find({}, {"_id": 0})
    return [Certificate(**item) for item in certificates_data]


def get_skills() -> List[Skill]:
    """Returns the list of skills."""
    skills_data = db.skills.find({}, {"_id": 0})
    return [Skill(**item) for item in skills_data]


def get_languages() -> List[Language]:
    """Returns the list of languages."""
    languages_data = db.languages.find({}, {"_id": 0})
    return [Language(**item) for item in languages_data]


def get_interests() -> List[Interest]:
    """Returns the list of interests."""
    interests_data = db.interests.find({}, {"_id": 0})
    return [Interest(**item) for item in interests_data]


def get_references() -> List[Reference]:
    """Returns the list of references."""
    references_data = db.references.find({}, {"_id": 0})
    return [Reference(**item) for item in references_data]


def get_projects() -> List[Project]:
    """Returns the list of projects."""
    projects_data = db.projects.find({}, {"_id": 0})
    return [Project(**item) for item in projects_data]
