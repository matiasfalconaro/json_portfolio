import reflex as rx

from database.db import db
from database.repository import (get_basics,
                                 get_work)
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


class AdminState(rx.State):
    selected_collection: str = "basics"

    basics: dict = get_basics() or {}
    basics_edit: dict = dict(basics)

    work_items: List[WorkItem] = [
        WorkItem(
            name=item.get("name", ""),
            position=item.get("position", ""),
            startDate=item.get("startDate", ""),
            endDate=item.get("endDate", ""),
            summary=item.get("summary", ""),
            highlights=item.get("highlights") or []
        )
        for item in (get_work() or [])
    ]
    work_edit: WorkItem = work_items[0] if work_items else WorkItem(
        name="", position="", startDate="", endDate="", summary="", highlights=[]
    )


    @staticmethod
    def to_plain(obj):
        """Convierte Rx State a dict/lists plain para DB."""
        if isinstance(obj, dict):
            return {k: AdminState.to_plain(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [AdminState.to_plain(v) for v in obj]
        return obj


    def load_basics(self):
        self.load_collection("basics")


    def load_work(self):
        self.load_collection("work")


    def toggle_admin_modal(self):
        self.show_admin_modal = not self.show_admin_modal
        if self.show_admin_modal:
            self.load_collection(self.selected_collection)


    def load_collection(self, collection: str):
        """Carga la colección seleccionada."""
        self.selected_collection = collection

        if collection == "basics":
            self.basics = get_basics() or {}
            self.basics_edit = dict(self.basics)

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


    def update_basics_field(self, field: str, value: str):
        self.basics_edit[field] = value


    def save_basics(self):
        basics_doc = self.to_plain(self.basics_edit)
        db.basics.replace_one({}, basics_doc, upsert=True)
        self.basics = basics_doc
        self.basics_edit = dict(basics_doc)


    def select_work_item(self, idx):
        idx = int(idx) if isinstance(idx, (str, float)) else idx
        if isinstance(idx, int) and 0 <= idx < len(self.work_items):
            self.work_edit = self.work_items[idx]


    def update_work_field(self, field: str, value: str):
        self.work_edit[field] = value


    def save_work(self):
        work_doc = self.to_plain(self.work_edit)
        db.work.replace_one({"name": work_doc["name"]}, work_doc, upsert=True)

        raw_work = get_work() or []
        self.work_items.clear()
        self.work_items.extend([
            WorkItem(
                name=item.get("name", ""),
                position=item.get("position", ""),
                startDate=item.get("startDate", ""),
                endDate=item.get("endDate", ""),
                summary=item.get("summary", ""),
                highlights=item.get("highlights") or []
            )
            for item in raw_work
        ])
        self.work_edit = self.work_items[0] if self.work_items else WorkItem(
            name="", position="", startDate="", endDate="", summary="", highlights=[]
        )
