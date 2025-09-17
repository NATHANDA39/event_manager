from nicegui import ui
from components.header import show_header
from components.footer import show_footer   

@ui.page("/create_event")
def show_create_event_page():
    ui.query('.nicegui-content').classes('m-0 p-0 gap-0')
    ui.query('.q-uploader__header').classes('bg-purple-600')
    show_header()

#  main container
    with ui.element("div").classes("w-full h-screen flex flex-col justify-center items-center"):
        ui.label("Create Event").classes("text-2xl font-bold p-4")
        with ui.card().classes("w-[40%] font-bold text-lg"):
            ui.label("Event Title")
            ui.input(placeholder="Enter your mail").classes('w-full').props("outlined")
            ui.label("Event Venue")
            ui.input(placeholder="Enter the venue").classes('w-full').props("outlined")
            with ui.row().classes("flex flex-row justify-around w-full"):
                ui.input(label="start time").props("type=time outlined")
                ui.input(label="End Time").props("type=time outlined")
            with ui.row().classes("flex flex-row justify-around w-full"):
                ui.input(label="start Date").props("type=date outlined")
                ui.input(label="start Date").props("type=date outlined")  

    with ui.element("div").classes("w-full h-screen flex flex-col justify-center items-center"):
        ui.label("Event Description").classes("text-2xl font-bold p-4")
        with ui.card().classes("w-[40%] font-bold text-lg p-8 mb-8"):
            ui.label("Event Image")
            ui.upload(auto_upload=True, on_multi_upload=True).classes("w-full") 
            ui.label("Event Description")
            ui.input(placeholder="Type here...").classes("w-full")     

    show_footer()