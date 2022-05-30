
from flask import Flask
from .directories import TEMPLATE_DIR, STATIC_DIR

from auth.routes import auth
from modul.routes import modul
from materi.routes import materi
from tilawah.routes import tilawah
from mawaris.routes import mawaris
from fiqh.routes import fiqh
from tajwid.routes import tajwid
from diskusi.routes import diskusi
from latihan.routes import latihan
from api.routes import api
from api.views import users
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
app.register_blueprint(materi, url_prefix='/materi')
app.register_blueprint(tilawah, url_prefix='/tilawah')
app.register_blueprint(mawaris, url_prefix='/mawaris')
app.register_blueprint(fiqh, url_prefix='/fiqh')
app.register_blueprint(tajwid, url_prefix='/tajwid')
app.register_blueprint(diskusi, url_prefix='/diskusi')
app.register_blueprint(api, url_prefix='/api')
app.register_blueprint(users)
app.register_blueprint(users2)

# unique secret key for to different app
# app.config['SECRET_KEY'] = os.getenv('SECRET_API')
# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db"
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba288'
app.config['WTF_CSRF_SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba288'
user = {"username": "bismillahtes", "password": "muwafaqtes"}
# set db
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)

# # # set hash
# bcrypt = Bcrypt(app)

# # set auth
# login_manager = LoginManager(app)
# login_manager.login_view = 'auth.login'
# login_manager.init_app(app)


# # set mail
# app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
# app.config['MAIL_PORT'] = 587
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
# app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
# mail = Mail(app)


# def create_app(config_class=Config):
#     app = Flask(__name__)
#     app.config.from_object(Config)
