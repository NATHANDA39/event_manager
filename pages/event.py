from nicegui import ui
from components.header import show_header
from components.footer import show_footer

@ui.page("/event")
def show_event_page():
    show_header()
    ui.label("This is the event page")
    show_footer()