from nicegui import ui


def show_event_card(event):
    with ui.card().on(
        type="click", handler=lambda: ui.navigate.to(f"/event?id={event["id"]}")
    ).classes("cursor-pointer"):
        ui.image(source=event["image"]).classes("h-48 w-full object-cover")
        ui.label(text=event["title"])
        ui.label(text=event["start_date"]).classes("text-purple-600")
        ui.label(text=event["venue"]).classes("text-gray-500")
