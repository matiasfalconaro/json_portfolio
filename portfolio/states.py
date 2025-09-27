import reflex as rx

from database.db import db
from database.repository import (get_basics,
                                 get_work,
                                 get_education,
                                 get_projects)
from typing import (List,
                    TypedDict)


class States(rx.State):
    show_modal: bool = False
    show_code_modal: bool = False

    def toggle_modal(self):
        self.show_modal = not self.show_modal

    def toggle_code_modal(self):
        self.show_code_modal = not self.show_code_modal


class WorkItem(TypedDict):
    name: str
    position: str
    startDate: str
    endDate: str
    summary: str
    highlights: List[str]


class EducationItem(TypedDict):
    institution: str
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

    # Basics
    basics: dict = {}
    basics_edit: dict = {}

    # Work
    work_items: List[WorkItem] = []
    work_edit: WorkItem = {}

    # Education
    education_items: List[EducationItem] = []
    education_edit: EducationItem = {}

    # Projects
    project_items: List[ProjectItem] = []
    project_edit: ProjectItem = {}

    # String representations for UI
    courses_str: str = ""
    highlights_str: str = ""


    def _update_courses_str(self):
        """Update courses string representation"""
        courses = self.education_edit.get("courses", [])
        if isinstance(courses, list):
            self.courses_str = ", ".join(courses)
        else:
            self.courses_str = ""


    def _update_highlights_str(self):
        """Update highlights string representation"""
        highlights = self.project_edit.get("highlights", [])
        if isinstance(highlights, list):
            self.highlights_str = ", ".join(highlights)
        else:
            self.highlights_str = ""


    @staticmethod
    def to_plain(obj):
        """Convierte Rx State a dict/lists plain para DB."""
        if isinstance(obj, dict):
            return {k: AdminState.to_plain(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [AdminState.to_plain(v) for v in obj]
        return obj


    def on_mount(self):
        """Load all data on mount."""
        self.load_basics()
        self.load_work()
        self.load_education()
        self.load_projects()


    def load_basics(self):
        self.load_collection("basics")


    def load_work(self):
        self.load_collection("work")


    def load_education(self):
        self.load_collection("education")


    def load_projects(self):
        self.load_collection("projects")


    def toggle_admin_modal(self):
        self.show_admin_modal = not self.show_admin_modal
        if self.show_admin_modal:
            self.load_collection(self.selected_collection)


    def load_collection(self, collection: str):
        """Carga la colección seleccionada."""
        self.selected_collection = collection

        if collection == "basics":
            basics_data = get_basics() or {}
            self.basics = basics_data
            self.basics_edit = dict(basics_data)

        elif collection == "work":
            raw_work = get_work() or []
            self.work_items = [
                WorkItem(
                    name=item.get("name", ""),
                    position=item.get("position", ""),
                    startDate=item.get("startDate", ""),
                    endDate=item.get("endDate", ""),
                    summary=item.get("summary", ""),
                    highlights=item.get("highlights") or []
                )
                for item in raw_work
            ]
            self.work_edit = self.work_items[0] if self.work_items else WorkItem(
                name="", position="", startDate="", endDate="", summary="", highlights=[]
            )

        elif collection == "education":
            raw_education = get_education() or []
            self.education_items = [
                EducationItem(
                    institution=item.get("institution", ""),
                    area=item.get("area", ""),
                    studyType=item.get("studyType", ""),
                    startDate=item.get("startDate", ""),
                    endDate=item.get("endDate", ""),
                    score=item.get("score", ""),
                    courses=item.get("courses") or []
                )
                for item in raw_education
            ]
            self.education_edit = self.education_items[0] if self.education_items else EducationItem(
                institution="", area="", studyType="", startDate="", endDate="", score="", courses=[]
            )
            self._update_courses_str()

        elif collection == "projects":
            raw_projects = get_projects() or []
            self.project_items = [
                ProjectItem(
                    name=item.get("name", ""),
                    role=item.get("role", ""),
                    description=item.get("description", ""),
                    highlights=item.get("highlights") or [],
                    github=item.get("github", ""),
                    isActive=item.get("isActive", False)
                )
                for item in raw_projects
            ]
            self.project_edit = self.project_items[0] if self.project_items else ProjectItem(
                name="", role="", description="", highlights=[], github="", isActive=False
            )
            self._update_highlights_str()


    # Basics methods
    def update_basics_field(self, field: str, value: str):
        if field in self.basics_edit:
            self.basics_edit[field] = value


    def save_basics(self):
        basics_doc = self.to_plain(self.basics_edit)
        db.basics.replace_one({}, basics_doc, upsert=True)
        self.basics = basics_doc
        self.basics_edit = dict(basics_doc)


    # Work methods
    def select_work_item(self, idx):
        idx = int(idx) if isinstance(idx, (str, float)) else idx
        if isinstance(idx, int) and 0 <= idx < len(self.work_items):
            self.work_edit = self.work_items[idx]


    def update_work_field(self, field: str, value: str):
        if field in self.work_edit:
            self.work_edit[field] = value


    def save_work(self):
        work_doc = self.to_plain(self.work_edit)
        db.work.replace_one({"name": work_doc["name"]}, work_doc, upsert=True)
        self.load_collection("work")


    # Education methods
    def select_education_item(self, idx):
        idx = int(idx) if isinstance(idx, (str, float)) else idx
        if isinstance(idx, int) and 0 <= idx < len(self.education_items):
            self.education_edit = self.education_items[idx]
            self._update_courses_str()


    def update_education_field(self, field: str, value: str):
        if field in self.education_edit:
            self.education_edit[field] = value


    def update_education_courses(self, courses_str: str):
        """Update courses from comma-separated string"""
        courses = [course.strip() for course in courses_str.split(",") if course.strip()]
        self.education_edit["courses"] = courses
        self.courses_str = courses_str


    def save_education(self):
        education_doc = self.to_plain(self.education_edit)
        db.education.replace_one({"institution": education_doc["institution"]}, education_doc, upsert=True)
        self.load_collection("education")


    # Projects methods
    def select_project_item(self, idx):
        idx = int(idx) if isinstance(idx, (str, float)) else idx
        if isinstance(idx, int) and 0 <= idx < len(self.project_items):
            self.project_edit = self.project_items[idx]
            self._update_highlights_str()


    def update_project_field(self, field: str, value: str):
        if field in self.project_edit:
            self.project_edit[field] = value


    def update_project_highlights(self, highlights_str: str):
        """Update highlights from comma-separated string"""
        highlights = [highlight.strip() for highlight in highlights_str.split(",") if highlight.strip()]
        self.project_edit["highlights"] = highlights
        self.highlights_str = highlights_str


    def update_project_is_active(self, is_active: bool):
        self.project_edit["isActive"] = is_active


    def save_project(self):
        project_doc = self.to_plain(self.project_edit)
        db.projects.replace_one({"name": project_doc["name"]}, project_doc, upsert=True)
        self.load_collection("projects")
