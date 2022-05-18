from flask import Blueprint
from root.directories import TEMPLATE_DIR, APP_DIRS
from flask import Flask
# Blueprint untuk utama
from .views import permintaan
from .views import users
from .views import users2


__app_name = 'api'

api = Blueprint(__app_name, __name__,
                template_folder=TEMPLATE_DIR / APP_DIRS[__app_name])

app = Flask(__name__, template_folder="templates",
            instance_relative_config=True)

app.register_blueprint(permintaan)

# app register disini brarti hapus aja, pake app register di init paling luar aja satu
# app.register_blueprint(users)
# app.register_blueprint(users2)
