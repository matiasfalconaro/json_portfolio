from typing import (List,
                    Optional)
from datetime import datetime
from .db import db
from portfolio.config import get_logger
from .models import (Basics,
                     Work,
                     Education,
                     Certificate,
                     Skill,
                     Language,
                     Interest,
                     Reference,
                     Project,
                     User)
from .auth import (hash_password,
                   verify_password)


logger = get_logger(__name__)


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


def create_user(username: str, password: str) -> Optional[User]:
    """Create a new user with hashed password."""
    try:
        existing_user = db.users.find_one({"username": username})
        if existing_user:
            logger.warning(f"User {username} already exists")
            return None

        password_hash = hash_password(password)
        user_doc = {
            "username": username,
            "password_hash": password_hash,
            "created_at": datetime.utcnow().isoformat()
        }

        db.users.insert_one(user_doc)
        logger.info(f"User {username} created successfully")
        return User(**user_doc)
    except Exception as e:
        logger.error(f"Error creating user: {e}")
        return None


def authenticate_user(username: str, password: str) -> Optional[User]:
    """Authenticate a user with username and password."""
    try:
        user_data = db.users.find_one({"username": username}, {"_id": 0})
        if not user_data:
            logger.warning(f"User {username} not found")
            return None

        if verify_password(password, user_data["password_hash"]):
            logger.info(f"User {username} authenticated successfully")
            return User(**user_data)
        else:
            logger.warning(f"Invalid password for user {username}")
            return None
    except Exception as e:
        logger.error(f"Error authenticating user: {e}")
        return None


def get_user(username: str) -> Optional[User]:
    """Get user by username."""
    try:
        user_data = db.users.find_one({"username": username}, {"_id": 0})
        if user_data:
            return User(**user_data)
        return None
    except Exception as e:
        logger.error(f"Error getting user: {e}")
        return None
