import logging
from api.model.umum.model import MateriUmum, materiUmum_KIND, umum_KIND
import datetime
import os
from xml.etree.ElementTree import dump

from flask import Flask, flash, jsonify, render_template, request, redirect
from api import model
from api.model.admin.check_login import check_login
from api.model.exception.model import EntityNotFoundException
from form.forms import (
    AddTemaForm,
    EditTulisanForm,
    KontenTulisanForm,
    KontenVideoForm,
    KontenVideo2Form,


)
from . import umum
from google.cloud import datastore
from google.cloud import storage


@umum.route('/')
@check_login
def mainumum(dataumum):
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
    return render_template('materi/umum/index_umum.html', data=hasil_baru, title="umum")


@umum.route('/tambahtema')
def addTema():
    form = AddTemaForm()
    return render_template('materi/umum/tema/add_tema.html', form=form)


@umum.route('/daftartema', methods=['POST'])
def daftartema():
    Tema = request.form['tema']
    # jenis_konten = request.form['konten']
    hasil = {}
    hasil["tema"] = Tema
    # hasil["konten"] = jenis_konten
    client = datastore.Client()
    # Minta dibuatkan Key/Id baru untuk object baru
    key_baru = client.key(umum_KIND)
    # Minta dibuatkan entity di datastore memakai key baru
    entity_baru = datastore.Entity(key=key_baru)
    # Simpan object Permintaan ke entity baru
    entity_baru.update(hasil)
    # Simpan entity ke datastore
    client.put(entity_baru)
    return redirect('/umum')


@umum.route('/detail_video/<int:idTema>')
def detailTemaVideo(idTema):
    client = datastore.Client()
    # Minta dibuatkan Key/Id baru untuk object baru
    query = client.query(kind=materiUmum_KIND)
    query.add_filter("idTema", "=", idTema)
    hasil = query.fetch()
    res = client.get(client.key(umum_KIND, idTema))
    hasil_baru = []
    for data in hasil:
        hasil_baru.append({
            "id": data.id,
            "judul": data['judul'],
            "video": data['video'],
            "tulisan": data['tulisan'],
            "author": data['author'],
            "idTema": data['idTema'],
            "tema": data['tema']
        })
    context = {
        "data": hasil_baru,
        "tema": res["tema"],
        # "konten": res["konten"],
    }
    return render_template('materi/umum/tema/tema_video.html', data=context)


@umum.route('/tambahvideo')
def addKontenVideo():
    form = KontenVideo2Form()
    client = datastore.Client()
    query = client.query(kind=umum_KIND)
    hasil = query.fetch()
    hasil_tema = []
    for data in hasil:
        hasil_tema.append({
            "tema": data['tema'],
            "idTema": data.id
        })
    return render_template('materi/umum/tema/add_video.html', data=hasil_tema, form=form)


@umum.route('/daftarvideo', methods=['POST'])
def daftarKontenVideo():
    Tema = request.form['idTema']
    client = datastore.Client()
    query = client.query(kind=umum_KIND)
    query.add_filter("tema", "=", Tema)
    data1 = list(query.fetch())
    Judul = request.form['judul']
    Tulisan = request.form['tulisan']
    author = request.form['author']
    Video = uploadVideo(request)
    # Video = request.form['video']
    idTema = str(data1[0].id)
    hasil = {}
    hasil["judul"] = Judul
    hasil["author"] = author
    hasil['tulisan'] = Tulisan
    hasil["tema"] = Tema
    hasil["idTema"] = int(idTema)
    hasil["video"] = Video
    client = datastore.Client()
    # Minta dibuatkan Key/Id baru untuk object baru
    key_baru = client.key(materiUmum_KIND)
    # Minta dibuatkan entity di datastore memakai key baru
    entity_baru = datastore.Entity(key=key_baru)
    # Simpan object Permintaan ke entity baru
    entity_baru.update(hasil)
    # Simpan entity ke datastore
    client.put(entity_baru)
    return redirect('/umum/detail_video/' + idTema)


