import reflex as rx

from .config import get_logger
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


class AdminState(rx.State):
    selected_collection: str = "basics"

    # Track if creating new items
    is_creating_work: bool = False
    is_creating_education: bool = False
    is_creating_project: bool = False

    # Basics
    basics: dict = {}
    basics_edit: dict = {}

    # Work
    work_items: List[WorkItem] = []
    work_edit: WorkItem = {}

    # Education
    education_items: List[EducationItem] = []
    education_edit: EducationItem = {}
    original_institution: str = ""

    # Projects
    project_items: List[ProjectItem] = []
    project_edit: ProjectItem = {}

    # String representations for UI
    courses_str: str = ""
    highlights_str: str = ""


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
        Handles HttpUrl objects by converting them to strings.
        
        Args:
            obj: Any Python object to convert (dict, list, or primitive)
            
        Returns:
            Union[dict, list, Any]: Plain Python data structure compatible with MongoDB
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
        self.load_basics()
        self.load_work()
        self.load_education()
        self.load_projects()


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
        self.load_collection("projects")


    def toggle_admin_modal(self) -> None:
        """Toggle the admin modal visibility and load selected collection data."""
        self.show_admin_modal = not self.show_admin_modal
        if self.show_admin_modal:
            self.load_collection(self.selected_collection)


    def load_collection(self, collection: str) -> None:
        """
        Load and prepare collection data for the admin panel editing interface.
        
        Args:
            collection: The name of the collection to load. Supported values:
                    - 'basics': Personal information and contact details
                    - 'work': Work experience history
                    - 'education': Educational background and qualifications  
                    - 'projects': Portfolio projects and technical work
        
        Workflow:
            1. Sets the currently selected collection for UI tracking
            2. Retrieves raw data from MongoDB via repository functions
            3. Converts Pydantic models to dictionaries for state compatibility
            4. Transforms data into TypedDict format for type-safe UI operations
            5. Initializes edit states with first item or empty templates
            6. Updates derived UI states (string representations, flags)
        
        Data Processing:
            - Handles both Pydantic model instances and raw dictionaries
            - Converts complex types (HttpUrl) to strings for UI compatibility  
            - Maintains type safety through TypedDict conversions
            - Preserves data integrity across the loading pipeline
        
        State Management:
            - Populates main state arrays (work_items, education_items, etc.)
            - Initializes edit states (work_edit, education_edit, etc.)
            - Resets creation flags and tracking variables
            - Updates string representations for list-based fields
        
        Raises:
            AttributeError: If collection data structure is unexpected
            KeyError: If required fields are missing from source data
        """
        self.selected_collection = collection

        if collection == "basics":
            basics_data = get_basics() or {}
            if basics_data and hasattr(basics_data, 'model_dump'):
                basics_data = basics_data.model_dump()
            self.basics = basics_data
            self.basics_edit = dict(basics_data)

        elif collection == "work":
            raw_work = get_work() or []
            work_dicts = []
            for item in raw_work:
                if hasattr(item, 'model_dump'):
                    work_dicts.append(item.model_dump())
                else:
                    work_dicts.append(item)
                    
            self.work_items = [
                self._convert_to_work_item(item) for item in work_dicts
            ]
            
            if self.work_items:
                self.work_edit = self.work_items[0]
            else:
                self.work_edit = WorkItem(
                    name="",
                    position="",
                    url=None,
                    startDate="",
                    endDate="",
                    summary="",
                    highlights=[]
                )

        elif collection == "education":
            raw_education = get_education() or []
            education_dicts = []
            for item in raw_education:
                if hasattr(item, 'model_dump'):
                    education_dicts.append(item.model_dump())
                else:
                    education_dicts.append(item)
                    
            self.education_items = [
                self._convert_to_education_item(item) for item in education_dicts
            ]
            
            if self.education_items:
                self.education_edit = self.education_items[0]
            else:
                self.education_edit = EducationItem(
                    institution="",
                    url=None,
                    area="",
                    studyType="",
                    startDate="",
                    endDate="",
                    score="",
                    courses=[]
                )
            self._update_courses_str()

            self.original_institution = ""
            logger.debug("Reset original_institution on collection load")
            
            self.is_creating_education = False
            logger.debug(f"After load, is_creating_education = {self.is_creating_education}")
            
        elif collection == "projects":
            raw_projects = get_projects() or []
            project_dicts = []
            for item in raw_projects:
                if hasattr(item, 'model_dump'):
                    project_dicts.append(item.model_dump())
                else:
                    project_dicts.append(item)
                    
            self.project_items = [
                ProjectItem(
                    name=item.get("name", ""),
                    role=item.get("role", ""),
                    description=item.get("description", ""),
                    highlights=item.get("highlights") or [],
                    github=item.get("github", ""),
                    isActive=item.get("isActive", False)
                )
                for item in project_dicts
            ]
            if self.project_items:
                self.project_edit = self.project_items[0]
            else:
                self.project_edit = ProjectItem(
                    name="", role="", description="", highlights=[], github="", isActive=False
                )
            self._update_highlights_str()


    # Basics methods
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


    # Work methods
    def _convert_to_work_item(self, data: dict) -> WorkItem:
        """Convert dictionary to WorkItem, handling HttpUrl conversion."""
        return WorkItem(
            name=data.get("name", ""),
            position=data.get("position", ""),
            url=str(data["url"]) if data.get("url") else None,
            startDate=data.get("startDate", ""),
            endDate=data.get("endDate", ""),
            summary=data.get("summary", ""),
            highlights=data.get("highlights") or []
        )


    def select_work_item(self, idx: Union[str, float, int]) -> None:
        """Select a work item for editing."""
        idx = int(idx) if isinstance(idx, (str, float)) else idx
        if isinstance(idx, int) and 0 <= idx < len(self.work_items):
            self.work_edit = self.work_items[idx]
            self.is_creating_work = False


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


    def create_new_work_item(self) -> None:
        """Create a new empty work item."""
        self.work_edit = WorkItem(
            name="",
            position="", 
            url=None,
            startDate="",
            endDate="",
            summary="",
            highlights=[]
        )
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
    def _convert_to_education_item(self, data: dict) -> EducationItem:
        """Convert dictionary to EducationItem, handling HttpUrl conversion."""
        return EducationItem(
            institution=data.get("institution", ""),
            url=str(data["url"]) if data.get("url") else None,
            area=data.get("area", ""),
            studyType=data.get("studyType", ""),
            startDate=data.get("startDate", ""),
            endDate=data.get("endDate", ""),
            score=data.get("score", ""),
            courses=data.get("courses") or []
        )


    def select_education_item(self, idx: Union[str, float, int]) -> None:
        """Select an education item for editing."""
        logger.debug(f"select_education_item called with idx={idx}, type={type(idx)}")
        
        idx = int(idx) if isinstance(idx, (str, float)) else idx
        
        if isinstance(idx, int) and 0 <= idx < len(self.education_items):
            selected_item = self.education_items[idx]
            logger.debug(f"Selected institution: {selected_item.get('institution')}")
            
            self.original_institution = selected_item.get("institution", "")
            logger.debug(f"Original institution saved: {self.original_institution}")
            
            self.education_edit = EducationItem(
                institution=selected_item.get("institution", ""),
                url=selected_item.get("url"),
                area=selected_item.get("area", ""),
                studyType=selected_item.get("studyType", ""),
                startDate=selected_item.get("startDate", ""),
                endDate=selected_item.get("endDate", ""),
                score=selected_item.get("score", ""),
                courses=selected_item.get("courses") or []
            )
            
            self._update_courses_str()
            self.is_creating_education = False
            logger.info(f"Education item selected for editing: {self.original_institution}")


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
        logger.debug(f"original_institution: {self.original_institution}")
        
        education_doc = self.to_plain(self.education_edit)
        
        if self.is_creating_education:
            logger.info("Creating NEW education item")
            result = db.education.insert_one(education_doc)
            logger.info(f"New education item created with id: {result.inserted_id}")
        else:
            logger.info("UPDATING existing education item")
            
            filter_query = {"institution": self.original_institution}
            logger.debug(f"Searching for education item with: {filter_query}")
            
            result = db.education.replace_one(
                filter_query, 
                education_doc, 
                upsert=True
            )
            logger.info(f"Education item updated, matched: {result.matched_count}, modified: {result.modified_count}")
            
            if result.matched_count == 0:
                logger.warning(f"No education item found with institution: {self.original_institution}")
        
        self.load_collection("education")
        self.is_creating_education = False
        self.original_institution = ""
        logger.debug(f"After save, is_creating_education = {self.is_creating_education}")


    def create_new_education_item(self) -> None:
        """Create a new empty education item."""
        logger.info("Creating new empty education item")
        self.education_edit = EducationItem(
            institution="",
            url=None,
            area="",
            studyType="", 
            startDate="",
            endDate="",
            score="",
            courses=[]
        )
        self._update_courses_str()
        self.is_creating_education = True
        self.original_institution = ""
        logger.debug(f"Set is_creating_education to {self.is_creating_education}")


    def delete_education_item(self, idx: int) -> None:
        """Delete an education item."""
        if 0 <= idx < len(self.education_items):
            item = self.education_items[idx]
            db.education.delete_one({"institution": item["institution"]})
            self.load_collection("education")
            if self.education_edit.get("institution") == item["institution"]:
                self.create_new_education_item()


    # Projects methods
    def select_project_item(self, idx: Union[str, float, int]) -> None:
        """Select a project item for editing."""
        idx = int(idx) if isinstance(idx, (str, float)) else idx
        if isinstance(idx, int) and 0 <= idx < len(self.project_items):
            self.project_edit = self.project_items[idx]
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
        project_doc = self.to_plain(self.project_edit)
        
        if self.is_creating_project:
            db.projects.insert_one(project_doc)
        else:
            db.projects.replace_one({"name": project_doc["name"]}, project_doc, upsert=True)
        
        self.load_collection("projects")
        self.is_creating_project = False


    def create_new_project_item(self) -> None:
        """Create a new empty project item."""
        new_project = ProjectItem(
            name="",
            role="",
            description="",
            highlights=[],
            github="",
            isActive=False
        )
        self.project_edit = new_project
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
