from api.model import tilawah as ti
from flask import render_template, request, jsonify
from api.model.admin.check_login import check_login
from api.model.tilawah.model import MateriTilawah, materiTilawah_KIND, tilawah_KIND
from api.model.fathurrahman.model import MateriFathurahman, materiFathurahman_KIND, fathurahman_KIND
from api.model.umum.model import MateriUmum, materiUmum_KIND, umum_KIND
from api.model.mawaris.model import MateriMawaris, materiMawaris_KIND, mawaris_KIND
from api.model.fiqh.model import MateriFiqh, materiFiqh_KIND, fiqh_KIND
from api.model.tajwid.model import MateriTajwid, materiTajwid_KIND, tajwid_KIND
from api.model.modul.model import Modul, MODUL_KIND
from api.model.latihan.model import Latihan, latihan_KIND
from api.model.diskusi.model import Diskusi, diskusi_KIND
import json
from . import api
from google.cloud import datastore


@api.route('/tilawah')
# @check_login
def tilawah():
    client = datastore.Client()
    query = client.query(kind=tilawah_KIND)
    hasil = query.fetch()
    hasil_baru = []
    for data in hasil:
        hasil_baru.append({
            "idTema": data.id,
            "konten": data['konten'],
            "tema": data['tema']
        })
    # return str(hasil_baru)
    return jsonify({
        "success": True,
        "result": hasil_baru,
        "code": 200}
    ), 200


@api.route('/mawaris')
# @check_login
def mawaris():
    client = datastore.Client()
    query = client.query(kind=mawaris_KIND)
    hasil = query.fetch()
    hasil_baru = []
    for data in hasil:
        hasil_baru.append({
            "idTema": data.id,
            "konten": data['konten'],
            "tema": data['tema']
        })
    # return str(hasil_baru)
    return jsonify({
        "success": True,
        "result": hasil_baru,
        "code": 200}
    ), 200


@api.route('/tajwid')
# @check_login
def tajwid():
    client = datastore.Client()
    query = client.query(kind=tajwid_KIND)
    hasil = query.fetch()
    hasil_baru = []
    for data in hasil:
        hasil_baru.append({
            "idTema": data.id,
            "konten": data['konten'],
            "tema": data['tema']
        })
    # return str(hasil_baru)
    return jsonify({
        "success": True,
        "result": hasil_baru,
        "code": 200}
    ), 200


@api.route('/fiqh')
# @check_login
def fiqh():
    client = datastore.Client()
    query = client.query(kind=fiqh_KIND)
    hasil = query.fetch()
    hasil_baru = []
    for data in hasil:
        hasil_baru.append({
            "idTema": data.id,
            "konten": data['konten'],
            "tema": data['tema']
        })
    # return str(hasil_baru)
    return jsonify({
        "success": True,
        "result": hasil_baru,
        "code": 200}
    ), 200


@api.route('/fathurahman')
# @check_login
def fathurahman():
    client = datastore.Client()
    query = client.query(kind=fathurahman_KIND)
    hasil = query.fetch()
    hasil_baru = []
    for data in hasil:
        hasil_baru.append({
            "idTema": data.id,
            "konten": data['konten'],
            "tema": data['tema']
        })
    # return str(hasil_baru)
    return jsonify({
        "success": True,
        "result": hasil_baru,
        "code": 200}
    ), 200


@api.route('/umum')
# @check_login
def umum():
    client = datastore.Client()
    query = client.query(kind=umum_KIND)
    hasil = query.fetch()
    hasil_baru = []
    for data in hasil:
        hasil_baru.append({
            "idTema": data.id,
            # "konten": data['konten'],
            "tema": data['tema']
        })
    # return str(hasil_baru)
    return jsonify({
        "success": True,
        "result": hasil_baru,
        "code": 200}
    ), 200


@api.route('/modul')
# @check_login
def modul():
    client = datastore.Client()
    query = client.query(kind=MODUL_KIND)
    hasil = query.fetch()
    hasil_baru = []
    for data in hasil:
        hasil_baru.append({
            "id": data.id,
            "judul": data['judul'],
            "PDF": data['PDF']
        })
    # return str(hasil_baru)
    return jsonify({
        "success": True,
        "result": hasil_baru,
        "code": 200}
    ), 200


