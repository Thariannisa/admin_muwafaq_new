# from curses import flash
# import bcrypt
import re
from google.cloud import storage
from google.cloud import datastore
from api.model import admin

from api.model.admin.model import Admin


from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask import escape, redirect, render_template, request, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash

from flask import escape, redirect, render_template, request, url_for, flash, session

# from flask_login import current_user, login_user
from . import auth
import os
from google.cloud import datastore
from auth.forms import LoginForm

admin_KIND = "ADMIN"


@auth.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if(request.method == 'POST'):
        session.pop("user", None)
        if request.form['password'] != None and request.form['email'] != None:
            hasil = admin.LoginAdmin(
                request.form['email'], request.form['password'])
            if hasil:
                suksesLogin = check_password_hash(
                    hasil['password'], request.form['password'])
                if suksesLogin:
                    session["user"] = request.form['email']
                    # return render_template('index.html')
                    return "berhasil"
                    # return redirect(url_for('index'))
        return "gagal"
        # return suksesLogin
        # return render_template('auth/login.html', form=form, error="email atau password salah")
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
def logout():
    session.pop("user", None)
    return render_template('auth/login.html')
