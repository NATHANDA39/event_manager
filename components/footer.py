from nicegui import ui

    # Load FontAwesome for social icons
ui.add_head_html(
        '<script src="https://kit.fontawesome.com/ccba89e5d4.js" crossorigin="anonymous"></script>'
    )


def show_footer():
    with ui.element("footer").style("background-color: navy;").classes("w-full h-[250px]"):
        with ui.element("div").classes("flex flex-col items-center"):
            with ui.element("div").classes("flex flex-row font-bold text-lg mt-4 mb-3"):
                ui.label("Event").classes("mr-2").classes("text-white")
                ui.label("Hive").classes("text-purple-600")
            with ui.element("div").classes("flex flex-row mb-8"):
                ui.input(placeholder="Enter your maill").props("borderless dense flat").classes("rounded-sm text-xs mr-2 w-[240px] bg-white placeholder:text-right h-[40px] px-2")
                ui.button(text="Subscribe").props("flat dense no-caps").classes("bg-purple-600 extended font-normal text-white w-[120px]")
             # navlinks
            navlinks = [
                    {"title":"Home","path":"/"},
                    {"title":"About","path":"/"},
                    {"title":"Services","path":"/"},
                    {"title":"Get in touch","path":"/"},
                    {"title":"FAQs","path":"/"}
                ]
            with ui.row().classes("gap-[31px] mb-8"):
                 for item in navlinks:
                     ui.link(item["title"], item["path"]).classes("no-underline text-white")
        
        ui.element("div").classes("bg-white w-[1240px] h-[0.2px] mx-auto mb-3")

        with ui.element("div").classes('w-full justify-start flex flex-row justify-between items-center px-40'):
            with ui.element("div").classes("space-x-4"):
                    ui.button("English").props("flat dense no-caps").classes("text-white bg-purple-600 shadow-none px-4 py-2 rounded-sm")
                    ui.link("French").classes('text-white no-underline')
                    ui.link("Hindi").classes("!text-white no-underline")

            # # Socials (icons)
            # with ui.row().classes("space-x-4 text-xl text-center text-white"):  # Added spacing and text size
            #     ui.html('<i class="fa-brands fa-facebook-f"></i>')
            #     ui.html('<i class="fa-brands fa-instagram"></i>')
            #     ui.html('<i class="fa-brands fa-x-twitter"></i>')
                    
            # ui.label("Non Copyrighted © 2023 Upload by EventHive").classes("text-white justify-end px-30")

          
            # Center: Social icons
            with ui.row().classes("gap-4 justify-center text-xl"):
                ui.html('<i class="fa-brands fa-facebook"></i>')
                ui.html('<i class="fa-brands fa-instagram"></i>')
                ui.html('<i class="fa-brands fa-twitter"></i>')
                ui.html('<i class="fa-brands fa-linkedin"></i>')

            # Right: Copyright
            ui.label("Non Copyrighted © 2025 Upload by EventHive").classes(
                "text-[12px] text-white" 
            )

