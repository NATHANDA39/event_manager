from nicegui import ui
from components.header import show_header
from components.footer import show_footer

@ui.page("/not-found")
def show_not_found_page():
    show_header()
    ui.label("This page is not found")
    show_footer()
    