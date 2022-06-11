from api.model.admin.check_login import check_login
from flask import render_template
from root import app


@app.route('/')
@check_login
def index(dataindex):
    return render_template('index.html', title="beranda")
