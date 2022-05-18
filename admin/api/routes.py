from api.model import tilawah as ti
from flask import render_template, request, jsonify

from api.model.tilawah.model import MateriTilawah
import json
from . import api
from google.cloud import datastore
modul_KIND = "MODUL"
latihan_KIND = "latihan"
tilawah_KIND = "tilawah"
diskusi_KIND = "DISKUSI"
mawaris_KIND = "mawaris"
fiqh_KIND = "FIQH"
tajwid_KIND = "TAJWID"
materiTilawah_KIND = "materi_tilawah"
materiMawaris_KIND = "materi_mawaris"
materiFiqh_KIND = "MATERI_FIQH"
materiTajwid_KIND = "MATERI_TAJWID"


@api.route('/tilawah')
def tilawah():
    client = datastore.Client()
    query = client.query(kind=tilawah_KIND)
    #query = client.query(kind="tilawah")
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


@api.route('/modul')
def modul():
    client = datastore.Client()
    query = client.query(kind=modul_KIND)
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


# @api.route('/materi/tema/<int:idTema>')
# def materi(idTema):
#     client = datastore.Client()
#     # Minta dibuatkan Key/Id baru untuk object baru
#     query = client.query(kind=materiMawaris_KIND)
#     query.add_filter("idTema", "=", idTema)
#     hasil = list(query.fetch())
#     hasil_baru = []
#     for data in hasil:
#         hasil_baru.append({
#             "id": data.id,
#             "judul": data['judul'],
#             "video": data['video'],
#             "idTema": data['idTema'],
#             "tema": data['tema'],

#         })
#     # return str(hasil_baru)
#     return jsonify({
#         "success": True,
#         "result": hasil_baru,
#         "code": 200}
#     ), 200


# @api.route('/materi/tilawah')
# def materiTilawah():
#     client = datastore.Client()
#     # Minta dibuatkan Key/Id baru untuk object baru
#     query = client.query(kind="materi_tilawah")
#     # query.add_filter("idTema", "=", idTema)
#     hasil = list(query.fetch())
#     hasil_baru = []
#     for data in hasil:
#         hasil_baru.append({
#             "id": data.id,
#             "judul": data['judul'],
#             "video": data['video'],
#             "idTema": data['idTema'],
#             "tema": data['tema'],

#         })
#     # return str(hasil_baru)
#     return jsonify({
#         "success": True,
#         "result": hasil_baru,
#         "code": 200}
#     ), 200


# @api.route('/materi/tajwid')
# def materiTajwid():
#     client = datastore.Client()
#     # Minta dibuatkan Key/Id baru untuk object baru
#     query = client.query(kind=materiTajwid_KIND)
#     # query.add_filter("idTema", "=", idTema)
#     hasil = list(query.fetch())
#     hasil_baru = []
#     for data in hasil:
#         hasil_baru.append({
#             "id": data.id,
#             "judul": data['judul'],
#             "video": data['video'],
#             "idTema": data['idTema'],
#             "tema": data['tema'],

#         })
#     # return str(hasil_baru)
#     return jsonify({
#         "success": True,
#         "result": hasil_baru,
#         "code": 200}
#     ), 200


# @api.route('/materi/mawaris')
# def materiMawaris():
#     client = datastore.Client()
#     # Minta dibuatkan Key/Id baru untuk object baru
#     query = client.query(kind="materi")
#     # query.add_filter("idTema", "=", idTema)
#     hasil = list(query.fetch())
#     hasil_baru = []
#     for data in hasil:
#         hasil_baru.append({
#             "id": data.id,
#             "judul": data['judul'],
#             "video": data['video'],
#             "idTema": data['idTema'],
#             "tema": data['tema'],

#         })
#     # return str(hasil_baru)
#     return jsonify({
#         "success": True,
#         "result": hasil_baru,
#         "code": 200}
#     ), 200


# @api.route('/materi/mawaris')
# def materiMawaris():
#     client = datastore.Client()
#     # Minta dibuatkan Key/Id baru untuk object baru
#     query = client.query(kind=materiMawaris_KIND)
#     # query.add_filter("idTema", "=", idTema)
#     hasil = list(query.fetch())
#     hasil_baru = []
#     for data in hasil:
#         hasil_baru.append({
#             "id": data.id,
#             "judul": data['judul'],
#             "tulisan": data['tulisan'],
#             "idTema": data['idTema'],
#             "tema": data['tema'],
#         })
#     # return str(hasil_baru)
#     return jsonify({
#         "success": True,
#         "result": hasil_baru,
#         "code": 200}
#     ), 200


@api.route('/materi/mawaris_video')
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


# @api.route('/latihan')
# def latihan():
#     client = datastore.Client()
#     # Minta dibuatkan Key/Id baru untuk object baru
#     query = client.query(kind="latihan")
#     hasil = list(query.fetch())
#     hasil_baru = []
#     for data in hasil:
#         hasil_baru.append({
#             "id": data.id,
#             "pertanyaan": data['pertanyaan'],
#             "pilihan1": data['pilihan1'],
#             "pilihan2": data['pilihan2'],
#             "pilihan3": data['pilihan3'],
#             "pilihan4": data['pilihan4'],
#             "jawaban": data['jawaban'],
#         })
#     # return str(hasil_baru)
#     return jsonify({
#         "success": True,
#         "result": hasil_baru,
#         "code": 200}
#     ), 200


@api.route('/latihan')
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