# @umum.route('/tambahpembahasan')
# def addKontenTulisan():
#     form = KontenTulisanForm()
#     client = datastore.Client()
#     query = client.query(kind=umum_KIND)
#     hasil = query.fetch()
#     hasil_tema = []
#     for data in hasil:
#         hasil_tema.append({
#             "tema": data['tema'],
#             "idTema": data.id
#         })
#     return render_template('materi/umum/tema/add_Tulisan.html', data=hasil_tema, form=form)


# @umum.route('/daftartulisan', methods=['POST'])
# def daftarKontenTulisan():

#     Tema = request.form['idTema']
#     client = datastore.Client()
#     query = client.query(kind=umum_KIND)
#     query.add_filter("tema", "=", Tema)
#     data1 = list(query.fetch())
#     Judul = request.form['judul']
#     Tulisan = request.form['tulisan']
#     idTema = str(data1[0].id)
#     hasil = {}
#     hasil["judul"] = Judul
#     hasil["tulisan"] = Tulisan
#     hasil['author'] = ""
#     hasil['video'] = ""
#     hasil["tema"] = Tema
#     hasil["idTema"] = int(idTema)
#     client = datastore.Client()
#     # Minta dibuatkan Key/Id baru untuk object baru
#     key_baru = client.key(materiUmum_KIND)
#     # Minta dibuatkan entity di datastore memakai key baru
#     entity_baru = datastore.Entity(key=key_baru)
#     # Simpan object Permintaan ke entity baru
#     entity_baru.update(hasil)
#     # Simpan entity ke datastore
#     client.put(entity_baru)
#     flash("Your materi has been added!", "success")
#     return redirect('/umum/detail_tulisan/' + idTema)


# @umum.route('/detail_tulisan/<int:idTema>')
# def detailTemaTulisan(idTema):
#     client = datastore.Client()
#     # Minta dibuatkan Key/Id baru untuk object baru
#     query = client.query(kind=materiUmum_KIND)
#     query.add_filter("idTema", "=", idTema)
#     hasil = query.fetch()
#     res = client.get(client.key(umum_KIND, idTema))
#     hasil_baru = []
#     for data in hasil:
#         hasil_baru.append({
#             "id": data.id,
#             "judul": data['judul'],
#             "tulisan": data['tulisan'],
#             "idTema": data['idTema'],
#             "tema": data['tema']
#         })
#     context = {
#         "data": hasil_baru,
#         "tema": res["tema"],
#         # "konten": res["konten"]
#     }
#     return render_template('materi/umum/tema/tema_tulisan.html', data=context)


def uploadVideo(request):
    uploaded_file = request.files.get("video")
    if not uploaded_file:
        return ""
    try:
        split = os.path.splitext(uploaded_file.filename)
        if split[1] not in [".mp4", ".MOV"]:
            return None
        # check size
        read = uploaded_file.read()
        size = len(read)
        if size >= 40000000:  # 40 mb
            return None
        # Create a Cloud Storage client.
        gcs = storage.Client()
        # Get the bucket that the file will be uploaded to.
        bucket = gcs.get_bucket("ta-fahmil.appspot.com")
        # Create a new blob and upload the file's content.
        dt = str(datetime.datetime.now())
        blob = bucket.blob(split[0] + dt + split[1])
        blob.upload_from_string(read, content_type=uploaded_file.content_type)
        blob.make_public()

        # The public URL can be used to directly access the uploaded file via HTTP.
        return str(blob.public_url)
    except:

        return ""


@umum.route('/deletekontenvideo/<int:id>/<int:idTema>', methods=['GET', 'POST'])
def deleteKontenVideo(id, idTema):
    # Buat object hanya jika kedua data ada
    if id != None:
        # Sambung ke datastore
        client = datastore.Client()
        entity = client.get(client.key(materiUmum_KIND, id))

        if entity != None:
            client.delete(entity)
            return redirect('/umum/detail_video/' + str(idTema))
    else:
        return "gagal"


# @umum.route('/deletekontentulisan/<int:id>/<int:idTema>', methods=['GET', 'POST'])
# def deleteKontenTulisan(id, idTema):
#     # Buat object hanya jika kedua data ada
#     if id != None:
#         # Sambung ke datastore
#         client = datastore.Client()
#         entity = client.get(client.key(materiUmum_KIND, id))

