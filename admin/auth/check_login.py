from werkzeug.utils import redirect
from flask.helpers import url_for
from flask import jsonify, request_finished, g, session
from functools import wraps


def check_login(f):
    wraps(f)

    def decorated(*args, kwargs):

        if 'user' in session:
            return f(session['user'], *args, **kwargs)
        else:
            return redirect(url_for('login'))
    return decorated
