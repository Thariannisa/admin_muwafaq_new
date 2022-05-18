from flask import Blueprint, jsonify, request, escape
import json
from api.model import permintaan as pr


permintaan = Blueprint("permintaan", __name__, url_prefix="/api")


@permintaan.route('/daftar', methods=["GET"])
def daftar():
    daftara = pr.daftar()

    def obj_dict(obj):
        return obj.__dict__
    print(daftara[0].nama)
    hasil = json.dumps(daftara, default=obj_dict)
    # Muat template
    return {"daftar": json.loads(hasil)}, 200
    return "coba"


@permintaan.route("/tambah_data", methods=["POST"])
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
    if "ulang" not in permintaan_baru.keys():
        return "Parameter salah", 400

    nama = escape(permintaan_baru["nama"].strip())
    ulang = permintaan_baru["ulang"]

    # Tambah permintaan baru
    hasil = pr.tambah(nama, ulang)

    # Pastikan berhasil
    if (hasil is None):
        return "Gagal menambah data!", 500

    return "Berhasi", 200


@permintaan.route('/daftar/<int:id>', methods=["GET"])
def getId(id):
    daftara = pr.getId(id)

    if daftara != None:
        return json.loads(json.dumps(daftara.__dict__)), 200
    else:
        return {"error": "not found data"}, 200


@permintaan.route('/update/<int:id>', methods=["PUT"])
def update(id):

    permintaan_baru = request.get_json()
    nama = escape(permintaan_baru["nama"].strip())
    ulang = permintaan_baru["ulang"]

    data = pr.update(id, nama, ulang)

    return data, 200


@permintaan.route('/delete/<int:id>', methods=["DELETE"])
def delete(id):

    data = pr.delete(id)

    return data, 200
