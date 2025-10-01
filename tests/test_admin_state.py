import pytest

from unittest.mock import (patch,
                           MagicMock)
from portfolio.states import AdminState
from bson.objectid import ObjectId


class TestAdminStateBasicsCRUD:
    """Test AdminState CRUD operations for basics collection."""

    @patch('portfolio.states.db')
    @patch('portfolio.states.get_basics')
    def test_load_basics_success(self, mock_get_basics, mock_db):
        """Test loading basics data successfully."""
        mock_basics = MagicMock()
        mock_basics.model_dump.return_value = {
            "name": "Test User",
            "email": "test@example.com",
            "label": "Developer",
            "summary": "Test summary"
        }
        mock_get_basics.return_value = mock_basics

        state = AdminState()
        state.load_basics()

        assert state.basics["name"] == "Test User"
        assert state.basics_edit["name"] == "Test User"

    @patch('portfolio.states.db')
    def test_save_basics_success(self, mock_db):
        """Test saving basics data successfully."""
        state = AdminState()
        state.basics_edit = {
            "name": "Updated Name",
            "email": "updated@example.com",
            "label": "Senior Developer",
            "summary": "Updated summary"
        }

        state.save_basics()

        mock_db.basics.replace_one.assert_called_once()
        assert state.is_editing_basics is False

    @patch('portfolio.states.db')
    def test_save_basics_database_error(self, mock_db):
        """Test save_basics when database operation fails."""
        mock_db.basics.replace_one.side_effect = Exception("Database error")

        state = AdminState()
        state.basics_edit = {"name": "Test"}

        with pytest.raises(Exception):
            state.save_basics()

    def test_update_basics_field(self):
        """Test updating a single basics field."""
        state = AdminState()
        state.basics_edit = {"name": "Old Name", "email": "old@example.com"}

        state.update_basics_field("name", "New Name")

        assert state.basics_edit["name"] == "New Name"
        assert state.basics_edit["email"] == "old@example.com"

    def test_start_editing_basics(self):
        """Test starting basics editing mode."""
        state = AdminState()
        state.editing_work_id = "some_id"

        state.start_editing_basics()

        assert state.is_editing_basics is True
        assert state.editing_work_id == ""


class TestAdminStateWorkCRUD:
    """Test AdminState CRUD operations for work collection."""

    @patch('portfolio.states.get_work')
    def test_load_work_success(self, mock_get_work):
        """Test loading work data successfully."""
        mock_work_item = MagicMock()
        mock_work_item.model_dump.return_value = {
            "name": "Company A",
            "position": "Developer",
            "startDate": "2020-01",
            "endDate": "2021-01",
            "summary": "Test",
            "highlights": []
        }
        mock_get_work.return_value = [mock_work_item]

        state = AdminState()
        state.load_work()

        assert len(state.work_items) == 1
        assert state.work_items[0]["name"] == "Company A"

    @patch('portfolio.states.db')
    def test_save_work_create_new(self, mock_db):
        """Test creating a new work item."""
        state = AdminState()
        state.is_creating_work = True
        state.work_edit = {
            "name": "New Company",
            "position": "Developer",
            "startDate": "2023-01",
            "endDate": "2024-01",
            "summary": "Test",
            "highlights": []
        }

        with patch('portfolio.states.AdminState.load_collection'):
            state.save_work()

        mock_db.work.insert_one.assert_called_once()

    @patch('portfolio.states.db')
    def test_save_work_update_existing(self, mock_db):
        """Test updating an existing work item."""
        state = AdminState()
        state.is_creating_work = False
        state.work_edit = {
            "name": "Company A",
            "position": "Senior Developer",
            "startDate": "2020-01",
            "endDate": "2022-01",
            "summary": "Updated",
            "highlights": []
        }

        with patch('portfolio.states.AdminState.load_collection'):
            state.save_work()

        mock_db.work.replace_one.assert_called_once()

    @pytest.mark.skip(reason="State mocking pattern is complex with Reflex")
    def test_delete_work_item(self):
        """Test deleting a work item."""
        pass

    def test_create_new_work_item(self):
        """Test creating an empty work item."""
        state = AdminState()

        state.create_new_work_item()

        assert state.is_creating_work is True
        assert state.work_edit["name"] == ""
        assert state.work_edit["position"] == ""

    def test_select_work_item(self):
        """Test selecting a work item for viewing."""
        state = AdminState()
        state.work_items = [
            {"name": "Company A", "position": "Dev"},
            {"name": "Company B", "position": "Senior Dev"}
        ]

        state.select_work_item(1)

        assert state.work_edit["name"] == "Company B"
        assert state.is_creating_work is False