@api.route('/materi/mawaris_video')
# @check_login
def materiMawarisVideo():
    client = datastore.Client()
    # Minta dibuatkan Key/Id baru untuk object baru
    query = client.query(kind=materiMawaris_KIND)
    # query.add_filter("idTema", "=", idTema)
    hasil = list(query.fetch())
    hasil_baru = []
    for data in hasil:
        hasil_baru.append({
            "id": data.id,
            "judul": data['judul'],
            "author": data['author'],
            "video": data['video'],
            "idTema": data['idTema'],
            "tema": data['tema'],
        })
    # return str(hasil_baru)
    return jsonify({
        "success": True,
        "result": hasil_baru,
        "code": 200}
    ), 200


@api.route('/materi/detail/<int:id>')
# @check_login
def detailTulisan(id):
    client = datastore.Client()
    # Minta dibuatkan Key/Id baru untuk object baru
    query = client.query(kind=materiMawaris_KIND)
    # query.add_filter("idTema", "=", idTema)
    hasil = list(query.fetch())
    hasil_baru = []
    for data in hasil:
        hasil_baru.append({
            "id": data.id,
            "judul": data['judul'],
            "video": data['video'],
            "idTema": data['idTema'],
            "tema": data['tema'],

        })
    # return str(hasil_baru)
    return jsonify({
        "success": True,
        "result": hasil_baru,
        "code": 200}
    ), 200


@api.route('/materi/tilawah_video')
# @check_login
def materiTilawahVideo():
    client = datastore.Client()
    # Minta dibuatkan Key/Id baru untuk object baru
    query = client.query(kind=materiTilawah_KIND)
    # query.add_filter("idTema", "=", idTema)
    hasil = list(query.fetch())
    hasil_baru = []
    for data in hasil:
        hasil_baru.append({
            "id": data.id,
            "judul": data['judul'],
            "author": data['author'],
            "video": data['video'],
            "idTema": data['idTema'],
            "tema": data['tema'],
        })
    # return str(hasil_baru)
    return jsonify({
        "success": True,
        "result": hasil_baru,
        "code": 200}
    ), 200


@api.route('/latihan')
# @check_login
def latihan():
    client = datastore.Client()
    # Minta dibuatkan Key/Id baru untuk object baru
    query = client.query(kind=latihan_KIND)
    hasil = list(query.fetch())
    hasil_baru = []
    for data in hasil:
        hasil_baru.append({
            "id": data.id,
            "pertanyaan": data['pertanyaan'],
            "pilihan1": data['pilihan1'],
            "pilihan2": data['pilihan2'],
            "pilihan3": data['pilihan3'],
            "pilihan4": data['pilihan4'],
            "jawaban": data['jawaban'],
        })
    # return str(hasil_baru)
    return jsonify({
        "success": True,
        "result": hasil_baru,
        "code": 200}
    ), 200


@api.route('/diskusi')
# @check_login
def diskusi():
    client = datastore.Client()
    query = client.query(kind=diskusi_KIND)
    hasil = query.fetch()
    hasil_baru = []
    for data in hasil:
        hasil_baru.append({
            "id": data.id,
            "platform": data['platform'],
            "link": data['link'],
            "keterangan": data['keterangan']
        })
    # return str(hasil_baru)
    return jsonify({
        "success": True,
        "result": hasil_baru,
        "code": 200}
    ), 200


@api.route('/daftar_tilawah/<int:id>', methods=["GET"])
def getId(id):
    daftara = ti.getId(id)

    if daftara != None:
        return json.loads(json.dumps(daftara.__dict__)), 200
    else:
        return {"error": "not found data"}, 200


