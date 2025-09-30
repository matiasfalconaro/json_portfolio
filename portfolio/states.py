import reflex as rx

from .config import get_logger
from bson.objectid import ObjectId
from database.db import db
from database.repository import (get_basics,
                                 get_work,
                                 get_education,
                                 get_projects)
from typing import (List,
                    TypedDict,
                    Any,
                    Optional,
                    Union)


logger = get_logger(__name__)


class States(rx.State):
    show_modal: bool = False
    show_code_modal: bool = False

    def toggle_modal(self) -> None:
        """Toggle the contact modal visibility state."""
        self.show_modal = not self.show_modal

    def toggle_code_modal(self) -> None:
        """Toggle the code information modal visibility state."""
        self.show_code_modal = not self.show_code_modal


class WorkItem(TypedDict):
    name: str
    position: str
    url: Optional[str]
    startDate: str
    endDate: str
    summary: str
    highlights: List[str]


class EducationItem(TypedDict):
    institution: str
    url: Optional[str] 
    area: str
    studyType: str
    startDate: str
    endDate: str
    score: str
    courses: List[str]


class ProjectItem(TypedDict):
    name: str
    role: str
    description: str
    highlights: List[str]
    github: str
    isActive: bool
    url: Optional[str]


class AdminState(rx.State):
    selected_collection: str = "basics"

    # Track if creating new items
    is_creating_work: bool = False
    is_creating_education: bool = False
    is_creating_project: bool = False

    # Track editing state for each collection
    editing_work_id: str = ""
    editing_education_id: str = ""
    editing_project_id: str = ""

    # Track current view mode
    is_editing_basics: bool = False

    # Basics
    basics: dict = {}
    basics_edit: dict = {}

    # Work
    work_items: List[dict] = []
    work_edit: dict = {}

    # Education
    education_items: List[dict] = []
    education_edit: dict = {}
    original_education_id: Optional[str] = None

    # Projects
    project_items: List[dict] = []
    project_edit: dict = {}

    # String representations for UI
    courses_str: str = ""
    highlights_str: str = ""


    def reset_editing_states(self):
        """Reset all editing states."""
        self.editing_work_id = ""
        self.editing_education_id = ""
        self.editing_project_id = ""
        self.is_editing_basics = False


    def cancel_editing(self):
        """Cancel current editing operation."""
        was_creating_work = self.is_creating_work
        was_creating_education = self.is_creating_education
        was_creating_project = self.is_creating_project
        
        self.reset_editing_states()
        self.load_collection(self.selected_collection)
        
        self.is_creating_work = was_creating_work
        self.is_creating_education = was_creating_education
        self.is_creating_project = was_creating_project


    def _update_courses_str(self) -> None:
        """Update courses string representation from education_edit courses list."""
        courses = self.education_edit.get("courses", [])
        if isinstance(courses, list):
            self.courses_str = ", ".join(courses)
        else:
            self.courses_str = ""


    def _update_highlights_str(self) -> None:
        """Update highlights string representation from project_edit highlights list."""
        highlights = self.project_edit.get("highlights", [])
        if isinstance(highlights, list):
            self.highlights_str = ", ".join(highlights)
        else:
            self.highlights_str = ""


    @staticmethod
    def to_plain(obj: Any) -> Union[dict, list, Any]:
        """
        Convert Reflex State objects to plain Python dict/lists for database operations.
        """
        if isinstance(obj, dict):
            return {k: AdminState.to_plain(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [AdminState.to_plain(v) for v in obj]
        elif hasattr(obj, '__str__') and hasattr(obj, 'scheme') and hasattr(obj, 'host'):
            return str(obj)
        else:
            return obj


    def on_mount(self) -> None:
        """Load all portfolio data when the component mounts."""
        try:
            self.load_basics()
            self.load_work()
            self.load_education()
            self.load_projects()
        except Exception as e:
            logger.error(f"Error loading data on mount: {e}")

    def load_basics(self) -> None:
        """Load basics data from the database."""
        self.load_collection("basics")


    def load_work(self) -> None:
        """Load work experience data from the database."""
        self.load_collection("work")


    def load_education(self) -> None:
        """Load education data from the database."""
        self.load_collection("education")


    def load_projects(self) -> None:
        """Load projects data from the database."""
        try:
            self.load_collection("projects")
        except Exception as e:
            logger.error(f"Error loading projects: {e}")
            self.project_items = []
            self.project_edit = {
                "name": "", 
                "role": "", 
                "description": "", 
                "highlights": [], 
                "github": "", 
                "isActive": False,
                "url": None
            }

    def toggle_admin_modal(self) -> None:
        """Toggle the admin modal visibility and load selected collection data."""
        self.show_admin_modal = not self.show_admin_modal
        if self.show_admin_modal:
            self.load_collection(self.selected_collection)


    def load_collection(self, collection: str) -> None:
        """Load and prepare collection data for editing."""
        self.selected_collection = collection

        if collection == "basics":
            basics_data = get_basics() or {}
            if basics_data and hasattr(basics_data, 'model_dump'):
                basics_data = basics_data.model_dump()
            self.basics = basics_data
            self.basics_edit = dict(basics_data)

        elif collection == "work":
            try:
                raw_work = get_work() or []
                work_dicts = []
                for item in raw_work:
                    if hasattr(item, 'model_dump'):
                        work_dicts.append(item.model_dump())
                    else:
                        work_dicts.append(item)
                        
                self.work_items = work_dicts
                
                if self.work_items:
                    self.work_edit = dict(self.work_items[0])
                else:
                    self.work_edit = {
                        "name": "",
                        "position": "",
                        "url": None,
                        "startDate": "",
                        "endDate": "",
                        "summary": "",
                        "highlights": []
                    }
            except Exception as e:
                logger.error(f"Error loading work: {e}")
                self.work_items = []
                self.work_edit = {}

        elif collection == "education":
            try:
                raw_education = get_education() or []
                education_dicts = []
                for item in raw_education:
                    if hasattr(item, 'model_dump'):
                        education_dicts.append(item.model_dump())
                    else:
                        education_dicts.append(item)
                        
                self.education_items = education_dicts
                
                if self.education_items:
                    first_item = self.education_items[0]
                    self.education_edit = dict(first_item)
                    if education_dicts and "_id" in education_dicts[0]:
                        self.original_education_id = str(education_dicts[0]["_id"])
                    else:
                        self.original_education_id = None
                else:
                    self.education_edit = {
                        "institution": "",
                        "url": None,
                        "area": "",
                        "studyType": "",
                        "startDate": "",
                        "endDate": "",
                        "score": "",
                        "courses": []
                    }
                    self.original_education_id = None
                
                self.is_creating_education = False
                self._update_courses_str()
                logger.debug(f"After load, is_creating_education = {self.is_creating_education}")
            except Exception as e:
                logger.error(f"Error loading education: {e}")
                self.education_items = []
                self.education_edit = {}

        elif collection == "projects":
            try:
                raw_projects = get_projects() or []
                project_dicts = []
                for item in raw_projects:
                    if hasattr(item, 'model_dump'):
                        project_dicts.append(item.model_dump())
                    else:
                        project_dicts.append(item)
                        
                self.project_items = project_dicts
                
                if self.project_items:
                    self.project_edit = dict(self.project_items[0])
                else:
                    self.project_edit = {
                        "name": "", 
                        "role": "", 
                        "description": "", 
                        "highlights": [], 
                        "github": "", 
                        "isActive": False,
                        "url": None
                    }
                self._update_highlights_str()
            except Exception as e:
                logger.error(f"Error loading projects: {e}")
                self.project_items = []
                self.project_edit = {
                    "name": "", 
                    "role": "", 
                    "description": "", 
                    "highlights": [], 
                    "github": "", 
                    "isActive": False,
                    "url": None
                }


    # Basics methods
    def start_editing_basics(self):
        """Start editing basics."""
        self.reset_editing_states()
        self.is_editing_basics = True


    def update_basics_field(self, field: str, value: str) -> None:
        """Update a specific field in the basics edit state."""
        if field in self.basics_edit:
            self.basics_edit[field] = value


    def save_basics(self) -> None:
        """Save basics data to the database and update local state."""
        basics_doc = self.to_plain(self.basics_edit)
        db.basics.replace_one({}, basics_doc, upsert=True)
        self.basics = basics_doc
        self.basics_edit = dict(basics_doc)
        self.is_editing_basics = False


    # Work methods
    def start_editing_work(self, idx: int):
        """Start editing a work item."""
        self.reset_editing_states()
        if 0 <= idx < len(self.work_items):
            self.work_edit = dict(self.work_items[idx])

            raw_work = get_work() or []
            if idx < len(raw_work):
                raw_item = raw_work[idx]
                if hasattr(raw_item, 'model_dump'):
                    raw_dict = raw_item.model_dump()
                else:
                    raw_dict = raw_item
                
                if "_id" in raw_dict:
                    self.editing_work_id = str(raw_dict["_id"])
                else:
                    self.editing_work_id = raw_dict.get("name", "")
            else:
                self.editing_work_id = self.work_items[idx].get("name", "")
            
            self.is_creating_work = False


    def select_work_item(self, idx: Union[str, float, int]) -> None:
        """Select a work item for viewing."""
        idx = int(idx) if isinstance(idx, (str, float)) else idx
        if isinstance(idx, int) and 0 <= idx < len(self.work_items):
            self.work_edit = dict(self.work_items[idx])
            self.is_creating_work = False
            self.editing_work_id = ""


    def update_work_field(self, field: str, value: str) -> None:
        """Update a specific field in the work edit state."""
        if field in self.work_edit:
            self.work_edit[field] = value


    def save_work(self) -> None:
        """Save work item - handles both create and update."""
        work_doc = self.to_plain(self.work_edit)
        
        if self.is_creating_work:
            db.work.insert_one(work_doc)
        else:
            db.work.replace_one({"name": work_doc["name"]}, work_doc, upsert=True)
        
        self.load_collection("work")
        self.is_creating_work = False
        self.editing_work_id = ""


    def create_new_work_item(self) -> None:
        """Create a new empty work item."""
        self.work_edit = {
            "name": "",
            "position": "", 
            "url": None,
            "startDate": "",
            "endDate": "",
            "summary": "",
            "highlights": []
        }
        self.is_creating_work = True


    def delete_work_item(self, idx: int) -> None:
        """Delete a work item."""
        if 0 <= idx < len(self.work_items):
            item = self.work_items[idx]
            db.work.delete_one({"name": item["name"]})
            self.load_collection("work")
            if self.work_edit.get("name") == item["name"]:
                self.create_new_work_item()


    # Education methods
    def start_editing_education(self, idx: int):
        """Start editing an education item."""
        self.reset_editing_states()
        if 0 <= idx < len(self.education_items):
            selected_item = self.education_items[idx]
            self.education_edit = dict(selected_item)
            self._update_courses_str()

            raw_education = get_education() or []
            if idx < len(raw_education):
                raw_item = raw_education[idx]
                if hasattr(raw_item, 'model_dump'):
                    raw_dict = raw_item.model_dump()
                else:
                    raw_dict = raw_item
                
                if "_id" in raw_dict:
                    self.original_education_id = str(raw_dict["_id"])
                    self.editing_education_id = self.original_education_id
                else:
                    self.original_education_id = None
            else:
                self.original_education_id = None
            
            self.is_creating_education = False


    def select_education_item(self, idx: Union[str, float, int]) -> None:
        """Select an education item for editing."""
        logger.debug(f"select_education_item called with idx={idx}, type={type(idx)}")
        
        idx = int(idx) if isinstance(idx, (str, float)) else idx
        
        if isinstance(idx, int) and 0 <= idx < len(self.education_items):
            selected_item = self.education_items[idx]
            logger.debug(f"Selected institution: {selected_item.get('institution')}")
            
            raw_education = get_education() or []
            if idx < len(raw_education):
                raw_item = raw_education[idx]
                if hasattr(raw_item, 'model_dump'):
                    raw_dict = raw_item.model_dump()
                else:
                    raw_dict = raw_item
                
                if "_id" in raw_dict:
                    self.original_education_id = str(raw_dict["_id"])
                else:
                    self.original_education_id = None
            
            logger.debug(f"Original education _id saved: {self.original_education_id}")
            
            self.education_edit = dict(selected_item)
            self._update_courses_str()
            self.is_creating_education = False
            logger.info(f"Education item selected for editing with _id: {self.original_education_id}")


    def update_education_field(self, field: str, value: str) -> None:
        """Update a specific field in the education edit state."""
        if field in self.education_edit:
            self.education_edit[field] = value


    def update_education_courses(self, courses_str: str) -> None:
        """Update courses from comma-separated string"""
        courses = [course.strip() for course in courses_str.split(",") if course.strip()]
        self.education_edit["courses"] = courses
        self.courses_str = courses_str


    def save_education(self) -> None:
        """Save education item - handles both create and update."""
        logger.info(f"save_education called, is_creating_education = {self.is_creating_education}")
        logger.debug(f"education_edit institution: {self.education_edit.get('institution')}")
        logger.debug(f"original_education_id: {self.original_education_id}")
        
        education_doc = self.to_plain(self.education_edit)
        
        if self.is_creating_education:
            logger.info("Creating NEW education item")
            result = db.education.insert_one(education_doc)
            logger.info(f"New education item created with id: {result.inserted_id}")
        else:
            logger.info("UPDATING existing education item")
            
            if self.original_education_id and len(self.original_education_id) == 24:
                try:
                    filter_query = {"_id": ObjectId(self.original_education_id)}
                    logger.debug(f"Searching for education item with _id: {self.original_education_id}")
                    
                    result = db.education.replace_one(filter_query, education_doc, upsert=False)
                    logger.info(f"Education item updated, matched: {result.matched_count}, modified: {result.modified_count}")
                    
                    if result.matched_count == 0:
                        logger.warning(f"No education item found with _id: {self.original_education_id}")
                        db.education.insert_one(education_doc)
                        logger.info("Inserted as new item due to no match")
                except Exception as e:
                    logger.error(f"Error updating education: {e}")
                    db.education.insert_one(education_doc)
                    logger.info("Inserted as new item due to error")
            else:
                logger.warning("No valid original_education_id, inserting as new item")
                db.education.insert_one(education_doc)
        
        self.load_collection("education")
        self.is_creating_education = False
        self.original_education_id = None
        self.editing_education_id = ""
        logger.debug(f"After save, is_creating_education = {self.is_creating_education}")


    def create_new_education_item(self) -> None:
        """Create a new empty education item."""
        logger.info("Creating new empty education item")
        self.education_edit = {
            "institution": "",
            "url": None,
            "area": "",
            "studyType": "", 
            "startDate": "",
            "endDate": "",
            "score": "",
            "courses": []
        }
        self._update_courses_str()
        self.is_creating_education = True
        self.original_education_id = None
        logger.debug(f"Set is_creating_education to {self.is_creating_education}")


    def delete_education_item(self, idx: int) -> None:
        """Delete an education item."""
        if 0 <= idx < len(self.education_items):
            item = self.education_items[idx]
            raw_education = get_education() or []
            if idx < len(raw_education):
                raw_item = raw_education[idx]
                if hasattr(raw_item, 'model_dump'):
                    raw_dict = raw_item.model_dump()
                else:
                    raw_dict = raw_item
                
                if "_id" in raw_dict:
                    db.education.delete_one({"_id": ObjectId(raw_dict["_id"])})
                else:
                    db.education.delete_one({"institution": item["institution"]})
            
            self.load_collection("education")
            if self.education_edit.get("institution") == item["institution"]:
                self.create_new_education_item()


    # Projects methods
    def start_editing_project(self, idx: int):
        """Start editing a project item."""
        self.reset_editing_states()
        if 0 <= idx < len(self.project_items):
            self.project_edit = dict(self.project_items[idx])
            self._update_highlights_str()
            self.editing_project_id = self.project_items[idx].get("name", "")
            self.is_creating_project = False


    def select_project_item(self, idx: Union[str, float, int]) -> None:
        """Select a project item for editing."""
        idx = int(idx) if isinstance(idx, (str, float)) else idx
        if isinstance(idx, int) and 0 <= idx < len(self.project_items):
            self.project_edit = dict(self.project_items[idx])
            self._update_highlights_str()
            self.is_creating_project = False


    def update_project_field(self, field: str, value: str) -> None:
        """Update a specific field in the project edit state."""
        if field in self.project_edit:
            self.project_edit[field] = value


    def update_project_highlights(self, highlights_str: str) -> None:
        """Update highlights from comma-separated string"""
        highlights = [highlight.strip() for highlight in highlights_str.split(",") if highlight.strip()]
        self.project_edit["highlights"] = highlights
        self.highlights_str = highlights_str


    def update_project_is_active(self, is_active: bool) -> None:
        """Update project active status."""
        self.project_edit["isActive"] = is_active


    def save_project(self) -> None:
        """Save project item - handles both create and update."""
        try:
            project_doc = self.to_plain(self.project_edit)
            
            if "url" not in project_doc:
                project_doc["url"] = None
            
            if self.is_creating_project:
                db.projects.insert_one(project_doc)
            else:
                db.projects.replace_one({"name": project_doc["name"]}, project_doc, upsert=True)
            
            self.load_collection("projects")
            self.is_creating_project = False
            self.editing_project_id = ""
        except Exception as e:
            logger.error(f"Error saving project: {e}")


    def create_new_project_item(self) -> None:
        """Create a new empty project item."""
        self.project_edit = {
            "name": "",
            "role": "",
            "description": "",
            "highlights": [],
            "github": "",
            "isActive": False,
            "url": None
        }
        self._update_highlights_str()
        self.is_creating_project = True


    def delete_project_item(self, idx: int) -> None:
        """Delete a project item."""
        if 0 <= idx < len(self.project_items):
            item = self.project_items[idx]
            db.projects.delete_one({"name": item["name"]})
            self.load_collection("projects")
            if self.project_edit.get("name") == item["name"]:
                self.create_new_project_item()
