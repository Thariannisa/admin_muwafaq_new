from flask import Blueprint
from root.directories import TEMPLATE_DIR, APP_DIRS

__app_name = 'tajwid'

tajwid = Blueprint(__app_name, __name__,
                template_folder=TEMPLATE_DIR / APP_DIRS[__app_name])
