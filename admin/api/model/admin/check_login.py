from werkzeug.utils import redirect
from flask.helpers import url_for
from flask import jsonify, request_finished, g, session
from functools import wraps

def check_login(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if "user" in session:
            return f(session['user'], *args, **kwargs)
        elif "google_id" not in session:
            return redirect("/auth/login")  # Authorization required
        else:
            return f(session['google_id'], *args, **kwargs)

    return wrapper