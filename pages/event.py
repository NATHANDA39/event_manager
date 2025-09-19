from nicegui import ui
from components.header import show_header
from components.footer import show_footer
from components.event_card import show_event_card
import requests
from utils.api import base_url


@ui.page("/event")
def show_event_page():
    show_header()
    event_id = ui.context.client.request.query_params.get("id")
    response = requests.get(url=f"{base_url}/events/{event_id}")
    # print(response.status_code, response.content)
    if response.status_code == 200:
        json_data = response.json()
        event = json_data["data"]
        with ui.element("div").classes(
            f"w-full flex flex-row bg-[url({event["image"]})] bg-cover bg-center mb-8"
        ):
            with ui.element("div").classes("w-1/2 text-white px-6 py-10"):
                with ui.link("", "/"):
                    ui.button("Back").props("color=orange-7").classes("mb-8")
                ui.label(text=event["title"]).classes(
                    "font-bold text-5xl mb-8"
                )
                ui.label("IIIT Sonepat").classes("font-bold text-3xl mb-4")
                ui.label(text=event["description"]).classes("text-xs mb-")
                ui.icon("location_on").classes("")

            with ui.element("div").classes("w-1/2 flex items-center justify-center"):
                with ui.card().classes("w-1/2"):
                    ui.label("Date & Time").classes("font-bold mb-4")
                    ui.label("Saturday, March 18 2023, 9:30")
                    ui.link("Add to calender", "/")
                    with ui.column().classes("items-center w-full"):
                        ui.button("Book now").classes("w-full").props("color=orange-7")
                        ui.button("Program promoter").classes("w-full").props(
                            "color=orange-3"
                        )

        with ui.element("div").classes("w-full flex flex-row"):
            with ui.element("div").classes("w-1/2"):
                ui.label("Description").classes("text-xl mb-4 font-bold")
                ui.label(
                    "DesignHub organized a 3D Modeling Workshop using Blender on 16th February at 5 PM. The workshop taught participants the magic of creating stunning 3D models and animations using Blender. It was suitable for both beginners and experienced users. The event was followed by a blender-render competition, which added to the excitement."
                ).classes("text-sm mb-4")
                ui.label(
                    "DesignHub organized a 3D Modeling Workshop using Blender on 16th February at 5 PM. The workshop taught participants the magic of creating stunning 3D models and animations using Blender. It was suitable for both beginners and experienced users. The event was followed by a blender-render competition, which added to the excitement."
                ).classes("text-sm mb-4")

                ui.label("Hours").classes("text-xl mb-4 font-bold")
                with ui.row().classes("text-sm mb-2"):
                    ui.label("Weekdays hour:")
                    ui.label("7PM - 10PM").classes("text-purple-600")
                with ui.row().classes("text-sm mb-4"):
                    ui.label("Sunday hour:")
                    ui.label("7PM - 10PM").classes("text-purple-600")

                ui.label("Organizer Contact").classes("text-xl mb-2 font-bold")
                ui.html(
                    "<p>Please go to <a href='/'> www.drqrack.com </a> and refer the FAQ section for more detail</p>"
                )

            with ui.element("div").classes("w-1/2"):
                ui.label("Event Location").classes("text-xl mb-4 font-bold")
                ui.html(
                    '<iframe src="https://www.google.com/maps/embed?pb=!1m14!1m12!1m3!1d15883.291381306237!2d-0.2713955!3d5.59317755!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!5e0!3m2!1sen!2sgh!4v1757268790959!5m2!1sen!2sgh" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>'
                ).classes("mb-4")
                ui.label("Dream world wide in jakatra").classes("text-xl mb-4")
                ui.label(
                    "Dummy location generation model by RSU. Our approach generates more realistic dummy locations."
                ).classes("text-sm mb-4")
                ui.label("Tags").classes("text-xl mb-4 font-bold")
                with ui.row().classes("text-sm mb-4"):
                    ui.label("Indonesia event").classes("bg-gray-300") 
                    ui.label("Jaskaran event").classes("bg-gray-300")
                    ui.label("Seminar").classes("bg-gray-300")
                    ui.label("Cincinatti event").classes("bg-gray-300")
                ui.label("Share with friends").classes("text-xl mb-4 font-bold")
                with ui.row().classes("text-black text-4xl "):
                    ui.html('<i class="fa-brands fa-facebook"></i>').classes(
                        "hover:text-orange-600 cursor-pointer text-blue-600"
                    )
                    ui.html('<i class="fa-brands fa-instagram"></i>').classes(
                        "hover:text-purple-600 cursor-pointer text-orange-500"
                    )
                    ui.html('<i class="fa-brands fa-linkedin"></i>').classes(
                        "hover:text-orange-600 cursor-pointer text-sky-600"
                    )
                    ui.html('<i class="fa-brands fa-whatsapp"></i>').classes(
                        "hover:text-orange-600 cursor-pointer text-green-500"
                    )
                    ui.html('<i class="fa-brands fa-x-twitter"></i>').classes(
                        "hover:text-orange-600 cursor-pointer"
                    )
        # other event you may like
        with ui.grid(columns=3).classes("w-full px-20 pb-20"):
            response =requests.get(f"{base_url}/events?limit=6")
            # print(response.status_code, response.content)
            json_data = response.json()
            for event in json_data["data"]:
                 show_event_card(event)

    elif response.status_code == 422:
        ui.label(text="Not found")

    show_footer()