#         if entity != None:
#             client.delete(entity)
#             return redirect('/umum/detail_tulisan/' + str(idTema))
#     else:
#         return "gagal"


@umum.route('/deletetema/<int:id>', methods=['GET', 'POST'])
def deleteTema(id):
    # Buat object hanya jika kedua data ada
    if id != None:
        # Sambung ke datastore
        client = datastore.Client()
        entity = client.get(client.key(umum_KIND, id))
        if entity != None:
            client.delete(entity)
            return redirect('/umum')
    else:
        return "gagal"


# @umum.route('/edit_tulisan/<int:id>/<int:idTema>',  methods=["GET", "POST"])
# def edit_tulisan(id, idTema):
#     form = KontenTulisanForm()
#     # Lakukan pencarian materi berdasar id
#     try:
#         cari_materi = model.umum.atur.cari(id)
#     except:

#         return f"Gagal mencari materi dengan id: {id}.", 400
#     # Pastikan berhasil
#     if cari_materi is None:
#         return f"Gagal mencari materi dengan id: {id}.", 400
#     return render_template('materi/umum/tema/edit_Tulisan.html/', form=form, data=cari_materi)


# @umum.route('/updatetulisan/<int:id>/<int:idTema>', methods=["POST"])
# def ubah_tulisan(id, idTema):
#     Tema = request.form['idTema']
#     client = datastore.Client()
#     query = client.query(kind=umum_KIND)
#     query.add_filter("tema", "=", Tema)
#     data1 = list(query.fetch())
#     Judul = request.form['judul']
#     Tulisan = request.form['tulisan']
#     idTema = str(data1[0].id)
#     hasil = {}
#     hasil["judul"] = Judul
#     hasil["tulisan"] = Tulisan
#     hasil['author'] = ""
#     hasil['video'] = ""
#     hasil["tema"] = Tema
#     hasil["idTema"] = int(idTema)
#     client = datastore.Client()
#     # Minta dibuatkan Key/Id baru untuk object baru
#     key = client.key(materiUmum_KIND, id)
#     # Minta dibuatkan entity di datastore memakai key baru
#     entity = datastore.Entity(key=key)
#     # Simpan object Permintaan ke entity baru
#     entity.update(hasil)
#     # Simpan entity ke datastore
#     client.put(entity)
#     return redirect('/umum/detail_tulisan/' + str(idTema))


@umum.route('/edit_video/<int:id>/<int:idTema>',  methods=["GET", "POST"])
def edit_video(id, idTema):
    form = KontenVideoForm()
    # Lakukan pencarian materi berdasar id
    try:
        cari_materi = model.umum.atur.cari(id)
    except:
        return f"Gagal mencari materi dengan id: {id}.", 400
    # Pastikan berhasil
    if cari_materi is None:
        return f"Gagal mencari materi dengan id: {id}.", 400
    return render_template('materi/umum/tema/edit_video.html/', form=form, data=cari_materi)


@umum.route('/updatevideo/<int:id>/<int:idTema>', methods=["POST"])
def ubah_video(id, idTema):
    Tema = request.form['idTema']
    client = datastore.Client()
    query = client.query(kind=umum_KIND)
    query.add_filter("tema", "=", Tema)
    data1 = list(query.fetch())
    Judul = request.form['judul']
    Tulisan = request.form['tulisan']
    author = request.form['author']
    Video = uploadVideo(request)
    idTema = str(data1[0].id)
    hasil = {}
    hasil["judul"] = Judul
    hasil["author"] = author
    hasil['tulisan'] = Tulisan
    hasil["tema"] = Tema
    hasil["idTema"] = int(idTema)
    hasil["video"] = Video
    client = datastore.Client()
    # Minta dibuatkan Key/Id baru untuk object baru
    key = client.key(materiUmum_KIND, id)
    # Minta dibuatkan entity di datastore memakai key baru
    entity = datastore.Entity(key=key)
    # Simpan object Permintaan ke entity baru
    entity.update(hasil)
    # Simpan entity ke datastore
    client.put(entity)
    return redirect('/umum/detail_video/' + idTema)
