import pytest

from pydantic import ValidationError
from database.models import (Basics,
                              Work,
                              Education,
                              Certificate,
                              Skill,
                              Language,
                              Interest,
                              Reference,
                              Project,
                              Profile,
                              Location)


class TestBasicsModel:
    """Test Basics model validation."""

    def test_basics_valid_data(self):
        """Test Basics model with valid data."""
        data = {
            "name": "John Doe",
            "label": "Software Developer",
            "email": "john@example.com",
            "summary": "Experienced developer",
            "image": None,
            "phone": None,
            "url": None,
            "location": {
                "city": "New York",
                "countryCode": "US",
                "postalCode": "10001",
                "region": "NY"
            },
            "profiles": []
        }

        basics = Basics(**data)

        assert basics.name == "John Doe"
        assert basics.email == "john@example.com"

    def test_basics_invalid_email(self):
        """Test Basics model with invalid email."""
        data = {
            "name": "John Doe",
            "label": "Developer",
            "email": "not-an-email",
            "summary": "Test",
            "location": {"city": "NY", "countryCode": "US"},
            "profiles": []
        }

        with pytest.raises(ValidationError) as exc_info:
            Basics(**data)

        assert "email" in str(exc_info.value)

    def test_basics_optional_fields(self):
        """Test Basics model with optional fields as None."""
        data = {
            "name": "John Doe",
            "label": "Developer",
            "email": "john@example.com",
            "summary": "Test",
            "location": {},
            "profiles": [],
            "phone": None,
            "url": None,
            "image": None
        }

        basics = Basics(**data)

        assert basics.phone is None
        assert basics.url is None

    def test_basics_with_profiles(self):
        """Test Basics model with profiles."""
        data = {
            "name": "John Doe",
            "label": "Developer",
            "email": "john@example.com",
            "summary": "Test",
            "image": None,
            "phone": None,
            "url": None,
            "location": {},
            "profiles": [
                {
                    "network": "GitHub",
                    "username": "johndoe",
                    "url": "https://github.com/johndoe"
                }
            ]
        }

        basics = Basics(**data)

        assert len(basics.profiles) == 1
        assert basics.profiles[0].network == "GitHub"


class TestWorkModel:
    """Test Work model validation."""

    def test_work_valid_data(self):
        """Test Work model with valid data."""
        data = {
            "name": "Tech Corp",
            "position": "Senior Developer",
            "startDate": "2020-01",
            "endDate": "2022-01",
            "summary": "Developed applications",
            "highlights": ["Python", "Django"]
        }

        work = Work(**data)

        assert work.name == "Tech Corp"
        assert work.position == "Senior Developer"
        assert len(work.highlights) == 2

    def test_work_optional_url(self):
        """Test Work model with optional URL."""
        data = {
            "name": "Tech Corp",
            "position": "Developer",
            "startDate": "2020-01",
            "endDate": "2022-01",
            "summary": "Test",
            "highlights": [],
            "url": None
        }

        work = Work(**data)

        assert work.url is None

    def test_work_invalid_url(self):
        """Test Work model with invalid URL."""
        data = {
            "name": "Tech Corp",
            "position": "Developer",
            "startDate": "2020-01",
            "endDate": "2022-01",
            "summary": "Test",
            "highlights": [],
            "url": "not-a-valid-url"
        }

        with pytest.raises(ValidationError):
            Work(**data)

    def test_work_missing_required_fields(self):
        """Test Work model with missing required fields."""
        data = {
            "name": "Tech Corp"
            # Other fields
        }

        with pytest.raises(ValidationError):
            Work(**data)


class TestEducationModel:
    """Test Education model validation."""

    def test_education_valid_data(self):
        """Test Education model with valid data."""
        data = {
            "institution": "MIT",
            "area": "Computer Science",
            "studyType": "Bachelor",
            "startDate": "2015-09",
            "endDate": "2019-06",
            "score": "3.8"
        }

        education = Education(**data)

        assert education.institution == "MIT"
        assert education.area == "Computer Science"

    def test_education_optional_fields(self):
        """Test Education model with optional fields."""
        data = {
            "institution": "MIT",
            "area": "CS",
            "studyType": "Bachelor",
            "startDate": "2015",
            "endDate": "2019",
            "url": None,
            "score": None
        }

        education = Education(**data)

        assert education.url is None
        assert education.score is None

    def test_education_with_valid_url(self):
        """Test Education model with valid URL."""
        data = {
            "institution": "MIT",
            "area": "CS",
            "studyType": "Bachelor",
            "startDate": "2015",
            "endDate": "2019",
            "url": "https://www.mit.edu"
        }

        education = Education(**data)

        assert str(education.url) == "https://www.mit.edu/"