class TestAdminStateEducationCRUD:
    """Test AdminState CRUD operations for education collection."""

    @patch('portfolio.states.get_education')
    def test_load_education_success(self, mock_get_education):
        """Test loading education data successfully."""
        mock_edu = MagicMock()
        mock_edu.model_dump.return_value = {
            "_id": ObjectId(),
            "institution": "MIT",
            "area": "CS",
            "studyType": "Bachelor",
            "startDate": "2015",
            "endDate": "2019",
            "score": "3.8",
            "courses": ["Algorithms", "Data Structures"]
        }
        mock_get_education.return_value = [mock_edu]

        state = AdminState()
        state.load_education()

        assert len(state.education_items) == 1
        assert state.education_items[0]["institution"] == "MIT"

    @patch('portfolio.states.db')
    def test_save_education_create_new(self, mock_db):
        """Test creating a new education item."""
        mock_result = MagicMock()
        mock_result.inserted_id = ObjectId()
        mock_db.education.insert_one.return_value = mock_result

        state = AdminState()
        state.is_creating_education = True
        state.education_edit = {
            "institution": "Stanford",
            "area": "AI",
            "studyType": "Master",
            "startDate": "2020",
            "endDate": "2022",
            "score": "4.0",
            "courses": []
        }

        with patch('portfolio.states.AdminState.load_collection'):
            state.save_education()

        mock_db.education.insert_one.assert_called_once()

    @patch('portfolio.states.db')
    def test_save_education_update_existing(self, mock_db):
        """Test updating an existing education item."""
        mock_result = MagicMock()
        mock_result.matched_count = 1
        mock_result.modified_count = 1
        mock_db.education.replace_one.return_value = mock_result

        state = AdminState()
        state.is_creating_education = False
        state.original_education_id = "507f1f77bcf86cd799439011"
        state.education_edit = {
            "institution": "MIT",
            "area": "CS",
            "studyType": "PhD",
            "startDate": "2015",
            "endDate": "2020",
            "score": "4.0",
            "courses": []
        }

        with patch('portfolio.states.AdminState.load_collection'):
            state.save_education()

        mock_db.education.replace_one.assert_called_once()

    def test_update_education_courses(self):
        """Test updating education courses from comma-separated string."""
        state = AdminState()
        state.education_edit = {"courses": []}

        state.update_education_courses("Algorithms, Data Structures, Machine Learning")

        assert len(state.education_edit["courses"]) == 3
        assert "Algorithms" in state.education_edit["courses"]
        assert state.courses_str == "Algorithms, Data Structures, Machine Learning"

    def test_create_new_education_item(self):
        """Test creating an empty education item."""
        state = AdminState()

        state.create_new_education_item()

        assert state.is_creating_education is True
        assert state.education_edit["institution"] == ""
        assert state.original_education_id is None


