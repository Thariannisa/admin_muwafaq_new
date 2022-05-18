from flask import Blueprint, jsonify, request, escape
import json
from api.model import users as us


users = Blueprint("users", __name__, url_prefix="/api/users")


@users.route('/daftar', methods=["GET"])
def daftar():
    daftara = us.daftar()

    def obj_dict(obj):
        return obj.__dict__

    hasil = json.dumps(daftara, default=obj_dict)
    # Muat template
    return {"daftar": json.loads(hasil)}, 200


@users.route("/tambah_data", methods=["POST"])
def tambah():
    # Pastikan parameter dalam JSON
    if request.is_json:
        # Ambil parameter
        permintaan_baru = request.get_json()
    else:
        return "Parameter salah", 415

    # Periksa parameter sudah benar
    if permintaan_baru is None:
        return "Parameter salah", 400
    if "nama" not in permintaan_baru.keys():
        return "Parameter salah", 400
    if "email" not in permintaan_baru.keys():
        return "Parameter salah", 400

    nama = escape(permintaan_baru["nama"].strip())

    # Tambah permintaan baru
    hasil = us.tambah(
        nama,
        request.json['email'],

        request.json['kontak'],
        request.json['password']
    )

    # Pastikan berhasil
    if (hasil is None):
        return "Gagal menambah data!", 500

    return "Berhasi", 200


@ users.route('/daftar/<int:id>', methods=["GET"])
def getId(id):
    daftara = us.getId(id)

    if daftara != None:
        return json.loads(json.dumps(daftara.__dict__)), 200
    else:
        return {"error": "not found data"}, 200


@ users.route('/update/<int:id>', methods=["PUT"])
def update(id):

    permintaan_baru = request.get_json()
    nama = escape(permintaan_baru["nama"].strip())
    data = us.update(
        id,
        nama,
        request.json['email'],
        request.json['image'],
        request.json['kontak'],
        request.json['password'])

    return data, 200


@ users.route('/delete/<int:id>', methods=["DELETE"])
def delete(id):

    data = us.delete(id)

    return data, 200
