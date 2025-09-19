from nicegui import ui
from components.header import show_header
from components.footer import show_footer
from components.event_card import show_event_card
import requests
from utils.api import base_url

@ui.page("/")
def show_home_page():
    ui.query(".nicegui-content").classes("p-0 m-0 gap-0")
    
    show_header()

    with ui.element("main").classes("w-full h-screen p-0 m-0"):
        with ui.element("div").style(
            "background-image:url('/assets/HP_1.png'); background-size: cover; background-position: center; background-color: #000000;"
        ).classes("flex flex-col bg-cover bg-center w-full h-full justify-center items-center pb-20"):

            with ui.column().classes("text-white items-center mb-10"):
                ui.label("MADE FOR THOSE").classes("text-7xl font-bold")
                ui.label("WHO DO").classes("text-6xl font-bold")

# Search bar
    with ui.row().classes(
    " bg-[#10107B] rounded-xl shadow-lg p-4 w-11/12 md:w-3/4 mx-auto -mt-10 "
    "justify-around space-x-4 z-20 animate-fadeInUp"):
    # Event type select
        ui.select(
        ["select event type", "Conference", "Workshop", "Concert"],
        value="select event type",
        with_input=True).props("outlined dense").classes("w-1/4 bg-white rounded-lg text-gray-700")

    # Location select
        ui.select(
        ["select event location", "Accra", "London", "New York"],
        value="select event location",
        with_input=True).props("outlined dense").classes("w-1/4 bg-white rounded-lg text-gray-700")

    # Date/time select
        ui.input(
        label="choose date and time").props("outlined dense").classes("w-1/4 bg-white rounded-lg text-gray-700")

        # Search button 
        ui.button(icon="search").props("flat dense no-caps").classes("bg-deep-purple-600 text-white rounded-sm p-3 hover:bg-indigo-700 hover:scale-105 transition-all shadow-lg")

