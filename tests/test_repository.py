import pytest

from unittest.mock import (patch,
                           MagicMock)
from pydantic import ValidationError
from database.repository import (get_basics,
                                  get_work,
                                  get_education,
                                  get_certificates,
                                  get_skills,
                                  get_languages,
                                  get_interests,
                                  get_references,
                                  get_projects)
from database.models import (Basics,
                              Work,
                              Education,
                              Certificate,
                              Skill,
                              Language,
                              Interest,
                              Reference,
                              Project)


class TestGetBasics:
    """Test get_basics repository function."""

    @patch('database.repository.db')
    def test_get_basics_returns_basics_model(self, mock_db):
        """Test that get_basics returns a Basics model instance."""
        mock_db.basics.find_one.return_value = {
            "name": "Test User",
            "label": "Developer",
            "email": "test@example.com",
            "summary": "Test summary",
            "image": None,
            "phone": None,
            "url": None,
            "location": {},
            "profiles": []
        }

        result = get_basics()

        assert isinstance(result, Basics)
        assert result.name == "Test User"
        assert result.email == "test@example.com"

    @patch('database.repository.db')
    def test_get_basics_returns_none_when_empty(self, mock_db):
        """Test that get_basics returns None when no data exists."""
        mock_db.basics.find_one.return_value = None

        result = get_basics()

        assert result is None

    @patch('database.repository.db')
    def test_get_basics_handles_validation_error(self, mock_db):
        """Test that get_basics raises error with invalid data."""
        mock_db.basics.find_one.return_value = {
            "name": "Test",
            "email": "invalid-email"
        }

        with pytest.raises(ValidationError):
            get_basics()

    @patch('database.repository.db')
    def test_get_basics_database_unavailable(self, mock_db):
        """Test get_basics when database is unavailable."""
        mock_db.basics.find_one.side_effect = Exception("Database connection failed")

        with pytest.raises(Exception):
            get_basics()


class TestGetWork:
    """Test get_work repository function."""

    @patch('database.repository.db')
    def test_get_work_returns_list_of_work_models(self, mock_db):
        """Test that get_work returns a list of Work models."""
        mock_db.work.find.return_value = [
            {
                "name": "Company A",
                "position": "Developer",
                "startDate": "2020-01",
                "endDate": "2021-01",
                "summary": "Worked on projects",
                "highlights": ["Python", "Django"]
            }
        ]

        result = get_work()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], Work)
        assert result[0].name == "Company A"

    @patch('database.repository.db')
    def test_get_work_returns_empty_list_when_no_data(self, mock_db):
        """Test that get_work returns empty list when no data exists."""
        mock_db.work.find.return_value = []

        result = get_work()

        assert result == []

    @patch('database.repository.db')
    def test_get_work_with_malformed_data(self, mock_db):
        """Test get_work with malformed data raises ValidationError."""
        mock_db.work.find.return_value = [
            {
                "name": "Company",
            }
        ]

        with pytest.raises(ValidationError):
            get_work()


class TestGetEducation:
    """Test get_education repository function."""

    @patch('database.repository.db')
    def test_get_education_returns_list_of_education_models(self, mock_db):
        """Test that get_education returns a list of Education models."""
        mock_db.education.find.return_value = [
            {
                "institution": "University A",
                "area": "Computer Science",
                "studyType": "Bachelor",
                "startDate": "2015-09",
                "endDate": "2019-06",
                "score": "3.8"
            }
        ]

        result = get_education()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], Education)
        assert result[0].institution == "University A"

    @patch('database.repository.db')
    def test_get_education_empty_collection(self, mock_db):
        """Test get_education with empty collection."""
        mock_db.education.find.return_value = []

        result = get_education()

        assert result == []


class TestGetProjects:
    """Test get_projects repository function."""

    @patch('database.repository.db')
    def test_get_projects_returns_list_of_project_models(self, mock_db):
        """Test that get_projects returns a list of Project models."""
        mock_db.projects.find.return_value = [
            {
                "name": "Project A",
                "role": "Lead Developer",
                "description": "A test project",
                "highlights": ["Python", "Flask"],
                "github": "https://github.com/test/project",
                "isActive": True
            }
        ]

        result = get_projects()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], Project)
        assert result[0].name == "Project A"
        assert result[0].isActive is True

    @patch('database.repository.db')
    def test_get_projects_validation_error(self, mock_db):
        """Test get_projects with validation error."""
        mock_db.projects.find.return_value = [
            {
                "name": "Project",
                # Missing required fields like 'role', 'description', 'github'
            }
        ]

        with pytest.raises(ValidationError):
            get_projects()


class TestGetCertificates:
    """Test get_certificates repository function."""

    @patch('database.repository.db')
    def test_get_certificates_returns_list(self, mock_db):
        """Test that get_certificates returns a list of Certificate models."""
        mock_db.certificates.find.return_value = [
            {
                "name": "AWS Certified",
                "date": "2023-01-15",
                "issuer": "Amazon",
                "url": "https://aws.amazon.com/cert"
            }
        ]

        result = get_certificates()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], Certificate)
        assert result[0].name == "AWS Certified"

    @patch('database.repository.db')
    def test_get_certificates_with_invalid_url(self, mock_db):
        """Test get_certificates with invalid URL."""
        mock_db.certificates.find.return_value = [
            {
                "name": "Certificate",
                "date": "2023-01-01",
                "issuer": "Test",
                "url": "not-a-valid-url"
            }
        ]

        with pytest.raises(ValidationError):
            get_certificates()


class TestGetSkills:
    """Test get_skills repository function."""

    @patch('database.repository.db')
    def test_get_skills_returns_list(self, mock_db):
        """Test that get_skills returns a list of Skill models."""
        mock_db.skills.find.return_value = [
            {
                "name": "Python",
                "level": "Advanced",
                "keywords": ["Django", "Flask", "FastAPI"]
            }
        ]

        result = get_skills()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], Skill)
        assert result[0].name == "Python"


class TestGetLanguages:
    """Test get_languages repository function."""

    @patch('database.repository.db')
    def test_get_languages_returns_list(self, mock_db):
        """Test that get_languages returns a list of Language models."""
        mock_db.languages.find.return_value = [
            {
                "language": "English",
                "fluency": "Native"
            }
        ]

        result = get_languages()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], Language)


class TestGetInterests:
    """Test get_interests repository function."""

    @patch('database.repository.db')
    def test_get_interests_returns_list(self, mock_db):
        """Test that get_interests returns a list of Interest models."""
        mock_db.interests.find.return_value = [
            {
                "name": "Coding",
                "keywords": ["Python", "Open Source"]
            }
        ]

        result = get_interests()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], Interest)


class TestGetReferences:
    """Test get_references repository function."""

    @patch('database.repository.db')
    def test_get_references_returns_list(self, mock_db):
        """Test that get_references returns a list of Reference models."""
        mock_db.references.find.return_value = [
            {
                "name": "John Doe",
                "reference": "Great colleague"
            }
        ]

        result = get_references()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], Reference)


class TestRepositoryPerformance:
    """Test repository performance with large datasets."""

    @patch('database.repository.db')
    def test_get_work_with_large_dataset(self, mock_db):
        """Test get_work performance with 100 items."""
        large_dataset = [
            {
                "name": f"Company {i}",
                "position": "Developer",
                "startDate": "2020-01",
                "endDate": "2021-01",
                "summary": "Summary",
                "highlights": []
            }
            for i in range(100)
        ]

        mock_db.work.find.return_value = large_dataset

        result = get_work()

        assert len(result) == 100
        assert all(isinstance(item, Work) for item in result)
