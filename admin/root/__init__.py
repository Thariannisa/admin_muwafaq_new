
from flask import Flask
from .directories import TEMPLATE_DIR, STATIC_DIR

from auth.routes import auth
from modul.routes import modul
from tilawah.routes import tilawah
from mawaris.routes import mawaris
from fiqh.routes import fiqh
from tajwid.routes import tajwid
from fathurahman.routes import fathurahman
from umum.routes import umum
from diskusi.routes import diskusi
from latihan.routes import latihan
from api.routes import api
from api.views import users2
import os
from flask_ckeditor import CKEditor
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
# from .config import Config
# from flask_sqlalchemy import SQLAlchemy
# from flask_bcrypt import Bcrypt
# from flask_login import LoginManager
# from flask_mail import Mail
# from flask_migrate import Migrate

# init app
app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)
ckeditor = CKEditor(app)

# register app

app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(modul, url_prefix='/modul')
app.register_blueprint(latihan, url_prefix='/latihan')
app.register_blueprint(tilawah, url_prefix='/tilawah')
app.register_blueprint(mawaris, url_prefix='/mawaris')
app.register_blueprint(fiqh, url_prefix='/fiqh')
app.register_blueprint(tajwid, url_prefix='/tajwid')
app.register_blueprint(fathurahman, url_prefix='/fathurahman')
app.register_blueprint(umum, url_prefix='/umum')
app.register_blueprint(diskusi, url_prefix='/diskusi')
app.register_blueprint(api, url_prefix='/api')
app.register_blueprint(users2)

# unique secret key for to different app
# app.config['SECRET_KEY'] = os.getenv('SECRET_API')
# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db"
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba288'
app.config['WTF_CSRF_SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba288'
