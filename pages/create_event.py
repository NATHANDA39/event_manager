from nicegui import ui
from components.header import show_header
from components.footer import show_footer  
import requests
from utils.api import base_url 

event_image = None

def _handle_image_upload(event): 
    global _event_image
    _event_image = event.content

# function to create a post event 
def _post_event(data, files):
    response = requests.post(f"{base_url}/events", data=data, files=files)
    if response.status_code == 200:
        ui.notify(message="Event added successfully!", 
        type="positive")

        return ui.navigate.to ("/")
    elif response.status_code == 422:
        return ui.notify(
            message="Please ensure all inputs are filled!",
            type="negative"
        )
    json_data = response.json()
    

@ui.page("/create_event")
def show_create_event_page():
    ui.query('.nicegui-content').classes('m-0 p-0 gap-0')
    # ui.query('.q-uploader__header').classes('bg-purple-600')
    show_header()

#  main container
    with ui.element("div").classes("w-full h-screen flex flex-col justify-center items-center"):
        ui.label("Create Event").classes("text-2xl font-bold p-4")
        with ui.card().classes("w-[40%] font-bold text-lg"):
            ui.label("Event Title")
            event_title = ui.input(placeholder="Enter your title").classes('w-full').props("outlined")
            event_venue=ui.label("Event Venue")
            ui.input(placeholder="Enter the venue").classes('w-full').props("outlined")
            
            #Start and End Time section with time inputs
            with ui.row().classes("flex flex-row justify-between w-full gap-4"):
                event_start_time = ui.input(label="start time").props("type=time outlined").classes("flex-1")
                event_end_time = ui.input(label="End Time").props("type=time outlined").classes("flex-1")

            # Start and End date section with date inputs
            with ui.row().classes("flex flex-row justify-between w-full gap-4"):
                event_start_date = ui.input(label="start Date").props("type=date outlined").classes("flex-1")
                event_end_date = ui.input(label="End Date").props("type=date outlined").classes("flex-1")
            
            # Event Description and File upload 
    with ui.element("div").classes("w-full flex flex-col justify-center items-center"):
        ui.label("Event Description").classes("text-2xl font-bold p-4")
        with ui.card().classes("w-[40%] font-bold text-lg p-8 mb-8"):
            ui.label("Event Image")
            ui.upload(auto_upload=True, on_upload=True).props("outlined color=purple-600").classes("w-full")
            ui.label("Event Description").classes("w-full")
            event_description =  ui.textarea(placeholder="Type here...").props("outlined").classes("w-full") 

            with ui.element("div").classes("w-full flex justify-center items-center"):
                ui.button("Create Event", on_click=lambda: _post_event(
            data={
                "title": event_title.value,
                "venue": event_venue.value,
                "start_time": event_start_time.value,
                "end_time": event_end_time.value,
                "start_date": event_start_date.value,
                "end_date": event_end_date.value,
                "description": event_description.value
            },
            files={
                "image": _event_image
            }
        )).props("flat dense no-caps").classes("w-[30%]  bg-purple-600 p-2 text-white text-sm rounded-lg")

    show_footer()
    