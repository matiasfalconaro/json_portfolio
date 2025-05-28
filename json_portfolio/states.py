import reflex as rx


class States(rx.State):
    show_modal: bool = False
    show_code_modal: bool = False

    def toggle_modal(self):
        self.show_modal = not self.show_modal
    
    def toggle_code_modal(self):
        self.show_code_modal = not self.show_code_modal