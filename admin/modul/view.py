from flask import Blueprint, jsonify, render_template, request, escape
import json
from .model import modul as ma

modul = Blueprint("modul", __name__, url_prefix="/modul")


@modul.route('/modul')
def mainModul():
    return render_template('modul/index_modul.html')


@modul.route('/tambah_modul', methods=["POST"])
def tambah():
    if request.is_json:
        data = request.get_json()
    else:
        return "Parameter salah", 415

    # Periksa parameter sudah benar
    if data is None:
        return "Parameter salah", 400
    if "idKelas" not in data.keys():
        return "Parameter salah", 400

    hasil = ma.tambah(
        data['judul'],
        data['gambarDefault'],
        data['PdfUrl']
    )

    # Pastikan berhasil
    if (hasil is None):
        return "Gagal menambah data!", 500

    return "Berhasi", 200


@modul.route('/daftar', methods=["GET"])
def daftar():
    daftara = ma.daftar()

    def obj_dict(obj):
        return obj.__dict__

    hasil = json.dumps(daftara, default=obj_dict)
    # Muat template
    return {"daftar": json.loads(hasil)}, 200


@modul.route('/daftar/<int:id>', methods=["GET"])
def getId(id):
    daftara = ma.getId(id)

    if daftara != None:
        return json.loads(json.dumps(daftara.__dict__)), 200
    else:
        return {"error": "not found data"}, 200


@modul.route('/update/<int:id>', methods=["PUT"])
def update(id):

    data = request.get_json()

    data = ma.update(
        id,
        data['judul'],
        data['gambarDefault'],
        data['PdfUrl'],
    )

    return data, 200


@modul.route('/delete/<int:id>', methods=["DELETE"])
def delete(id):

    data = ma.delete(id)

    return data, 200
