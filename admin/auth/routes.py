# from curses import flash
# import bcrypt
from google.cloud import storage
from google.cloud import datastore
from api.model.admin.model import Admin
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask import escape, redirect, render_template, request, url_for, flash, session


from flask import escape, redirect, render_template, request, url_for, flash, session

# from flask_login import current_user, login_user
from . import auth
import os
from google.cloud import datastore
from auth.forms import LoginForm
admin_KIND = "ADMIN"
# from flask_login import login_user
# from auth.models import User
# from curses import flash
# import bcrypt

# from flask_login import current_user, login_user
# login_manager = LoginManager(auth)
# login_manager.login_view = 'auth.login'
# login_manager.init_auth(auth)


# @login_manager.user.loader
# def load_user(id):
#     return Admin.query.get(int(id))

# from flask_login import login_user
# from auth.models import User


@auth.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()

    client = datastore.Client()
    query = client.query(kind=admin_KIND)
    hasil = query.fetch()
    hasil_baru = []
    for data in hasil:
        hasil_baru.append({
            "id": data.id,
            "email": data['email'],
            "password": data['password'],
        })
    if form.validate_on_submit():
        admin = Admin.query.filter_by(email=form.email.data).first()
        if check_password_hash(admin.password, form.password.data):
            login_user(admin)

            return redirect(url_for('index'))
        return redirect(url_for('index'))
    return render_template('auth/login.html', form=form)
