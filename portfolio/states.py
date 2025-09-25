import reflex as rx

from database.db import db
from database.repository import (get_basics,
                                 get_work)


class States(rx.State):
    show_modal: bool = False
    show_code_modal: bool = False

    def toggle_modal(self):
        self.show_modal = not self.show_modal
    
    def toggle_code_modal(self):
        self.show_code_modal = not self.show_code_modal


class AdminState(rx.State):
    selected_collection: str = "basics"

    basics: dict = {}
    basics_edit: dict = {}

    work_items: list[dict] = []
    work_edit: dict = {}


    @staticmethod
    def to_plain(obj):
        if isinstance(obj, dict):
            return {k: AdminState.to_plain(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [AdminState.to_plain(v) for v in obj]
        return obj


    def toggle_admin_modal(self):
        self.show_admin_modal = not self.show_admin_modal
        if self.show_admin_modal:
            self.load_collection(self.selected_collection)


    def load_collection(self, collection: str):
        self.selected_collection = collection
        if collection == "basics":
            self.basics = get_basics()
            self.basics_edit = self.basics.copy() if self.basics else {
                "name": "", "label": "", "email": "", "summary": ""
            }
        elif collection == "work":
            self.work_items = [dict(item) for item in get_work()] if get_work() else []
            self.work_edit = self.work_items[0].copy() if self.work_items else {
                "name": "", "position": "", "startDate": "", "endDate": "",
                "summary": "", "highlights": []
            }


    def update_basics_field(self, field: str, value: str):
        self.basics_edit[field] = value


    def save_basics(self):
        basics_doc = AdminState.to_plain(self.basics_edit)
        db.basics.replace_one({}, basics_doc, upsert=True)
        self.load_collection("basics")

    def select_work_item(self, idx):
        idx = int(idx) if isinstance(idx, (str, float)) else idx

        if isinstance(idx, int) and 0 <= idx < len(self.work_items):
            self.work_edit = dict(self.work_items[idx])


    def update_work_field(self, field: str, value: str):
        self.work_edit[field] = value


    def save_work(self):
        work_doc = AdminState.to_plain(self.work_edit)
        db.work.replace_one({"name": work_doc["name"]}, work_doc, upsert=True)
        self.load_collection("work")