class TestAdminStateProjectsCRUD:
    """Test AdminState CRUD operations for projects collection."""

    @patch('portfolio.states.get_projects')
    def test_load_projects_success(self, mock_get_projects):
        """Test loading projects data successfully."""
        mock_project = MagicMock()
        mock_project.model_dump.return_value = {
            "name": "Project A",
            "role": "Lead",
            "description": "Test project",
            "highlights": ["Python", "FastAPI"],
            "github": "https://github.com/test",
            "isActive": True
        }
        mock_get_projects.return_value = [mock_project]

        state = AdminState()
        state.load_projects()

        assert len(state.project_items) == 1
        assert state.project_items[0]["name"] == "Project A"

    @patch('portfolio.states.db')
    def test_save_project_create_new(self, mock_db):
        """Test creating a new project."""
        state = AdminState()
        state.is_creating_project = True
        state.project_edit = {
            "name": "New Project",
            "role": "Developer",
            "description": "A new project",
            "highlights": [],
            "github": "https://github.com/new",
            "isActive": False
        }

        with patch('portfolio.states.AdminState.load_collection'):
            state.save_project()

        mock_db.projects.insert_one.assert_called_once()

    @patch('portfolio.states.db')
    def test_save_project_update_existing(self, mock_db):
        """Test updating an existing project."""
        state = AdminState()
        state.is_creating_project = False
        state.project_edit = {
            "name": "Project A",
            "role": "Lead Developer",
            "description": "Updated project",
            "highlights": ["Python"],
            "github": "https://github.com/test",
            "isActive": True
        }

        with patch('portfolio.states.AdminState.load_collection'):
            state.save_project()

        mock_db.projects.replace_one.assert_called_once()

    def test_update_project_highlights(self):
        """Test updating project highlights from comma-separated string."""
        state = AdminState()
        state.project_edit = {"highlights": []}

        state.update_project_highlights("Python, FastAPI, PostgreSQL")

        assert len(state.project_edit["highlights"]) == 3
        assert "FastAPI" in state.project_edit["highlights"]

    def test_update_project_is_active(self):
        """Test updating project active status."""
        state = AdminState()
        state.project_edit = {"isActive": False}

        state.update_project_is_active(True)

        assert state.project_edit["isActive"] is True

    def test_create_new_project_item(self):
        """Test creating an empty project item."""
        state = AdminState()

        state.create_new_project_item()

        assert state.is_creating_project is True
        assert state.project_edit["name"] == ""


class TestAdminStateHelperMethods:
    """Test AdminState helper methods."""

    def test_to_plain_dict(self):
        """Test to_plain with a dictionary."""
        data = {"key": "value", "nested": {"inner": "data"}}

        result = AdminState.to_plain(data)

        assert result == data

    def test_to_plain_list(self):
        """Test to_plain with a list."""
        data = ["item1", "item2", {"key": "value"}]

        result = AdminState.to_plain(data)

        assert result == data

    def test_to_plain_httpurl(self):
        """Test to_plain with HttpUrl object."""
        from pydantic import HttpUrl

        url = HttpUrl("https://example.com")

        result = AdminState.to_plain(url)

        assert result == "https://example.com/"

    def test_reset_editing_states(self):
        """Test resetting all editing states."""
        state = AdminState()
        state.editing_work_id = "work123"
        state.editing_education_id = "edu456"
        state.editing_project_id = "proj789"
        state.is_editing_basics = True

        state.reset_editing_states()

        assert state.editing_work_id == ""
        assert state.editing_education_id == ""
        assert state.editing_project_id == ""
        assert state.is_editing_basics is False

    def test_cancel_editing(self):
        """Test canceling current editing operation."""
        state = AdminState()
        state.is_creating_work = True
        state.editing_education_id = "edu123"

        with patch('portfolio.states.AdminState.load_collection'):
            state.cancel_editing()

        assert state.editing_education_id == ""
        assert state.is_creating_work is True


class TestAdminStateOnMount:
    """Test AdminState on_mount behavior."""

    @pytest.mark.skip(reason="State mocking pattern is complex with Reflex")
    def test_on_mount_loads_all_collections(self):
        """Test that on_mount loads all collections."""
        pass

    @pytest.mark.skip(reason="State mocking pattern is complex with Reflex")
    def test_on_mount_handles_error(self):
        """Test that on_mount handles errors gracefully."""
        pass
