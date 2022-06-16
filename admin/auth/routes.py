# from curses import flash
# import bcrypt
import re
from google.cloud import storage
from google.cloud import datastore
from api.model import admin
from api.model.admin.model import Admin
from flask import escape, redirect, render_template, request, url_for, flash, session, Flask, session, abort
from werkzeug.security import generate_password_hash, check_password_hash
from flask import escape, redirect, render_template, request, url_for, flash, session
from api.model.admin.model import admin_KIND
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
from pip._vendor import cachecontrol
import google.auth.transport.requests
# from flask_login import current_user, login_user
# from google_auth_oauthlib.flow import Flow
from . import auth
import os
import pathlib
import requests
from google.cloud import datastore
from auth.forms import LoginForm
# GOOGLE_CLIENT_ID = "908376936693-j3g8s0pgq0ihtid7b8806ksmlt6ac95h.apps.googleusercontent.com"
# flow = Flow.from_client_secret_file
admin2_KIND = "ADMIN3"

app = Flask("Google Login App")
app.secret_key = "5791628bb0b13ce0c676dfde280ba288"

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:\gcloud_key\key_rio\key.json"


GOOGLE_CLIENT_ID = "417093792904-uf0v2s77ikv9m8fr0ak447avhotesdka.apps.googleusercontent.com"
client_secrets_file = os.path.join(
    pathlib.Path(__file__).parent, "C:\gcloud_key\key_rio\client_secret_key_login.json")

flow = Flow.from_client_secrets_file(
    client_secrets_file=client_secrets_file,
    scopes=["https://www.googleapis.com/auth/userinfo.profile",
            "https://www.googleapis.com/auth/userinfo.email", "openid"],
    redirect_uri="http://127.0.0.1:5000/auth/login_google"
)


def login_is_required(function):
    def wrapper(*args, **kwargs):
        if "google_id" not in session:
            return abort(401)  # Authorization required
        else:
            return function()

    return wrapper


@auth.route("/google")
def googlelogin():
    authorization_url, state = flow.authorization_url()
    session["state"] = state
    return redirect(authorization_url)


@auth.route("/login_google")
def callback():
    flow.fetch_token(authorization_response=request.url)

    if not session["state"] == request.args["state"]:
        abort(500)  # State does not match!

    credentials = flow.credentials
    request_session = requests.session()
    cached_session = cachecontrol.CacheControl(request_session)
    token_request = google.auth.transport.requests.Request(
        session=cached_session)

    id_info = id_token.verify_oauth2_token(
        id_token=credentials._id_token,
        request=token_request,
        audience=GOOGLE_CLIENT_ID
    )

    email = id_info.get("email")

    if LoginGoogleAdmin(email):
        session["google_id"] = id_info.get("sub")
        session["name"] = id_info.get("name")
        session["email"] = id_info.get("email")
        return redirect("/")
    else:
        session.clear()
        return redirect("/")
    


@auth.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if(request.method == 'POST'):
        session.pop("user", None)
        if request.form['password'] != None and request.form['email'] != None:
            hasil = LoginAdmin(
                request.form['email'], request.form['password'])
            if hasil:
                suksesLogin = check_password_hash(
                    hasil['password'], request.form['password'])
                print(suksesLogin)
                if suksesLogin:
                    session["user"] = request.form['email']
                    return redirect(url_for('index'))
                    # return "berhasil"
        # return "gagal"
        # return redirect(url_for('index'))
        # return "tes"
        # return suksesLogin
        return render_template('auth/login.html', form=form, error="email atau password salah")

    return render_template('auth/login.html', form=form)


@auth.route("/logout")
def logout():
    session.clear()
    return redirect("/")


def LoginAdmin(
    email,
    password,
):
    if email != None and password != None:

        client = datastore.Client()
        queri = client.query(kind=admin2_KIND)
        queri.add_filter("email", "=", email)

        satuHasil = list(queri.fetch(limit=1))
        if satuHasil:
            data = satuHasil[0]
            return data
        return None

def LoginGoogleAdmin(
    email
):
    if email != None:

        client = datastore.Client()
        query = client.query(kind=admin_KIND)
        hasil = query.fetch()
        hasil_baru = []

        for data in hasil:
            if email == data['email']:
                return True
            else:
                return False
        return None


@auth.route('/generate_pass')
def create_user():
    create_pass = generate_password_hash('BismillahMuwafaqAceh10',
                                         method='pbkdf2:sha256', salt_length=26)
    return create_pass


# method tambah admin
@auth.route('/list_admin', methods=['GET'])
def listAdmin():
    client = datastore.Client()
    query = client.query(kind=admin_KIND)
    hasil = query.fetch()
    hasil_baru = []
    for data in hasil:
        hasil_baru.append({
            "idAdmin": data.id,
            "nama": data['nama'],
            "email": data['email'],
        })
    return render_template('auth/list_Admin.html',  data=hasil_baru, title="Admin")


@auth.route('/tambah_admin')
def addAdmin():
    form = LoginForm()
    return render_template('auth/add_dataAdmin.html', form=form, title="tambah admin")


@auth.route('/daftar_admin', methods=['POST'])
def daftarAdmin():
    Email = request.form['email']
    Nama = request.form['nama']

    hasil = {}

    hasil["email"] = Email
    hasil["nama"] = Nama

    client = datastore.Client()
    # Minta dibuatkan Key/Id baru untuk object baru
    key_baru = client.key(admin_KIND)
    # Minta dibuatkan entity di datastore memakai key baru
    entity_baru = datastore.Entity(key=key_baru)
    # Simpan object Permintaan ke entity baru
    entity_baru.update(hasil)
    # Simpan entity ke datastore
    client.put(entity_baru)
    # return render_template('modul/index_modul.html')
    # return hasil
    return redirect('/auth/list_admin')


@auth.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    # Buat object hanya jika kedua data ada
    if id != None:
        # Sambung ke datastore
        client = datastore.Client()
        entity = client.get(client.key(admin_KIND, id))
        if entity != None:
            client.delete(entity)
            return redirect('/auth/list_admin')
    else:
        return "gagal"


if __name__ == "__main__":
    app.run(debug=True)
