from flask import render_template
from . import materi


@materi.route('/materi')
def mainMateri():
    return render_template('materi/basic-table.html')