# Upcoming events 
    with ui.element('section').classes("flex flex-row justify-between items-center w-full mt-16 pt-16 mb-16 px-20 py-4"): #Push section content down	pt-XX | Push whole section down	mt-XX

        # Left Title
        with ui.row().classes("items-baseline px-20 gap-0 space-x-2 mb-16"):
            ui.label("Upcoming").classes("text-2xl font-bold")
            ui.label("Events").classes("text-2xl text-purple-600 font-bold")

        # Right Filter Container
        with ui.row().classes("space-x-2 px-20 mb-16"):
            weekdays = ['Weekdays', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
            ui.select(label='', options=weekdays, value='Weekdays').props('dense outlined')
            Event_page = ['Event type', 'Workshop', 'Webinar', 'Meetup']
            ui.select(label='',options=Event_page, value="Event type" ).props('dense outlined')
            Any_category = ['Any category', 'Tech', 'Health', 'Business']
            ui.select(label='', options=Any_category, value="Any category").props('dense outlined')
        
        # Grid_1 - pb-10 = padding-bottom or  mb-10 = margin-bottom provide a space underneath the grid 
        # with ui.grid(columns=3).classes("w-full px-20 pb-20"):
        with ui.grid(columns=3).classes("w-full px-20 pb-20"):
            response =requests.get(f"{base_url}/events?limit=6")
            # print(response.status_code, response.content)
            json_data = response.json()
            for event in json_data["data"]:
                 show_event_card(event)

            # for i in range(6):
            #     with ui.card().classes("mb-4"):
            #         ui.image("/assets/X1.jpeg")
            #         ui.label("Best Seller Bootcamp-Write, Market and Publish your Book-Lucknow")
            #         ui.label("Saturday, March 10, 6:30pm").classes("text-purple-600")
            #         ui.label("ONLINE EVENT - ATTEND anywhere").classes("text-gray-500")

        with ui.element("div").classes("w-full flex items-center justify-center py-10"):
            ui.button("Load More...", on_click=lambda: ui.navigate.to('/loadmore')).props("flat dense no-caps").classes("bg-purple-600 text-white shadow hover:bg-purple-500 px-4 py-2 rounded")
            
        # ui.separator().classes("h-10 bg-white")


# Create events
    with ui.element("section").classes("relative w-full h-[303px] mt-[100px]"):
                # Navy blue background
                with ui.element("div").classes("absolute w-full h-[252px] left-0 top-[51px] bg-[#10107B]"):
                    pass
                # Left image
                with ui.element("div").classes("absolute w-[544.67px] h-[303px] left-[100px] top-0"):
                    ui.image("assets/HP_2.png").classes("w-full h-full object-cover rounded-[10px]")
                # Right content
                with ui.element("div").classes("absolute w-[417px] h-[182px] left-[696px] top-[86px]"):
                    ui.label("Make your own Event").classes("text-[36px] font-bold leading-[42px] text-[#F8F8FA]")
                    ui.label("Empower your campus—host, manage, and share unforgettable events with ease.").classes("mt-4 text-[18px] leading-[21px] text-[#F8F8FA]")
                # CTA Button
                with ui.element("div").classes("absolute w-[302px] h-[60px] left-[696px] top-[208px]"):
                    ui.button("Create Events").props("flat dense no-caps").classes(
                        "bg-purple-600 text-white shadow hover:bg-purple-500 px-4 py-2 rounded")
                    

# Brands Section (Figma spec, flex layout, no overlap)
    with ui.element("section").classes("relative w-full max-w-[1200px] mx-auto py-[60px] mt-[30px]"):
                ui.label("Join these brands").classes("block text-[36px] font-bold leading-[42px] text-center text-[#131315] mb-2")
                ui.label("We've had the pleasure of working with industry-defining brands. These are just some of them.").classes("block text-[18px] font-bold leading-[21px] text-center text-[#131315] mb-3")
                # Logo grid (flex, Figma sizes)
                brand_logos = [
                    ("assets/spotify.png", "w-[179px] h-[50px]"),
                    ("assets/google.png", "w-[162px] h-[49px]"),
                    ("assets/stripe.png", "w-[141px] h-[63px]"),
                    ("assets/YouTube.png", "w-[226px] h-[131px]"),
                    ("assets/Microsoft.png", "w-[182px] h-[39px]"),
                    ("assets/Medium.png", "w-[297px] h-[124px]"),
                    ("assets/Zoom.png", "w-[295px] h-[83px]"),
                    ("assets/Uber.png", "w-[134px] h-[44px]"),
                    ("assets/Grab.png", "w-[145px] h-[52px]")
                ]
                with ui.row().classes("flex flex-wrap justify-between items-center gap-y-8 gap-x-8 mb-8"):
                    for logo, size in brand_logos:
                        ui.image(logo).classes(f"object-contain bg-transparent rounded-md {size}")

# Cards trending Colleges
# Grid_2 
    with ui.element('section').classes("flex flex-row justify-between items-center w-full mt-16 pt-16 mb-16 px-20 py-4"):  
        # Left Title
        with ui.row().classes("items-baseline px-20 gap-0 space-x-2 mb-5"):
                ui.label("Trending").classes("text-2xl font-bold")
                ui.label("Colleges").classes("text-2xl text-purple-600 font-bold")
                
        with ui.grid(columns=3).classes("w-full px-20 pb-2"): # pb-10 = padding-bottom or  mb-10 = margin-bottom provide a space underneath the grid 

            for i in range(3):
                with ui.card().classes("mb-2"):
                    ui.image("/assets/X1.jpeg")
                    ui.label("Standford University")
                    ui.label("Standard califonia").classes("text-black")
    with ui.element("div").classes("w-full flex items-center justify-center py-2"):
                ui.button("Load More...", on_click=lambda: ui.navigate.to('/loadmore')).props("flat dense no-caps").classes("bg-purple-600 text-white shadow hover:bg-purple-500 px-4 py-2 rounded mb-5")
    
# Grid_3 
    with ui.element('section').classes("flex flex-row justify-between items-center w-full mt-16 pt-16 mb-16 px-20 py-4"):  
    # Left Title
        with ui.row().classes("items-baseline px-20 gap-0 space-x-2 mb-5"):
            ui.label("Our").classes("text-2xl font-bold")
            ui.label("Blogs").classes("text-2xl text-purple-600 font-bold")
        with ui.grid(columns=3).classes("w-full px-20 pb-2"): # pb-10 = padding-bottom or  mb-10 = margin-bottom provide a space underneath the grid 

            for i in range(3):
                with ui.card().classes("mb-2"):
                    ui.image("/assets/X1.jpeg")
                    ui.label("Best Seller Bootcamp-Write, Market and Publish your Book-Lucknow")
                    ui.label("Saturday, March 10, 6:30pm").classes("text-purple-600")
                    ui.label("ONLINE EVENT - ATTEND anywhere").classes("text-gray-500")

    with ui.element("div").classes("w-full flex items-center justify-center py-5"):
                ui.button("Load More...", on_click=lambda: ui.navigate.to('/loadmore')).props("flat dense no-caps").classes("bg-purple-600 text-white shadow hover:bg-purple-500 px-4 py-2 rounded mb-5")

    show_footer()