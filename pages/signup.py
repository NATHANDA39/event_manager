from nicegui import ui

BG_IMAGE_URL = "https://cdn.pixabay.com/photo/2012/11/22/07/54/sunrise-66954_640.jpg"

@ui.page("/signup")
def show_signup_page():
    ui.query(".nicegui-content").classes("p-0 m-0 gap-0")

    def handle_sign_up(name, email, password, confirm):
        ui.notify(f'Account created for {name}!')

    with ui.row().classes('w-full h-screen font-sans'):

        # LEFT: Image with overlay text
        with ui.element('div').classes('flex-1 min-w-0 h-full relative overflow-hidden'):
            ui.image(BG_IMAGE_URL).classes('w-full h-full object-cover rounded-none').style('filter: brightness(70%);')
            with ui.column().classes('absolute inset-0 z-10 items-center justify-center text-center text-white p-8'):
                ui.label('Welcome back').classes('text-4xl font-bold drop-shadow-lg')
                ui.label('To keep connected with us provide us with your information ').classes('mt-4 text-lg font-light max-w-md drop-shadow')

                with ui.link("", "/signin").classes("no-underline"):
                    with ui.button(text=None).classes('relative px-4 flex items-center justify-center bg-transparent border-none'):
                        # The blurred overlay
                        ui.element('div').classes('absolute inset-0 backdrop-blur-sm bg-white/30')    
                        # The text label (must be a separate element to avoid being blurred)
                        ui.label('Sign in').props("flat dense no-caps").classes('relative z-10 text-white font-semibold text-sm')

        # RIGHT: Sign up form
        with ui.element('div').classes('flex-1 min-w-0 h-full flex flex-col items-center p-0 bg-white'):
            with ui.row().classes('items-center gap-0 space-x-2 mt-10'):
                ui.label('Event').classes('text-2xl font-bold text-gray-800 mb-8')
                ui.label('Hive').classes('text-2xl font-bold text-purple-600 mb-8')
            
            ui.label('Sign Up to Event Hive').classes('text-3xl font-bold text-gray-800 mb-2')

            with ui.element('div').classes('w-full max-w-md flex flex-col justify-center items-center mt-10 gap-6'):
                name_input = ui.input(placeholder='Full Name').props('outlined dense').classes('w-full')
                email_input = ui.input(placeholder='Email').props('outlined dense').classes('w-full')
                password_input = ui.input(placeholder='Password', password=True, password_toggle_button=True).props('outlined dense').classes('w-full')
                confirm_input = ui.input(placeholder='Confirm Password', password=True, password_toggle_button=True).props('outlined dense').classes('w-full')

                with ui.row().classes('w-full justify-center'):
                    ui.button(
                        'Sign Up',
                        on_click=lambda: handle_sign_up(
                            name_input.value, email_input.value, password_input.value, confirm_input.value
                        )
                    ).props("flat dense no-caps").classes(
                        'w-full max-w-xs py-3 rounded-lg font-semibold bg-purple-600 text-white transition-colors mb-4'
                    )

                ui.link('Already have an account? Sign In', '/signin').classes('text-gray-600 underline text-lg mt-2')
                ui.button(
                    'Go Back Home',
                    on_click=lambda: ui.navigate.to('/')
                ).props("flat dense no-caps").classes(
                    'bg-purple-600 text-white shadow hover:bg-purple-500 w-full max-w-xs px-4 py-3 rounded-lg'
                )

