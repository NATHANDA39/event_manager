from nicegui import ui

def show_header():
    with ui.element("div").classes("flex justify-between items center w-full px-10 py-5"):
        with ui.element("div").classes("flex items-center space-x-2"):
            ui.label("Event").classes("text-2xl font-bold text-black")
            ui.label("Hive").classes("text-2xl font-bold text-purple-600")
# ui.label("Welcome to the home page")
        with ui.row():
                ui.link("Signup", "/signup")
                ui.link("Signin", "/signin")
                ui.link("event", "/event")
                ui.link("college", "/college")
                ui.link("create_event", "/create_event")
                ui.link("not_found", "/not_found")
                
        with ui.element("div").classes("flex items-center"):
            ui.button("Login", on_click=lambda: ui.navigate.to('/signin')).props("flat dense no-caps").classes("text-black bg-hover:bg-purple shadow-none px-4 py-2")
            ui.button("Signup", on_click=lambda: ui.navigate.to('/signup')).props("flat dense no-caps").classes("bg-purple-600 text-white bg-hover:bg-purple shadow-none px-4 py-2")