@api.route('/materi/tilawahAll')
# @check_login
def materiTilawahAll():
    client = datastore.Client()
    # Minta dibuatkan Key/Id baru untuk object baru
    query = client.query(kind=materiTilawah_KIND)
    # query.add_filter("idTema", "=", idTema)
    hasil = list(query.fetch())
    hasil_baru = []
    for data in hasil:
        hasil_baru.append({
            "id": data.id,
            "judul": data['judul'],
            "author": data['author'],
            "video": data['video'],
            "tulisan": data['tulisan'],
            "idTema": data['idTema'],
            "tema": data['tema'],
        })
    # return str(hasil_baru)
    return jsonify({
        "success": True,
        "result": hasil_baru,
        "code": 200}
    ), 200


@api.route('/materi/fiqhAll')
# @check_login
def materiFiqhAll():
    client = datastore.Client()
    # Minta dibuatkan Key/Id baru untuk object baru
    query = client.query(kind=materiFiqh_KIND)
    # query.add_filter("idTema", "=", idTema)
    hasil = list(query.fetch())
    hasil_baru = []
    for data in hasil:
        hasil_baru.append({
            "id": data.id,
            "judul": data['judul'],
            "author": data['author'],
            "video": data['video'],
            "tulisan": data['tulisan'],
            "idTema": data['idTema'],
            "tema": data['tema'],
        })
    # return str(hasil_baru)
    return jsonify({
        "success": True,
        "result": hasil_baru,
        "code": 200}
    ), 200


@api.route('/materi/mawarisAll')
# @check_login
def materiMawarisAll():
    client = datastore.Client()
    # Minta dibuatkan Key/Id baru untuk object baru
    query = client.query(kind=materiMawaris_KIND)
    # query.add_filter("idTema", "=", idTema)
    hasil = list(query.fetch())
    hasil_baru = []
    for data in hasil:
        hasil_baru.append({
            "id": data.id,
            "judul": data['judul'],
            "author": data['author'],
            "video": data['video'],
            "tulisan": data['tulisan'],
            "idTema": data['idTema'],
            "tema": data['tema'],
        })
    # return str(hasil_baru)
    return jsonify({
        "success": True,
        "result": hasil_baru,
        "code": 200}
    ), 200


@api.route('/materi/TajwidAll')
# @check_login
def materiTajwidAll():
    client = datastore.Client()
    # Minta dibuatkan Key/Id baru untuk object baru
    query = client.query(kind=materiTajwid_KIND)
    # query.add_filter("idTema", "=", idTema)
    hasil = list(query.fetch())
    hasil_baru = []
    for data in hasil:
        hasil_baru.append({
            "id": data.id,
            "judul": data['judul'],
            "author": data['author'],
            "video": data['video'],
            "tulisan": data['tulisan'],
            "idTema": data['idTema'],
            "tema": data['tema'],
        })
    # return str(hasil_baru)
    return jsonify({
        "success": True,
        "result": hasil_baru,
        "code": 200}
    ), 200


@api.route('/materi/FathurahmanAll')
# @check_login
def materiFathurahmandAll():
    client = datastore.Client()
    # Minta dibuatkan Key/Id baru untuk object baru
    query = client.query(kind=materiFathurahman_KIND)
    # query.add_filter("idTema", "=", idTema)
    hasil = list(query.fetch())
    hasil_baru = []
    for data in hasil:
        hasil_baru.append({
            "id": data.id,
            "judul": data['judul'],
            "author": data['author'],
            "video": data['video'],
            "tulisan": data['tulisan'],
            "idTema": data['idTema'],
            "tema": data['tema'],
        })
    # return str(hasil_baru)
    return jsonify({
        "success": True,
        "result": hasil_baru,
        "code": 200}
    ), 200


@api.route('/materi/UmumAll')
# @check_login
def materiUmumdAll():
    client = datastore.Client()
    # Minta dibuatkan Key/Id baru untuk object baru
    query = client.query(kind=materiUmum_KIND)
    # query.add_filter("idTema", "=", idTema)
    hasil = list(query.fetch())
    hasil_baru = []
    for data in hasil:
        hasil_baru.append({
            "id": data.id,
            "judul": data['judul'],
            "author": data['author'],
            "video": data['video'],
            "tulisan": data['tulisan'],
            "idTema": data['idTema'],
            "tema": data['tema'],
        })
    # return str(hasil_baru)
    return jsonify({
        "success": True,
        "result": hasil_baru,
        "code": 200}
    ), 200
