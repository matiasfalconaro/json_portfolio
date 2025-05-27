import reflex as rx


class ContactState(rx.State):
    show_modal: bool = False

    def toggle_modal(self):
        self.show_modal = not self.show_modal