class TestProjectModel:
    """Test Project model validation."""

    def test_project_valid_data(self):
        """Test Project model with valid data."""
        data = {
            "name": "Awesome Project",
            "role": "Lead Developer",
            "description": "A great project",
            "highlights": ["Python", "FastAPI"],
            "github": "https://github.com/user/project",
            "isActive": True
        }

        project = Project(**data)

        assert project.name == "Awesome Project"
        assert project.isActive is True
        assert len(project.highlights) == 2

    def test_project_empty_highlights(self):
        """Test Project model with empty highlights."""
        data = {
            "name": "Project",
            "role": "Developer",
            "description": "Test",
            "highlights": [],
            "github": "https://github.com/test",
            "isActive": False
        }

        project = Project(**data)

        assert project.highlights == []

    def test_project_default_is_active(self):
        """Test Project model default isActive value."""
        data = {
            "name": "Project",
            "role": "Developer",
            "description": "Test",
            "github": "https://github.com/test"
        }

        project = Project(**data)

        assert project.isActive is False

    def test_project_optional_url(self):
        """Test Project model with optional URL."""
        data = {
            "name": "Project",
            "role": "Developer",
            "description": "Test",
            "github": "https://github.com/test",
            "url": None
        }

        project = Project(**data)

        assert project.url is None


class TestCertificateModel:
    """Test Certificate model validation."""

    def test_certificate_valid_data(self):
        """Test Certificate model with valid data."""
        data = {
            "name": "AWS Certified Solutions Architect",
            "date": "2023-01-15",
            "issuer": "Amazon Web Services",
            "url": "https://aws.amazon.com/certification/"
        }

        cert = Certificate(**data)

        assert cert.name == "AWS Certified Solutions Architect"
        assert cert.issuer == "Amazon Web Services"

    def test_certificate_optional_url(self):
        """Test Certificate model with optional URL."""
        data = {
            "name": "Certificate",
            "date": "2023-01",
            "issuer": "Test Org",
            "url": None
        }

        cert = Certificate(**data)

        assert cert.url is None

    def test_certificate_invalid_url(self):
        """Test Certificate model with invalid URL."""
        data = {
            "name": "Certificate",
            "date": "2023-01",
            "issuer": "Test",
            "url": "invalid-url"
        }

        with pytest.raises(ValidationError):
            Certificate(**data)


class TestSkillModel:
    """Test Skill model validation."""

    def test_skill_valid_data(self):
        """Test Skill model with valid data."""
        data = {
            "name": "Python",
            "level": "Advanced",
            "keywords": ["Django", "Flask", "FastAPI"]
        }

        skill = Skill(**data)

        assert skill.name == "Python"
        assert skill.level == "Advanced"
        assert len(skill.keywords) == 3

    def test_skill_empty_keywords(self):
        """Test Skill model with empty keywords."""
        data = {
            "name": "JavaScript",
            "level": "Intermediate",
            "keywords": []
        }

        skill = Skill(**data)

        assert skill.keywords == []


class TestLanguageModel:
    """Test Language model validation."""

    def test_language_valid_data(self):
        """Test Language model with valid data."""
        data = {
            "language": "English",
            "fluency": "Native"
        }

        lang = Language(**data)

        assert lang.language == "English"
        assert lang.fluency == "Native"


class TestInterestModel:
    """Test Interest model validation."""

    def test_interest_valid_data(self):
        """Test Interest model with valid data."""
        data = {
            "name": "Open Source",
            "keywords": ["Python", "GitHub"]
        }

        interest = Interest(**data)

        assert interest.name == "Open Source"
        assert len(interest.keywords) == 2

    def test_interest_optional_name(self):
        """Test Interest model with optional name."""
        data = {
            "name": None,
            "keywords": ["Test"]
        }

        interest = Interest(**data)

        assert interest.name is None


class TestReferenceModel:
    """Test Reference model validation."""

    def test_reference_valid_data(self):
        """Test Reference model with valid data."""
        data = {
            "name": "Jane Smith",
            "reference": "Excellent team player"
        }

        ref = Reference(**data)

        assert ref.name == "Jane Smith"
        assert ref.reference == "Excellent team player"

    def test_reference_optional_fields(self):
        """Test Reference model with optional fields."""
        data = {
            "name": None,
            "reference": None
        }

        ref = Reference(**data)

        assert ref.name is None
        assert ref.reference is None


class TestProfileModel:
    """Test Profile model validation."""

    def test_profile_valid_data(self):
        """Test Profile model with valid data."""
        data = {
            "network": "LinkedIn",
            "username": "johndoe",
            "url": "https://linkedin.com/in/johndoe"
        }

        profile = Profile(**data)

        assert profile.network == "LinkedIn"
        assert profile.username == "johndoe"


class TestLocationModel:
    """Test Location model validation."""

    def test_location_all_fields(self):
        """Test Location model with all fields."""
        data = {
            "postalCode": "10001",
            "city": "New York",
            "countryCode": "US",
            "region": "NY"
        }

        location = Location(**data)

        assert location.city == "New York"
        assert location.countryCode == "US"

    def test_location_optional_fields(self):
        """Test Location model with optional fields."""
        data = {}

        location = Location(**data)

        assert location.city is None
        assert location.postalCode is None
