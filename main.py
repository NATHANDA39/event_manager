from nicegui import ui, app
from pages.home import *
from pages.signin import *
from pages.signup import *
from pages.event import *
from pages.college import *
from pages.create_event import *
from pages.not_found import *

app.add_static_files("/assets", "assets")




ui.run() # By using ui.run(on_air=True) you can share your local app with others over the internet 